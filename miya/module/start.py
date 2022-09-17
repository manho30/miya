#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : start module
@File        : start.py
@IDE         : PyCharm
@Date        : 16/9/2022 20:04
"""

from miya import bot


def start(message):
    bot.send_message(message.chat.id, 'Hello, I am Miya, a bot for Telegram. I can help you to manage your group. '
                                      'If you need help, please type /help')
    print(message)