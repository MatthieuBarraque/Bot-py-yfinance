from discord import Embed, Color

from init_print import start_print
from bot_module import bot
from config import TOKEN, CHANEL
from stock import *

bot.remove_command('help')


@bot.event
async def on_ready():
    start_print()
    target_channel_id = CHANEL
    target_channel = bot.get_channel(target_channel_id)
    if target_channel:
        await target_channel.send('Stcok Bot est en ligne !')

        # Message de bienvenue du bot
        embed = Embed(title="Salut C'est moi StockBot !", description="Je suis la pour fournir des info sur stock market Voici quelques commandes utiles", color=Color.red())
        embed.add_field(name="🔍 Aide", value="Pour obtenir de l'aide, tapez `/commands`", inline=False)
        embed.add_field(name="📜 Liste des Commandes", value="Pour voir toutes les commandes, tapez `/commands`", inline=False)
        embed.add_field(name="📊 Stock", value="Pour voir les commandes associez au cac40, tapez `/cac40`", inline=False)
        embed.add_field(name="📈 Graph", value="Pour voir les graphiques associez au cac40, tapez `/graph`", inline=False)
        embed.add_field(name="⌚ Scrap", value="Pour voir les informations associez au action du cac40, tapez `/scrap`", inline=False)
        embed.add_field(name="💲 add", value="Permet a l'utilisateur des placement boursier avec le nombre d'action acheter(arg1) ainsi que la date d'achat(arg2) et le prix d'achat(arg3)", inline=False)

        await target_channel.send(embed=embed)
    else:
        print(f"Could not find channel with ID {target_channel_id}")


@bot.command(name='cac40')
async def cac40(ctx):
    try:
        target_channel_id = CHANEL
        target_channel = bot.get_channel(target_channel_id)
        if target_channel:
            await target_channel.send('**Voici le cours actuelle du cac40 !**')
            embed = Embed(title="CAC40", description="Voici le cours actuelle du cac40", color=Color.red())
            embed.add_field(name="📈 orange", value=stock_orange())
            embed.add_field(name="📈 airbus", value=stock_airbus())
            embed.add_field(name="📈 peugeot", value=stock_peugeot())
            embed.add_field(name="📈 renault", value=stock_renault())
            embed.add_field(name="📈 societe_generale", value=stock_societe_generale())
            embed.add_field(name="📈 bnp_paribas", value=stock_bnp_paribas())
            embed.add_field(name="📈 credit_agricole", value=stock_credit_agricole())
            embed.add_field(name="📈 engie", value=stock_engie())
            embed.add_field(name="📈 total", value=stock_total())
            embed.add_field(name="📈 sanofi", value=stock_sanofi())
            embed.add_field(name="📈 vinci", value=stock_vinci())
            embed.add_field(name="📈 bouygues", value=stock_bouygues())
            embed.add_field(name="📈 atos", value=stock_atos())
            embed.add_field(name="📈 saint_gobain", value=stock_saint_gobain())
            embed.add_field(name="📈 schneider_electric", value=stock_schneider_electric())
            await target_channel.send(embed=embed)
        else:
            print(f"Could not find channel with ID {target_channel_id}")
    except:
        print("error")


@bot.command(name='commands')
async def commands(ctx):
    target_channel_id = CHANEL
    target_channel = bot.get_channel(target_channel_id)
    if target_channel:
        embed = Embed(title="Salut C'est moi StockBot !", description="Je suis la pour fournir des info sur stock market Voici quelques commandes utiles", color=Color.red())
        embed.add_field(name="🔍 Aide", value="Pour obtenir de l'aide, tapez `/help`", inline=False)
        embed.add_field(name="📜 Liste des Commandes", value="Pour voir toutes les commandes, tapez `/commands`", inline=False)
        embed.add_field(name="📊 Stock", value="Pour voir les commandes associez au cac40, tapez `/cac40`", inline=False)
        embed.add_field(name="📈 Graph", value="Pour voir les graphiques associez au cac40, tapez `/graph`", inline=False)
        embed.add_field(name="⌚ Scrap", value="Pour voir les informations associez au action du cac40, tapez `/scrap`", inline=False)
        embed.add_field(name="💲 add", value="Permet a l'utilisateur des placement boursier avec le nombre d'action acheter(arg1) ainsi que la date d'achat(arg2) et le prix d'achat(arg3)", inline=False)
        await target_channel.send(embed=embed)
    else:
        print(f"Could not find channel with ID {target_channel_id}")
        await ctx.send("error, try again")

bot.run(TOKEN)
