#!/usr/bin/env python

"""
scrap.py:
    scrap function give informations about a stock
"""

from datetime import datetime
import time

from asyncio import sleep
from discord import Embed

from include import bot, stocks, yf


@bot.command(name="scrap")
async def scrap(ctx, arg):
    if arg is None:
        await ctx.send("Vous n'avez pas rentrer les bonnes informations")
        await ctx.send("La commande est : /scrap <action>")

    if arg.lower() not in stocks:
        await ctx.send("L'action rentrez en parametre n'est pas enregistrez dans notre BDD")
        await ctx.send("La commande est : /scrap <action>")
        print("L'utilisateur a rentrez une action qui n'est pas dans notre BDD")
        print("Le user est : " + str(ctx.author) + " et le serveur est : " + str(ctx.guild))
        return

    if arg.lower() in stocks:
        stock_id = stocks[arg.lower()]

        for _ in range(60):  # Répéter 60 fois
            try:
                # Créer un nouvel objet stock_info à chaque itération
                stock_info = yf.Ticker(stock_id)

                # Récupérer les informations
                stock_value = stock_info.info['currentPrice']
                closing_time = stock_info.info['regularMarketPreviousClose']
                daily_high = stock_info.info['dayHigh']
                daily_low = stock_info.info['dayLow']

                embed = Embed(title=f'Informations sur {arg.capitalize()}', color=0x2ecc71 if stock_value >= daily_low else 0xe74c3c)

                # Utilisation d'emojis pour rendre l'affichage plus visuel
                embed.add_field(name='Cours actuel 📊', value=f'**{stock_value:.2f} €**')

                # Formatage de l'heure de clôture
                closing_time_formatted = time.ctime(closing_time)

                embed.add_field(name='Heure de clôture ⏰', value=closing_time_formatted)

                embed.add_field(name='Plus haut de la journée 📈', value=f'**{daily_high:.2f} €**')
                embed.add_field(name='Plus bas de la journée 📉', value=f'**{daily_low:.2f} €**')
                embed.add_field(name='Volume Actuelle achat 💲', value=f'**{stock_info.info["regularMarketVolume"]:.0f}**')
                embed.add_field(name='Volume Actuelle vente 💲', value=f'**{stock_info.info["regularMarketVolume"]:.0f}**')

                # Ajout d'un footer avec la date et l'heure actuelles
                embed.set_footer(text=f'Mis à jour le {datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")}')

                # Envoyer l'embed
                await ctx.send(embed=embed)

                # Attendre 5 secondes avant de répéter
                await sleep(5)

                print("L'utilisateur a demandé les informations sur", arg.capitalize() + '.')
                print("l'utilisateur est sur le channel", ctx.channel.name + '.')

                print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {arg.capitalize()} : {stock_value:.2f} €')

            except Exception as e:
                print("error")
                print(e)
