#!/usr/bin/env python

"""
add.py
    
"""

from datetime import datetime

from include import bot, yf, discord
from config_stock import stocks


@bot.command(name='add', help='Add two numbers')
async def add(ctx, arg1=None, arg2=None, arg3=None):
    try:
        if arg1 is None or arg2 is None or arg3 is None:
            await ctx.send("Vous n'avez pas rentrer les bonnes informations")
            await ctx.send("La commande est : /add <action> <nombre d'action> <date d'achat>")
            print("L'utilisateur n'a pas rentrer les bonnes informations")
            print("Le user est : " + str(ctx.author) + " et le serveur est : " + str(ctx.guild))
            return
        if arg1.lower() not in stocks:
            await ctx.send("L'action rentrez en parametre n'est pas enregistrez dans notre BDD")
            await ctx.send("La commande est : /add <action> <nombre d'action> <date d'achat>")
            print("L'utilisateur a rentrez une action qui n'est pas dans notre BDD")
            print("Le user est : " + str(ctx.author) + " et le serveur est : " + str(ctx.guild))
            return

        if arg1.lower() in stocks:
            stock_id = stocks[arg1.lower()]
            stock_info = yf.Ticker(stock_id)
            stock_value = stock_info.info['currentPrice']
            # Récupérer les informations historiques de l'action
            hist = stock_info.history(period="max")
            # Calculer les moyennes mobiles
            hist['MA20'] = hist['Close'].rolling(window=20).mean()

            # Convertir arg2 en nombre d'actions
            num_shares = int(arg2)

            # Convertir arg3 en date
            purchase_date = datetime.strptime(arg3, '%d/%m/%Y').date()

            # Obtenir le prix de l'action à la date d'achat
            purchase_price = hist.loc[purchase_date.strftime('%Y-%m-%d')]['Close']

            # Calculer le coût total de l'achat
            total_cost = purchase_price * num_shares

            # Calculer le bénéfice ou la perte
            profit_loss = (stock_value * num_shares) - total_cost

            # Déterminer si le profit ou la perte est positif ou négatif
            if profit_loss > 0:
                profit_loss_str = f'+{profit_loss:.2f} €'
            else:
                profit_loss_str = f'-{abs(profit_loss):.2f} €'

            # Créer un embed avec les informations
            embed = discord.Embed(title=f'Informations sur {arg1.capitalize()}', color=discord.Color.green())
            embed.add_field(name='Cours actuel', value=f'{stock_value:.2f} €', inline=False)
            embed.add_field(name='Prix d\'achat', value=f'{purchase_price:.2f} €', inline=False)
            embed.add_field(name='Coût total de l\'achat', value=f'{total_cost:.2f} €', inline=False)
            embed.add_field(name='Bénéfice ou perte', value=profit_loss_str, inline=False)

            # Envoyer l'embed
            await ctx.send(embed=embed)
            print("L'utilsateur a bien ajouter un placement boursier !")
            print("Le user est : " + str(ctx.author) + " et le serveur est : " + str(ctx.guild))
        else:
            await ctx.send("L'action rentrez en parametre n'est pas enregistrez dans notre BDD ou les informations sont peut etre éroner")
            await ctx.send("La commande est : /add <action> <nombre d'action> <date d'achat>")
            print("L'utilisateur a rentrez une action qui n'est pas dans notre BDD")
            print("Le user est : " + str(ctx.author) + " et le serveur est : " + str(ctx.guild))

    except Exception as e:
        await ctx.send("Une erreur est survenue vérifier que vous avez bien entrer les bonnes informations")
        await ctx.send("Pour plus d'information taper /commands")
        await ctx.send("Sinom n'oubliez pas de vérifier que la dates est bien au format : jj/mm/aaaa et assuez vous que la date n'est pas un weekend ou un jour férié")
        await ctx.send("L'action rentrez en parametre n'est pas enregistrez dans notre BDD")
        await ctx.send("La commande est : /add <action> <nombre d'action> <date d'achat>")
        print("error")
        print(e)
