from include import *
import yfinance as yf
import matplotlib.pyplot as plt
import io
import discord
import numpy as np
import datetime
from config_stock import stocks


@bot.command(name='graph')
async def stock(ctx, arg):
  try:
    if arg.lower() in stocks:
      stock_id = stocks[arg.lower()]
      stock_info = yf.Ticker(stock_id)
      stock_value = stock_info.info['currentPrice']

      # Récupérer les informations historiques de l'action
      hist = stock_info.history(period="max")

      # Calculer les moyennes mobiles
      hist['MA20'] = hist['Close'].rolling(window=20).mean() # 20 jours ouvrés, cela correspond à un mois
      hist['MA50'] = hist['Close'].rolling(window=50).mean() # 50 jours ouvrés, cela correspond à 2 mois et demi j'utilise

      # Créer un graphique de l'évolution du cours de l'action
      fig, ax = plt.subplots()

      # Ajouter les moyennes mobiles
      ax.plot(hist['MA20'], label='MA20')
      ax.plot(hist['MA50'], label='MA50')

      # Ajouter les barres de couleur pour les mouvements haussiers et baissiers
      ax.bar(hist.index, hist['Close'] - hist['Open'], bottom=hist['Open'], color=np.where(hist['Close'] - hist['Open'] > 0, 'g', 'r'))

      ax.legend()
      plt.title(f'Evolution du cours de {arg.capitalize()}')
      plt.xlabel('Date')
      plt.ylabel('Cours de clôture')

      # Sauvegarder le graphique dans un BytesIO object
      buf = io.BytesIO()
      plt.savefig(buf, format='png')
      buf.seek(0)

      # Envoyer le graphique sur Discord
      await ctx.send(file=discord.File(buf, 'stock_graph.png'))

      embed = discord.Embed(title=f'Informations sur {arg.capitalize()}', color=0x3498db)
      
      # Utilisation du formatage Markdown pour le style
      embed.add_field(name='**Cours actuel**', value=f'**{stock_value:.2f} €**', inline=True)
      embed.add_field(name='**Cours de clôture**', value=f'*{hist["Close"][-1]:.2f} €*', inline=True)
      
      # Utilisation des emojis pour une meilleure visibilité
      embed.add_field(name='📈 Moyenne mobile sur 20 jours', value=f'{hist["MA20"][-1]:.2f} €', inline=True)
      embed.add_field(name='📉 Moyenne mobile sur 50 jours', value=f'{hist["MA50"][-1]:.2f} €', inline=True)
      embed.add_field(name='🔝 Cours le plus haut', value=f'{hist["High"].max():.2f} €', inline=True)
      embed.add_field(name='🔻 Cours le plus bas', value=f'{hist["Low"].min():.2f} €', inline=True)
      embed.add_field(name='🔄 Volume moyen', value=f'{hist["Volume"].mean():.0f}', inline=True)  # Pas de symbole € pour le volume
      
      # Footer et Timestamp
      embed.set_footer(text="Dernière mise à jour")
      embed.timestamp = datetime.datetime.utcnow()  # Ajoute le timestamp actuel
      
      await ctx.send(embed=embed)
      

      print('User sent showme at :', time.strftime("%H:%M:%S", time.localtime()), 'date :', time.strftime("%d/%m/%Y", time.localtime()))

      # Clear the current figure
      plt.clf()
    else:
      await ctx.send("Cette action n'est pas prise en charge.")
  except Exception as e:
    await ctx.send("erreur de connection")
    print('erreur de connection at :', time.strftime("%H:%M:%S", time.localtime()), 'date :', time.strftime("%d/%m/%Y", time.localtime()))
    print(f'Exception: {e}')
