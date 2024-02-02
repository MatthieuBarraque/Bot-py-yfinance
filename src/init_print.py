#!/usr/bin/env python

"""
init_print.py
    start_print print some information at the launch of the bot
"""

import time

from bot_module import bot


def start_print():
    print('Stock Bot est en ligne.')
    print('avec le nom :', bot.user.name)
    print('avec l id :', bot.user.id)
    print('------------------')
    print('Connecté sur :' + str(len(bot.guilds)) + ' serveurs')
    print('Connecté avec :' + str(len(set(bot.get_all_members()))) + ' membres')
    print('------------------')
    print('heure :', time.strftime("%H:%M:%S", time.localtime()))
