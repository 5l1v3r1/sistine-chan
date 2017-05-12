# -*- coding: utf-8 -*-


class Constants(object):
    # See command.py for implementation
    RESERVED_KEYWORDS = [
        ("help", "Sistine-chan will show you these texts"),
        ("subscribe offerings", "Sistine-chan will start sending a good morning & a good night messages"),
        ("unsubscribe offerings", "Sistine-chan will stop sending you a good morning & a good night messages, but Sistine-chan will be sad :'("),
        ("update offerings", "Sistine-chan will keep her best to follow your waking up and sleeping time pattern!"),
        ("subscribe japanese", "Sistine-chan will start sending you daily Japanese Kanji & Vocabulary"),
        ("unsubscribe japanese", "Sistine-chan will stop sending you daily Japanese Kanji & Vocabulary"),
        ("update japanese", "Sistine-chan will ask you about Kanji level selection (N1-N4, old test format)"),
        ("update name", "What name do you prefer to be called? onii-chan? goshujin-sama? or perhaps, ... darling?"),
        ("subscribe rss", "[Experimental] Sistine-chan will guide you through RSS Feed subscription, e.g.: manga, nyaa"),
        ("unsubscribe rss", "[Experimental] Sistine-chan will remove RSS Feed which you want to stop subscribing"),
        ("show profile", "Sistine-chan will show all information which Sistine-chan knows about you"),
    ]

    FEATURES = [
        ("upload picture", "Sistine-chan will convert it to a primivite image, but it might take several minutes"),
        ("simple chatbot", "Sistine-chan will try her best to engage in a conversation!"),
        ("translate", "[Experimental] Sistine-chan will ask Google-sensei for the translation from/to Indonesian, English, and Japanese (with language detection)")
    ]

    QUESTIONS = {
        1: "What time do you usually wake up in the morning, {}? (e.g.: 9:00)",
        2: "What time do you usually sleep, {}? (e.g.: 23:00)",
        3: "Which level of Kanji do you want to learn between N1-N4, {}? (e.g.: N3)",
        4: "How should Sistine-chan call you? onii-chan? goshujin-sama? or perhaps, ... darling?",
        5: "Do you want to use preset RSS feed or add a custom one, {}? (Type 1 for preset, 2 for custom)",
        6: "Which preset do you want to use?",
        7: "Which RSS feed do you want to use? (e.g.: http://mangastream.com/rss)",
        8: "What is the title (regex pattern) that you want to use? (e.g.: Shokugeki no Soma, or .* to match all)",
        9: "Which number of subscription do you want to remove, {}?"
    }

    NORMAL_GOOD_MORNING = [
        "おはよう! Wishing you a good day ahead, {} <3",
        "Ohaa~ I had a nice dream last night. Hope {} also had one!",
        "Good morning, {}. I feel you will have a nice day today!",
        "Ohayou gozaimasu, {}! Don't forget to exercise!",
        "Morning, {}. It's time to wake up :D",
        "Good morning to you, {}",
        "Ohaa~ Time to get up already, {}",
        "Guten Morgen, {}. A new day means a new hope, がんばって!",
        "Good morning, {}! Don't forget to eat healthy food!"
    ]

    NORMAL_GOOD_NIGHT = [
        "おやすみ, {}! Have a nice dream and rest tonight <3",
        "Oyasumi, {}~ Today was fun and thanks for keep talking with me, nyaa~",
        "Good night, {}. I hope you will have a nice sleep tonight zzz...",
        "Have a nice sleep, {} <3",
        "Tomorrow will be absolutely better. It's time to sleep, {} :D",
        "Good night to you, {}",
        "Oyaa~ Let's have a nice sleep, {}",
        "Gute Nacht, have a proper rest, {}!",
        "Good night! Don't forget to have enough sleep time, {} ^^"
    ]

    SPECIAL_GOOD_MORNING = [
        "Kyaaaah! Sistine-chan overslept today, やばい やばい! Good morning, {}~",
        "Uh? What time is it now, {}? Pyaaahh! Sistine-chan is late!"
    ]

    SPECIAL_GOOD_NIGHT = [
        "Ah no, it's already this late! Good night, {} <3",
        "The game was so much fun! Are you sleeping already, {}? Good nite~"
    ]

    # Base default time, before adding random delta
    DEFAULT_MORNING_TIME = "09:00"  # UTC+9
    DEFAULT_JAPANESE_TIME = "13:00"  # UTC+9
    DEFAULT_NIGHT_TIME = "23:00"  # UTC+9

    # RSS Feed default preset
    DEFAULT_RSS_PRESET = {
        "1": {
            "title": "Manga",
            "url": "https://www.mangaupdates.com/rss.php"
        },
        "2": {
            "title": "Nyaa",
            "url": "https://www.nyaa.se/?page=rss"
        }
    }

    # Supported Languages
    TRANSLATION_LANGUAGE = {
        "vn": ["vn", "vietnam", "vietnamese", "vietnamese", "vietnamese", "ベトナム語"],
        "ja": ["ja", "jp", "japanese", "japan", "jepang", "日本語", "nihongo"],
        "en": ["en", "english", "inggris", "英語", "eigo"]
    }
    TRANSLATION_DETECT = {
        "Vietnamese": "vn",
        "Japanese": "ja",
        "English": "en"
    }
    TRANSLATION_MAP = { # Source : Target
        "en": "ja",
        "ja": "en",
        "vn": "ja",
        "": "en"  # Default
    }
    TRANSLATION_KEYWORD = ["translate", "terjemahkan"]
    TRANSLATION_FROM = ["from", "dari"]
    TRANSLATION_TO = ["to", "ke"]
