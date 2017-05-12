# -*- coding: utf-8 -*-
import re

from sischan.constant import Constants
from sischan.helper import time_to_next_utc_mt
from sischan.rss import is_valid_feed_url, validate_and_create_entry

DEFAULT_NICKNAME = "onii-chan"


def process_command(redis_client, recipient_id, query):
    # TODO: Check admin status (for admin-only help menu)
    if query == "subscribe offerings":
        return process_subscribe_offerings(redis_client, recipient_id)
    elif query == "unsubscribe offerings":
        return process_unsubscribe_offerings(redis_client, recipient_id)
    elif query == "update offerings":
        return process_update_offerings(redis_client, recipient_id)
    elif query == "subscribe japanese":
        return process_subscribe_japanese(redis_client, recipient_id)
    elif query == "unsubscribe japanese":
        return process_unsubscribe_japanese(redis_client, recipient_id)
    elif query == "update japanese":
        return process_update_japanese(redis_client, recipient_id)
    elif query == "update name":
        return process_update_name(redis_client, recipient_id)
    elif query == "subscribe rss":
        return process_subscribe_rss(redis_client, recipient_id)
    elif query == "unsubscribe rss":
        return process_unsubscribe_rss(redis_client, recipient_id)
    elif query == "show profile":
        return process_show_profile(redis_client, recipient_id)
    # query "help" as default query
    return process_help(redis_client, recipient_id)


def process_active_question(redis_client, recipient_id, question_id, query):
    redis_client.set_active_question(recipient_id, -1)  # Set back to default
    if question_id == 1:
        return process_morning_question(redis_client, recipient_id, query)
    elif question_id == 2:
        return process_night_question(redis_client, recipient_id, query)
    elif question_id == 3:
        return process_kanji_level_question(redis_client, recipient_id, query)
    elif question_id == 4:
        return process_update_name_question(redis_client, recipient_id, query)
    elif question_id == 5:
        return process_rss_source_selection(redis_client, recipient_id, query)
    elif question_id == 6:
        return process_default_preset(redis_client, recipient_id, query)
    elif question_id == 7:
        return process_rss_url(redis_client, recipient_id, query)
    elif question_id == 8:
        return process_rss_pattern(redis_client, recipient_id, query)
    elif question_id == 9:
        return process_rss_removal(redis_client, recipient_id, query)
    return "<3"


def process_help(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    message = "Hello {}, welcome to Sistine-chan Help System!\n\n".format(
        user.get("nickname", DEFAULT_NICKNAME)
    )
    message += "You could ask me for these commands:\n"
    for keyword in Constants.RESERVED_KEYWORDS:
        message += "- \"{}\": {}\n".format(
            keyword[0],
            keyword[1]
        )

    message += "\nSistine-chan also has the following features:\n"
    for feature in Constants.FEATURES:
        message += "- \"{}\": {}\n".format(
            feature[0],
            feature[1]
        )

    message += "\nOh, and also, time is handled in UTC+9 (Japan time), te-hee~"
    return message


def process_subscribe_offerings(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    if user["offerings_status"] == "subscribed":
        return "You have been subscribed to Sistine-chan offerings, {}!".format(
            user.get("nickname", DEFAULT_NICKNAME)
        )
    # Update DB information
    user["offerings_status"] = "subscribed"
    redis_client.set_user(recipient_id, user)
    # Ask for user's preference
    message = "Thanks for subscribing to Sistine-chan offerings <3\n"
    redis_client.set_active_question(recipient_id, 1)
    message += Constants.QUESTIONS[1].format(
        user.get("nickname", DEFAULT_NICKNAME)
    )
    return message


def process_unsubscribe_offerings(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    # Update DB information
    user["offerings_status"] = "unsubscribed"
    # Remove schedule
    if "morning_offerings_mt" in user["schedules"]:
        del user["schedules"]["morning_offerings_mt"]
    if "night_offerings_mt" in user["schedules"]:
        del user["schedules"]["night_offerings_mt"]
    redis_client.set_user(recipient_id, user)
    return "Sistine-chan wish she could serve {} in the future :)".format(
        user.get("nickname", DEFAULT_NICKNAME)
    )


def process_update_offerings(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    if user["offerings_status"] != "subscribed":
        return "You need to subscribe first, {}!".format(
            user.get("nickname", DEFAULT_NICKNAME)
        )
    # Ask for user's preference
    redis_client.set_active_question(recipient_id, 1)
    return Constants.QUESTIONS[1].format(
        user.get("nickname", DEFAULT_NICKNAME)
    )


def process_subscribe_japanese(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    if user["japanese_status"] == "subscribed":
        return "You have been subscribed to Japanese lesson, {}!".format(
            user.get("nickname", DEFAULT_NICKNAME)
        )
    # Update DB information
    user["japanese_status"] = "subscribed"
    user["schedules"]["japanese_lesson_mt"] = time_to_next_utc_mt(
        Constants.DEFAULT_JAPANESE_TIME
    )
    redis_client.set_user(recipient_id, user)
    # Ask for user's preference
    message = "Thanks for subscribing to Sistine-chan Japanese lessons <3\n"
    redis_client.set_active_question(recipient_id, 3)
    message += Constants.QUESTIONS[3].format(
        user.get("nickname", DEFAULT_NICKNAME)
    )
    return message


def process_unsubscribe_japanese(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    # Update DB information
    user["japanese_status"] = "unsubscribed"
    # Remove schedule
    if "japanese_lesson_mt" in user["schedules"]:
        del user["schedules"]["japanese_lesson_mt"]
    redis_client.set_user(recipient_id, user)
    return "Sistine-chan wish she could serve {} in the future :)".format(
        user.get("nickname", DEFAULT_NICKNAME)
    )


def process_update_japanese(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    if user["japanese_status"] != "subscribed":
        return "You need to subscribe first, {}!".format(
            user.get("nickname", DEFAULT_NICKNAME)
        )
    # Ask for user's preference
    redis_client.set_active_question(recipient_id, 3)
    return Constants.QUESTIONS[3].format(
        user.get("nickname", DEFAULT_NICKNAME)
    )


def process_update_name(redis_client, recipient_id):
    redis_client.set_active_question(recipient_id, 4)
    return Constants.QUESTIONS[4]


def process_subscribe_rss(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    redis_client.set_active_question(recipient_id, 5)
    return Constants.QUESTIONS[5].format(
        user.get("nickname", DEFAULT_NICKNAME)
    )


def process_unsubscribe_rss(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    if user["rss"]:
        redis_client.set_active_question(recipient_id, 9)
        message = Constants.QUESTIONS[9].format(
            user.get("nickname", DEFAULT_NICKNAME)
        )
        message += "\n"
        for key, entry in user["rss"].iteritems():
            message += "{}: URL = \"{}\" and pattern = \"{}\"\n".format(
                key,
                entry["url"],
                entry["pattern"]
            )
    else:
        message = "Your RSS subscription is currently empty!"
    return message


def process_show_profile(redis_client, recipient_id):
    user = redis_client.get_user(recipient_id)
    message = "Hi, {}!\n\n".format(user.get("nickname", DEFAULT_NICKNAME))
    if not user.get("nickname"):
        message += "Sistine-chan haven't learned how to call you properly :'(\n\n"
    # Offerings Section
    message += "Offerings status: {}\n".format(user["offerings_status"])
    if user["offerings_status"] == "subscribed":
        message += "Morning message: around {} UTC+9\n".format(
            user["morning_time"]
        )
        message += "Night message: around {} UTC+9\n".format(
            user["night_time"]
        )
    # Japanese Section
    message += "Japanese status: {}\n".format(user["japanese_status"])
    if user["japanese_status"] == "subscribed":
        message += "Kanji level: {}\n".format(user["kanji_level"])
    # RSS Section
    if user["rss"]:
        message += "RSS Subscription status:\n"
        for entry in user["rss"].values():
            message += "- URL = \"{}\" and pattern = \"{}\"\n".format(
                entry["url"],
                entry["pattern"]
            )
    return message


def process_morning_question(redis_client, recipient_id, query):
    user = redis_client.get_user(recipient_id)
    match = re.search(r'^([01]?\d|2[0-3]):([0-5]?\d)$', query)
    if not match:
        user["morning_time"] = Constants.DEFAULT_MORNING_TIME
        message = "Since I couldn't understand your message, "
        message += "I set your morning time to {} UTC+9, sorry :(\n".format(
            Constants.DEFAULT_MORNING_TIME
        )
    else:
        user["morning_time"] = match.group(0)
        message = "Thank you!\n"
    metadata = redis_client.get_schedules()
    next_mt = time_to_next_utc_mt(user["morning_time"])
    next_mt += metadata.get("morning_offering_mt_offset", 0)
    night_mt = user["schedules"].get("night_offerings_mt")
    if not night_mt or next_mt < night_mt:
        if night_mt:  # Replace
            del user["schedules"]["night_offerings_mt"]
        user["schedules"]["morning_offerings_mt"] = next_mt
    redis_client.set_user(recipient_id, user)
    redis_client.set_active_question(recipient_id, 2)
    message += Constants.QUESTIONS[2].format(
        user.get("nickname", DEFAULT_NICKNAME)
    )
    return message


def process_night_question(redis_client, recipient_id, query):
    user = redis_client.get_user(recipient_id)
    match = re.search(r'^([01]?\d|2[0-3]):([0-5]?\d)$', query)
    if not match:
        user["night_time"] = Constants.DEFAULT_NIGHT_TIME
        message = "Since I couldn't understand your message, "
        message += "I set your night time to {} UTC+9, sorry :(\n".format(
            Constants.DEFAULT_NIGHT_TIME
        )
    else:
        user["night_time"] = match.group(0)
        message = "Thank you for answering Sistine-chan question!\n"
    metadata = redis_client.get_schedules()
    next_mt = time_to_next_utc_mt(user["night_time"])
    next_mt += metadata.get("night_offering_mt_offset", 0)
    morning_mt = user["schedules"].get("morning_offerings_mt")
    if not morning_mt or next_mt < morning_mt:
        if morning_mt:  # Replace
            del user["schedules"]["morning_offerings_mt"]
        user["schedules"]["night_offerings_mt"] = next_mt
    redis_client.set_user(recipient_id, user)
    message += "Your information for my offerings has been updated <3"
    return message


def process_kanji_level_question(redis_client, recipient_id, query):
    user = redis_client.get_user(recipient_id)
    match = re.search(r'^N[1-4]$', query)
    if not match:
        user["kanji_level"] = "N3"
        message = "Since I couldn't understand your message, "
        message += "I set your Kanji level to N3, sorry :("
    else:
        user["kanji_level"] = match.group(0)
        message = "Your information for Kanji level has been updated <3"
    redis_client.set_user(recipient_id, user)
    return message


def process_update_name_question(redis_client, recipient_id, query):
    user = redis_client.get_user(recipient_id)
    # Ensure name is not empty or space-only
    if not query or query.isspace():
        return "That's not a proper name, buu-buu~"
    # Update DB information
    user["nickname"] = query
    redis_client.set_user(recipient_id, user)
    message = "Sistine-chan will start calling you {} from now onwards!\n".format(
        user.get("nickname", DEFAULT_NICKNAME)
    )
    message += "よろしくお願いします~"
    return message


def process_rss_source_selection(redis_client, recipient_id, query):
    if query == "1" or query.lower() == "preset":
        message = "Thank you!\n"
        redis_client.set_active_question(recipient_id, 6)
        message += Constants.QUESTIONS[6]
        message += "\n"
        for k, v in Constants.DEFAULT_RSS_PRESET.iteritems():
            message += "Type {} for {}\n".format(k, v["title"])
    elif query == "2" or query.lower() == "custom":
        message = "Thank you!\n"
        redis_client.set_active_question(recipient_id, 7)
        message += Constants.QUESTIONS[7]
    else:
        message = "Sorry, your choice is not recognized!"
    return message


def process_default_preset(redis_client, recipient_id, query):
    user = redis_client.get_user(recipient_id)
    if query not in Constants.DEFAULT_RSS_PRESET.keys():
        message = "Sorry, your preset is not recognized!"
    else:
        preset = Constants.DEFAULT_RSS_PRESET[query]
        user["temp_rss_url"] = preset["url"]
        redis_client.set_user(recipient_id, user)
        redis_client.set_active_question(recipient_id, 8)
        message = Constants.QUESTIONS[8]
    return message


def process_rss_url(redis_client, recipient_id, query):
    user = redis_client.get_user(recipient_id)
    if is_valid_feed_url(query):
        user["temp_rss_url"] = query
        redis_client.set_user(recipient_id, user)
        redis_client.set_active_question(recipient_id, 8)
        message = Constants.QUESTIONS[8]
    else:
        message = "Sorry, your URL feed is not valid!"
    return message


def process_rss_pattern(redis_client, recipient_id, query):
    user = redis_client.get_user(recipient_id)
    entry = validate_and_create_entry(
        user.get("temp_rss_url"),
        query
    )
    if entry:
        user["rss_id"] += 1  # Increment ID
        user["rss"][user["rss_id"]] = entry
        message = "Your RSS subscription has been updated!"
    else:
        message = "Sorry, Sistine-chan seems confused with your entry >_<"
    if "temp_rss_url" in user:
        del user["temp_rss_url"]  # Remove temporary reference
    redis_client.set_user(recipient_id, user)
    return message


def process_rss_removal(redis_client, recipient_id, query):
    user = redis_client.get_user(recipient_id)
    if query in user["rss"]:
        del user["rss"][query]
        redis_client.set_user(recipient_id, user)
        message = "Your RSS subscription has been updated!"
    else:
        message = "Sorry, Sistine-chan could not recognize the given number!"
    return message
