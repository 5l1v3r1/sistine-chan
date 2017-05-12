=================
Features Overview
=================

Features List
-------------

Currently, Maid-chan has the following features:

- :ref:`Image Processing with Primitive`: For every uploaded images to Maid-chan, Maid-chan will convert it to a geometric primitive GIF via `Primitive`_.

.. image:: https://freedomofkeima.com/images/maid-chan/primitive_scr.jpg
    :alt: maid-primitive-messenger
    :align: center
    :height: 300pt

.. image:: https://freedomofkeima.com/images/maid-chan/primitive.gif
    :alt: maid-primitive-gif
    :align: center
    :height: 300pt

- :ref:`Chatbot with ChatterBot`: For every text messages outside the provided available commands, Maid-chan will send a text response via `ChatterBot`_ and `langdetect`_ (to detect the language validity).

.. image:: https://freedomofkeima.com/images/maid-chan/chatterbot.png
    :alt: maid-chatbot-messenger
    :align: center
    :width: 300pt

- :ref:`Daily Offerings`: If user decides to subscribe for offerings feature, Maid-chan will send a good morning and a good night message with one additional image from `offerings/stock` directory.

.. image:: https://freedomofkeima.com/images/maid-chan/daily_morning_offerings.png
    :alt: sischan-offerings-morning
    :align: center
    :width: 300pt

.. image:: https://freedomofkeima.com/images/maid-chan/daily_night_offerings.png
    :alt: sischan-offerings-night
    :align: center
    :width: 300pt

- :ref:`Daily Japanese Lesson`: If user decides to subscribe for Japanese lesson feature, Maid-chan will send a Kanji (N1-N4, by choice) and a Vocabulary for each day.

.. image:: https://freedomofkeima.com/images/maid-chan/daily_japanese.png
    :alt: sischan-japanese-messenger
    :align: center
    :width: 300pt

- :ref:`RSS Feed Notifier`: The idea is similar to `rss-twilio-bot`_, where all subscribed RSS feeds are aggregated to Facebook Messenger via Maid-chan scheduler.

.. image:: https://freedomofkeima.com/images/maid-chan/rss_notification.png
    :alt: sischan-rss-preset-manga
    :align: center
    :width: 300pt

- :ref:`Translate text via Google Translate`: For every messages which have "translate" and its language derivatives in it, Maid-chan will use Google-translate to translate the given messages (with several default configuration).

.. image:: https://freedomofkeima.com/images/maid-chan/translate_normal.png
    :alt: sischan-translate-text
    :align: center
    :width: 300pt

Currently, Maid-chan only supports `Asia/Tokyo` timezone (**UTC +9**).


Available Commands
------------------

All commands receive 2 parameters: `redis_client` as `RedisDriver` object and `recipient_id` as user's identifier.

.. autofunction:: sischan.command.process_help

**help** is used to get the list of all available commands from Maid-chan.

.. autofunction:: sischan.command.process_subscribe_offerings

**subscribe offerings** is used to subscribe daily offerings.

.. autofunction:: sischan.command.process_unsubscribe_offerings

**unsubscribe offerings** is used to unsubscribe daily offerings.

.. autofunction:: sischan.command.process_update_offerings

**update offerings** is used to update information (wake up & sleeping time) for daily offerings.

.. autofunction:: sischan.command.process_subscribe_japanese

**subscribe japanese** is used to subscribe daily Japanese lesson.

.. autofunction:: sischan.command.process_unsubscribe_japanese

**unsubscribe japanese** is used to unsubscribe daily Japanese lesson.

.. autofunction:: sischan.command.process_update_japanese

**update japanese** is used to update information (Kanji N1-N4 level) for daily Japanese lesson.

.. autofunction:: sischan.command.process_update_name

**update name** is used to change user's nickname. By default, Maid-chan will use `onii-chan` to call users.

.. autofunction:: sischan.command.process_subscribe_rss

**subscribe rss** is used to subscribe a new RSS Feed with its pattern and let Maid-chan sends a notification if there is an update.

.. autofunction:: sischan.command.process_unsubscribe_rss

**unsubscribe rss** is used to remove one of the registered RSS Feed.

.. autofunction:: sischan.command.process_show_profile

**show profile** is used to show user's nickname, subscription status, and preference.

.. _Primitive: https://github.com/fogleman/primitive
.. _ChatterBot: https://github.com/gunthercox/ChatterBot
.. _langdetect: https://github.com/Mimino666/langdetect
.. _rss-twilio-bot: https://github.com/freedomofkeima/rss-twilio-bot
