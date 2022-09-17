#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : command handler
@File        : command.py
@IDE         : PyCharm
@Date        : 16/9/2022 20:01
"""

from miya.module.start import start
from miya.module.help import help
from miya.module.ban import ban


def command_handler(message):
    if message.text == '/start':
        return start(message)
    elif message.text == '/help':
        return help(message)
    elif '/ban' in message.text:
        return ban(message)
