#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : utils.py
@IDE         : PyCharm
@Date        : 16/9/2022 19:51
"""

from miya import bot
from miya.handler.text import text_handler
from miya.helper.log import log


def listener(message):
    for m in message:
        if m.content_type == 'text':
            text_handler(m)


bot.set_update_listener(listener)
log('Bot started')
bot.infinity_polling()
