from include import *
from datetime import datetime

stocks = {
  "airbus": "AIR.PA",
  "amundi": "AMUN.PA",
  "alstom": "ALO.PA",
  "atos": "ATO.PA",
  "bouygues": "EN.PA",
  "bnp_paribas": "BNP.PA",
  "capgemini": "CAP.PA",
  "credit_agricole": "ACA.PA",
  "dassault_systemes": "DSY.PA",
  "essilorluxottica": "EL.PA",
  "kering": "KER.PA",
  "l'oreal": "OR.PA",
  "orange": "ORAN",
  "renault": "RNO.PA",
  "societe_generale": "GLE.PA",
  "sanofi": "SAN.PA",
  "schneider_electric": "SU.PA",
  "saint_gobain": "SGO.PA",
  "totalenergies": "TTE.PA",
  "vinci": "DG.PA",
  "vivendi": "VIV.PA",
}

@bot.command()
async def scrap(ctx, arg):
    try:
        if arg.lower() in stocks:
            stock_id = stocks[arg.lower()]
            stock_info = yf.Ticker(stock_id)

            for _ in range(60):  # Répéter 60 fois
                # Récupérer les informations
                stock_value = stock_info.info['currentPrice']
                closing_time = stock_info.info['regularMarketPreviousClose']
                daily_high = stock_info.info['dayHigh']
                daily_low = stock_info.info['dayLow']

                embed = discord.Embed(title=f'Informations sur {arg.capitalize()}', color=0x2ecc71 if stock_value >= daily_low else 0xe74c3c)

                # Utilisation d'emojis pour rendre l'affichage plus visuel
                embed.add_field(name='Cours actuel 📊', value=f'**{stock_value:.2f} €**')

                # Formatage de l'heure de clôture
                closing_time_formatted = datetime.fromtimestamp(closing_time).strftime('%H:%M')

                embed.add_field(name='Heure de clôture ⏰', value=closing_time_formatted)

                embed.add_field(name='Plus haut de la journée 📈', value=f'**{daily_high:.2f} €**')
                embed.add_field(name='Plus bas de la journée 📉', value=f'**{daily_low:.2f} €**')

                # Ajout d'un footer avec la date et l'heure actuelles
                embed.set_footer(text=f'Mis à jour le {datetime.now().strftime("%d/%m/%Y à %H:%M")}')

                # Envoyer l'embed
                await ctx.send(embed=embed)

                # Attendre 5 secondes avant de répéter
                await asyncio.sleep(5)

                print(f"L'utilisateur a demandé les informations sur", arg.capitalize() + '.')
                print("l'utilisateur est sur le channel", ctx.channel.name + '.')
                      
                print(f'[{datetime.now().strftime("%H:%M:%S")}] {arg.capitalize()} : {stock_value:.2f} €')

    except Exception as e:
        print("error")
        print(e)