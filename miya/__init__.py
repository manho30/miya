#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : init the bot
@File        : __init__.py
@IDE         : PyCharm
@Date        : 16/9/2022 18:59
"""
import telebot

from miya.config import TOKEN
from miya.helper.log import log

bot = telebot.TeleBot(TOKEN)
log('Bot intialized')