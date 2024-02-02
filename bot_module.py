#!/usr/bin/env python

"""
bot_module.py:
    This file contains the bot object
"""

from discord.ext.commands import Bot
from intents import intents

bot = Bot(command_prefix='/', intents=intents)
