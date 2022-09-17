#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : kick module
@File        : kick.py
@IDE         : PyCharm
@Date        : 16/9/2022 20:51
"""

from miya import bot
from miya.helper.log import log
from miya.helper.permission import isAdmin


def ban(m):
    if m.chat.type == 'private':
        log('Private chat detected.')
        return bot.reply_to(m, 'This command can only be used in groups.')

    if not isAdmin(m.chat.id, m.from_user.id):
        log('Permission denied.')
        return bot.reply_to(m, 'You dont have permission to use this command.')
    if not m.reply_to_message:
        log('No reply detected.')
        '''determine weather the user key in the user id'''
        if len(m.text.split()) == 1:
            return bot.reply_to(m, 'Please reply to a message or key in the user id.')
