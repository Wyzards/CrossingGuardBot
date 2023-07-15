import os
import time

import discord
from discord.ext import commands

ANNOUNCEMENT_COOLDOWN_IN_MS = 300000  # 5 minutes
channels = [1095529250053968013, 1095529306169540749, 1095529356123701388, 1127068846013038682]
announceChannel = 1086111140066643978
announceTimes = {}


def get_role(guild_id):
    match guild_id:
        case 698402467133784154:
            return "1095843313644470393"
        case 997400397058682940:
            return "1090720870097485914"
        case 751307973846106143:
            return "1090720744205467733"
        case 585899337012215828:
            return "1090720848278736906"
        case 432671778733555742:
            return "1095844856288522351"
        case 286476446338252800:
            return "1085631851185569963"
        case 143852930036924417:
            return "1090720722390888609"
        case 341757159798734849:
            return "1090720664408817775"
        case 313066655494438922:
            return "1085631799633399879"
        case 331596305120100368:
            return "1085631822324580423"
        case 227080337862164480:
            return "1090720689989877831"
        case 208334819652796416:
            return "1090720583563612170"
        case 212744497434460160:
            return "1090720878788100218"
        case 476939901326196738:
            return "1090735405697089556"
        case 366568834628321281:
            return "1090735351129182288"
        case 821828605340418088:
            return "1095098731369599106"
        case 768658159623340063:
            return "1095912368892026950"
        case 133012942890336256:
            return "1095912611066945577"
        case 1055661804275122238:
            return "1096694886733991936"
        case 728589320713404437:
            return "1118096782241579110"
        case _:
            return "1085631729651421345"


class Announcements(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in channels:
            await self.announce(message)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.channel.id in channels:
            await self.announce(after, is_edit=True)

    async def announce(self, message, is_edit=False):
        from_guild = message.reference.guild_id
        to_guild = discord.utils.get(self.bot.guilds, name=os.getenv('DISCORD_GUILD'))
        to_channel = to_guild.get_channel(announceChannel)
        can_ping = time.time() - announceTimes.get(
            from_guild) < ANNOUNCEMENT_COOLDOWN_IN_MS if from_guild in announceTimes else True

        if is_edit:
            template = "**Edited from an earlier message in %s**\n<@&%s>\n\n%s"
        else:
            template = "**From %s**\n" + "<@&%s>" % get_role(from_guild) + "\n\n%s "

        if can_ping:
            announceTimes[from_guild] = time.time()

        allowed = discord.AllowedMentions.all() if can_ping else discord.AllowedMentions.none()
        allowed.everyone = False
        await to_channel.send(
            content=template % (message.author.display_name, message.content),
            allowed_mentions=allowed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Announcements(bot),
        guilds=[discord.Object(id=1122969422248824932)]
    )
