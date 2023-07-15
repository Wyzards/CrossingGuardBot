from typing import List

import discord
from discord.ext import commands


def load_servers() -> List:
    return {}


class ServerManager(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.servers = load_servers()


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ServerManager(bot),
        guilds=[discord.Object(id=1085622890344480879)]
    )
