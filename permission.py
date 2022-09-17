#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : check permission helper
@File        : permission.py
@IDE         : PyCharm
@Date        : 16/9/2022 20:32
"""

from miya import bot
from miya.helper.log import log

def isAdmin(chat_id, user_id):
    log(f'Checking permission for {user_id} in {chat_id}.')
    return True if bot.get_chat_member(chat_id, user_id).status in ['creator', 'administrator'] else False
