import discord
import time
from setup import TOKEN
from discord.ext import commands
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is working')

@client.command(pass_context=True)
async def Song(ctx):
    await ctx.send('Hello there')

@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')
    await client.process_commands(message)
client.run(TOKEN)

def main():
    print("1")

if __name__ == "__main__":
    main()