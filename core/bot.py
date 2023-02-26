import os
import asyncio
import discord
from discord.ext import commands
from rich.console import Console

from exceptions import TokenNotFound

TOKEN = os.environ.get("TOKEN", None)
if not TOKEN:
    raise TokenNotFound("Token not found")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    bot.console.log(f"Logged in as {bot.user.name} {bot.user.id}")
    return


@bot.event
async def on_error(ctx, error, *args):
    bot.console.log(f"[red]Error:[/] {error}")
    await ctx.send(f"Error: {error}")


async def main(bot):
    async with bot:
        await bot.load_extension("cogs.greetings")
        await bot.start(TOKEN)


bot.console = Console()
asyncio.run(main(bot))
