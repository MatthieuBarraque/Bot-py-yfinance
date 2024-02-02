#!/usr/bin/env python

"""
command_bot.py
    
"""

from time import localtime, strftime, localtime

from discord import Embed, Color

from bot_module import bot
from src.stock import *


# affiche le cours de orange
@bot.command(name='orange')
async def orange(ctx):
    try:
        stock_value = stock_orange()
        embed = Embed(title="Action Orange", description=f"La Valeurs Actuelle de Orange est de: **{stock_value} $**", color=Color.orange())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Orange_logo.svg/2048px-Orange_logo.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='airbus')
async def airbus(ctx):
    try:
        stock_value = stock_airbus()
        embed = Embed(title="Action Airbus", description=f"La Valeurs Actuelle de Airbus est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Airbus_Logo_2017.svg/2560px-Airbus_Logo_2017.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='peugeot')
async def peugeot(ctx):
    try:
        stock_value = stock_peugeot()
        embed = Embed(title="Action Peugeot", description=f"La Valeurs Actuelle de Peugeot est de: **{stock_value} $**", color=Color.grey())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Peugeot_Logo.svg/1200px-Peugeot_Logo.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='renault')
async def renault(ctx):
    try:
        stock_value = stock_renault()
        embed = Embed(title="Action Renault", description=f"La Valeurs Actuelle de Renault est de: **{stock_value} $**", color=Color.grey())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Renault_2009_logo.svg/2048px-Renault_2009_logo.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='societe_generale')
async def societe_generale(ctx):
    try:
        stock_value = stock_societe_generale()
        embed = Embed(title="Action Societe Generale", description=f"La Valeurs Actuelle de Societe Generale est de: **{stock_value} $**", color=Color.red())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Soci%C3%A9t%C3%A9_G%C3%A9n%C3%A9rale.svg/1280px-Soci%C3%A9t%C3%A9_G%C3%A9n%C3%A9rale.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='bnp_paribas')
async def bnp_paribas(ctx):
    try:
        stock_value = stock_bnp_paribas()
        embed = Embed(title="Action BNP Paribas", description=f"La Valeurs Actuelle de BNP Paribas est de: **{stock_value} $**", color=Color.green())
        embed.set_thumbnail(url="https://1000logos.net/wp-content/uploads/2020/06/BNP-Paribas-Logo.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='credit_agricole')
async def credit_agricole(ctx):
    try:
        stock_value = stock_credit_agricole()
        embed = Embed(title="Action Credit Agricole", description=f"La Valeurs Actuelle de Credit Agricole est de: **{stock_value} $**", color=Color.green())
        embed.set_thumbnail(url="https://1000logos.net/wp-content/uploads/2021/05/Credit-Agricole-logo.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='engie')
async def engie(ctx):
    try:
        stock_value = stock_engie()
        embed = Embed(title="Action Engie", description=f"La Valeurs Actuelle de Engie est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://www.power-eng.com/wp-content/uploads/2019/04/14962-file.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='total')
async def total(ctx):
    try:
        stock_value = stock_total()
        embed = Embed(title="Action Total", description=f"La Valeurs Actuelle de Total est de: **{stock_value} $**", color=Color.orange())
        embed.set_thumbnail(url="https://images.caradisiac.com/logos/6/5/5/7/266557/S8-total-change-de-nom-pour-se-refaire-une-identite-plus-verte-190209.jpg")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='sanofi')
async def sanofi(ctx):
    try:
        stock_value = stock_sanofi()
        embed = Embed(title="Action Sanofi", description=f"La Valeurs Actuelle de Sanofi est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Sanofi_logo.svg/2560px-Sanofi_logo.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='vinci')
async def vinci(ctx):
    try:
        stock_value = stock_vinci()
        embed = Embed(title="Action Vinci", description=f"La Valeurs Actuelle de Vinci est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://1000logos.net/wp-content/uploads/2021/09/Vinci-Logo.jpg")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='bouygues')
async def bouygues(ctx):
    try:
        stock_value = stock_bouygues()
        embed = Embed(title="Action Bouygues", description=f"La Valeurs Actuelle de Bouygues est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Bouygues_Telecom_%28alt_logo%29.svg/1200px-Bouygues_Telecom_%28alt_logo%29.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='atos')
async def atos(ctx):
    try:
        stock_value = stock_atos()
        embed = Embed(title="Action Atos", description=f"La Valeurs Actuelle de Atos est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://atos.net/wp-content/uploads/2022/02/atos-globe-blue-high-res.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='saint_gobain')
async def saint_gobain(ctx):
    try:
        stock_value = stock_saint_gobain()
        embed = Embed(title="Action Saint Gobain", description=f"La Valeurs Actuelle de Saint Gobain est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Saint-Gobain_Logo.svg/1200px-Saint-Gobain_Logo.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='schneider_electric')
async def schneider_electric(ctx):
    try:
        stock_value = stock_schneider_electric()
        embed = Embed(title="Action Schneider Electric", description=f"La Valeurs Actuelle de Schneider Electric est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Schneider_Electric_logo.svg/1200px-Schneider_Electric_logo.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))


@bot.command(name='tesla')
async def tesla(ctx):
    try:
        stock_value = stock_tesla()
        embed = Embed(title="Action Tesla", description=f"La Valeurs Actuelle de Tesla est de: **{stock_value} $**", color=Color.blue())
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Tesla_Motors.svg/1200px-Tesla_Motors.svg.png")
        await ctx.send(embed=embed)
        print('User sent showme at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
    except:
        await ctx.send("erreur de connection")
        print('erreur de connection at :', strftime("%H:%M:%S", localtime()), 'date :', strftime("%d/%m/%Y", localtime()))
