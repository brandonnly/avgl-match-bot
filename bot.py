import datetime
from datetime import timezone

import discord
from discord.ext import commands

from settings import *

intents = discord.Intents.default()
allowed_mentions = discord.AllowedMentions(everyone=False,
                                           users=True,
                                           roles=True)
bot = discord.ext.commands.Bot(command_prefix=prefix,
                               intents=intents,
                               case_insensitive=True,
                               allowed_mentions=allowed_mentions)


@bot.command(aliases=['m'])
@commands.has_role('AVGL Summer League Staff')
async def match(ctx):
    player1 = ctx.message.mentions[0]
    player2 = ctx.message.mentions[1]
    category = ctx.channel.category
    staff = ctx.guild.get_role(staff_id)

    overwrites = {
        player1: discord.PermissionOverwrite(add_reactions=True,
                                             read_messages=True,
                                             send_messages=True,
                                             external_emojis=True,
                                             attach_files=True,
                                             embed_links=True),

        player2: discord.PermissionOverwrite(add_reactions=True,
                                             read_messages=True,
                                             send_messages=True,
                                             external_emojis=True,
                                             attach_files=True,
                                             embed_links=True),

        staff: discord.PermissionOverwrite(add_reactions=True,
                                           read_messages=True,
                                           send_messages=True,
                                           external_emojis=True,
                                           attach_files=True,
                                           embed_links=True),
        ctx.guild.default_role: discord.PermissionOverwrite(
            read_messages=False)
    }

    # create channel
    name = f"{player1.display_name} vs {player2.display_name}"
    topic = f"AVGL Summer League: {player1.display_name} vs {player2.display_name}"
    reason = "Staff invoked tourney match channel"
    match_channel = await \
        ctx.guild.create_text_channel(name=name,
                                      category=category,
                                      topic=topic,
                                      reason=reason,
                                      overwrites=overwrites)

    text = f" \n\n{copypasta}"
    embed = discord.Embed(color=discord.Colour.dark_green())
    embed.add_field(name=f"{player1.display_name} vs {player2.display_name}",
                    value=copypasta,
                    inline=False)
    embed.add_field(name="Default Match Time",
                    value=f"<t:{get_unix_time(6)}:F>"
                          f"\n(<t:{get_unix_time(6)}:R>)")
    embed.timestamp = datetime.datetime.now()
    embed.set_footer(icon_url=footer_icon,
                     text="GLHF!")
    await match_channel.send(embed=embed)
    await match_channel.send(f"{player1.mention} vs {player2.mention}")

    embed = discord.Embed(color=discord.Colour.green())
    embed.add_field(name=f"Match Started!",
                    value=f"Head on over to it: {match_channel.mention}")
    embed.set_footer(icon_url=footer_icon,
                     text="GLHF!")

    await ctx.reply(embed=embed)


def get_unix_time(date_index):
    # get current time
    date = datetime.datetime.utcnow()
    # cycle to date index (mon - sun | 0 - 6)
    while date.weekday() != date_index:
        date += datetime.timedelta(1)

    new_date = date.replace(hour=19, minute=0, second=0, tzinfo=timezone.utc)
    return round(new_date.timestamp())


bot.run(bot_token)
