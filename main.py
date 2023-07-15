# main.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from keep_alive import keep_alive

load_dotenv()
keep_alive()


class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='$',
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        await self.load_extension(f"cogs.announcements")
        await bot.tree.sync(guild=discord.Object(id=1085622890344480879))

    async def on_ready(self):
        guild = discord.utils.get(bot.guilds, name=os.getenv('DISCORD_GUILD'))

        print(f'{self.user} is connected to the following guild: '
              f'{guild.name}(id: {guild.id})')


bot = MyBot()
bot.run(os.getenv('DISCORD_TOKEN'))
