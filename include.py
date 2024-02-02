#!/usr/bin/env python

"""
include.py:
    This file contains all the modules used in the bot
"""

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord import app_commands
import time
import yfinance as yf
import requests
import os
import matplotlib.pyplot as plt
import discord
import io
import numpy as np
import datetime


from discord import Embed
from intents import intents
from config import TOKEN, CHANEL, API
from intents import intents
from src.init_print import start_print
from bot_module import bot
from src.stock import *
from src.command_bot import orange
from src.graph import *
from src.scrap import *
from config_stock import stocks
from src.add import *
from config_stock import *
from src.news import *
