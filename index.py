import discord
from discord.ext import commands
from discord.utils import get
import datetime
from urllib import parse, request
import re

bot=commands.Bot(command_prefix='!', description="Esto es un bot de ayuda")

#Comandos
@bot.command()
async def suma(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)  

@bot.command()
async def div(ctx, num1: int, num2: int):
    await ctx.send(num1 / num2)       

@bot.command()
async def mult(ctx, num1: int, num2: int):
    await ctx.send(num1 * num2) 

@bot.command()
async def resta(ctx, num1: int, num2: int):
    await ctx.send(num1 - num2)     

@bot.command()
async def hola(ctx):
    await ctx.send("Hola me llamo bot-test y te puedo ayudar hacer varias cosas :smiley:")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
    timestamp=datetime.datetime.utcnow(), color = discord.Color.blue())
    embed.add_field(name="Servidor Creado el", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Region del Servidor", value=f"{ctx.guild.region}")
    embed.add_field(name="Id del Servidor", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://assets.stickpng.com/images/5848152fcef1014c0b5e4967.png")
    await ctx.send(embed=embed)


@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    await ctx.send('https://www.youtube.com/watch?v='+ search_results[0])

@bot.command()
async def comandos(ctx):
    embed = discord.Embed(title="Comandos", 
    description="Estos son los comandos que puedes utlizar hasta ahora", 
    color=discord.Color.red())
    embed.add_field(name="!suma", value="Te ayuda a sumar dos numeros ejemplo:(!suma 10 10).")
    embed.add_field(name="!resta", value="Te ayuda a restar dos numeros ejemplo:(!resta 10 10).")
    embed.add_field(name="!mult", value="Te ayuda a multiplicar dos numeros ejemplo:(!mult 10 10).")
    embed.add_field(name="!div", value="Te ayuda a dividir dos numeros ejemplo:(!div 10 10).")
    embed.add_field(name="!info", value="Informacion del servidor ejemplo:(!info).")
    embed.add_field(name="!hola", value="Saludo del bot ejemplo:(!hola).")
    embed.add_field(name="!youtube", value="Te ayuda a hacer busquedas en youtube ejemplo:(!youtube + busqueda).")
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/888/888879.png")
    await ctx.send (embed = embed)

#Evento
@bot.event
async def on_ready():
    print('Mi bot esta listo')

#bot.run('Aqui va tu TOKEN')