#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : ban module
@File        : ban.py
@IDE         : PyCharm
@Date        : 16/9/2022 20:31
"""

from miya import bot
from miya.helper.log import log
from miya.helper.permission import isAdmin


def ban(m, user_id=None):
    destination_id = 0
    if user_id:
        log(f'User id detected: {user_id}')
        return true, bot.kick_chat_member(m.chat.id, user_id)

    log(f'Handling ban command({m.text})from {m.from_user.id} in {m.chat.id}.')
    if m.chat.type == 'private':
        log('Private chat detected.')
        return bot.reply_to(m, 'This command can only be used in groups.')

    if not isAdmin(m.chat.id, m.from_user.id):
        log('Permission denied.')
        return bot.reply_to(m, 'You dont have permission to use this command.')

    try:
        if len(m.reply_to_message) > 1:
            log('Reply detected.')
    except:
        log('No reply detected.')
        '''determine weather the user key in the user id'''
        if len(m.text.split(' ')) == 1:
            log('Bad command.')
            return bot.reply_to(m, 'Please reply to a message or key in the user id.')

        destination_id = m.text.split(' ')[1]


