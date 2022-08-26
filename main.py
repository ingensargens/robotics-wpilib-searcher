import webbrowser
import discord
import requests
from requests_html import HTMLSession
from discord.ext import commands



txt = open('pass.txt', 'r')
password = txt.read()
txt.close()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or('>'), intents=intents)

url = 'https://docs.wpilib.org/en/stable/index.html'
base = 'https://docs.wpilib.org/en/stable/docs'
close = '/index.html'
searchbarstart = 'https://docs.wpilib.org/en/stable/search.html?q='
searchbarclose = '&check_keywords=yes&area=default'

try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)


# links = response.html.absolute_links
# h = str(input("first: "))
# k = str(input('second: '))
# link = [base, h, k, close]
# oeda = ('/').join(link)




@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command()
async def search(ctx: commands.Context, target: str):
    try:
        webbrowser.open(searchbarstart + target + searchbarclose)
    except:
        await ctx.send('no work')    





bot.run(password)
