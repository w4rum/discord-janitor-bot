#!/usr/bin/env python3

import config
import discord
from discord.ext import commands
from typing import Optional

bot = commands.Bot(command_prefix=config.BOT_CMD_PREFIX)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(aliases = ["wipe", "clean", "cleanse", "purify", "purge"])
async def nuke(ctx, amount: Optional[int]):
    await ctx.channel.purge(limit=amount)


if __name__ == "__main__":
    bot.run(config.BOT_TOKEN)
