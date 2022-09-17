#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : text handler
@File        : text.py
@IDE         : PyCharm
@Date        : 16/9/2022 19:58
"""

from miya.helper.log import log
from miya.handler.command import command_handler
def text_handler(message):
    # determine weather the message is a command
    if message.text.startswith('/') or message.text.startswith('!'):
        log(f'Command: {message.text} received.')
        command_handler(message)
        log(f'Command: {message.text} handled.')