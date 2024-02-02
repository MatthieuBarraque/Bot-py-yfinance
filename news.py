from include import *
from newsapi import NewsApiClient
import requests
from datetime import datetime, timedelta
import json

@bot.command(name="news")
async def news(ctx, arg1=None):

    if arg1 is None:
        await ctx.send("Vous n'avez pas rentrer les bonnes informations")
        await ctx.send("La commande est : /news <action>")
        print("L'utilisateur n'a pas rentrer les bonnes informations")
        print("Le user est : " + str(ctx.author) + " et le serveur est : " + str(ctx.guild))
        return

    query = "".join(arg1)
    yesterday = datetime.now() - timedelta(days=1)
    date_from = yesterday.strftime('%Y-%m-%d')

    languages = ['fr', 'en']

    articles_with_titles = {}

    for language in languages:
        url = f'https://newsapi.org/v2/everything?q={query}&from={date_from}&language={language}&sortBy=publishedAt&apiKey={API}'

        response = requests.get(url)
        articles = response.json().get('articles', [])

        for article in articles:
            title = article['title']
            articles_with_titles[title] = {
                'source': article['source']['name'],
                'author': article['author'],
                'description': article['description'],
                'url': article['url'],
                'publishedAt': article['publishedAt'],
                'content': article['content']
            }

    sorted_articles = sorted(articles_with_titles.items(), key=lambda item: item[1]['publishedAt'], reverse=True)[:10]

    for i, (title, article_info) in enumerate(sorted_articles, 1):
        embed = discord.Embed(title=f"{i}. {title}", description=article_info['description'], url=article_info['url'], color=0x3498db)
        embed.set_footer(text=f"Source: {article_info['source']}, Published at: {article_info['publishedAt']}")
        await ctx.send(embed=embed)
        print("L'utilisateur" + str(ctx.author) + " a demandé les actualités sur " + query + '.')