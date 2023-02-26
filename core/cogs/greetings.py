import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member.mention}!")

    @commands.command(pass_context=True)
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send(f"Hey {member.mention}!")

    pass


async def setup(client):
    await client.add_cog(Greetings(client))
