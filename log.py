#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : logging
@File        : log.py
@IDE         : PyCharm
@Date        : 16/9/2022 19:48
"""
import os
import logging
import datetime


def log(msg):
    logging.basicConfig(filename='./miya.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %('
                                                                         'message)s')
    logging.info(msg)
    print(msg)

def push_log():
    '''this is a simple function to push the log to the GitHub repo'''
    os.system('git init')
    os.system('git add .')
    os.system(f'git commit -m "[BOT] Update log at {datetime.datetime.now()}"')
    os.system('git remote add origin https://github.com/manho30/miya.git')
    os.system('git branch -M main')
    os.system('git push origin main')
    print('Log pushed')

if __name__ == '__main__':
    log('test')
    push_log()