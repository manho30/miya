#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : help.py
@IDE         : PyCharm
@Date        : 16/9/2022 20:09
"""

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from miya import bot
from miya.helper.log import log


def __generate_help():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(
        InlineKeyboardButton(text='Ban', callback_data='ban'),
        InlineKeyboardButton(text='Kick', callback_data='kick'),
        InlineKeyboardButton(text='Mute', callback_data='mute'),
        InlineKeyboardButton(text='Pin', callback_data='pin'),
        InlineKeyboardButton(text='Flood', callback_data='flood'),
        InlineKeyboardButton(text='Admin', callback_data='admin'),
        InlineKeyboardButton(text='Warn', callback_data='warn'),
        InlineKeyboardButton(text='Rules', callback_data='rules'),
        InlineKeyboardButton(text='Porn', callback_data='Porn'),
        InlineKeyboardButton(text='Ads', callback_data='ads'),
        InlineKeyboardButton(text='Welcome', callback_data='welcome'),
        InlineKeyboardButton(text='reCAPTCHA', callback_data='recaptcha'),
        InlineKeyboardButton(text='Filters', callback_data='filters'),
        InlineKeyboardButton(text='Lock', callback_data='lock'),
        InlineKeyboardButton(text='Setting', callback_data='setting'),
        InlineKeyboardButton(text='Note', callback_data='note'),
        InlineKeyboardButton(text='formatting', callback_data='formatting'),
        InlineKeyboardButton(text='greeting', callback_data='greeting'),
        InlineKeyboardButton(text='report', callback_data='report'),
    )
    return markup


def help(message):
    bot.send_message(message.chat.id, 'Check out the following buttons to get more information.',
                     reply_markup=__generate_help()
                     )
    log(f'Command: {message.text} executed.')
