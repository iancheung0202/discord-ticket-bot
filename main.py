import discord, asyncio, datetime
from discord.ext import commands
from discord.ext.commands import has_permissions
import config, ticket

bot = ticket.init(config.PREFIX, config.BOT_DESCRIPTION, config.STATUS)

@bot.event
async def on_button_click(interaction):
  await ticket.button_click(bot, interaction, config.TICKET_LOG, config.CATEGORY_ID, config.DETELE_TICKET_TIMEOUT) # Bot Object, Interaction Object, Ticket Log ID, Category ID, Delete Ticket Timeout

@bot.command()
async def help(ctx):
  await ticket.DM(bot, ctx)
  
@bot.command()
async def close(ctx):
  await ticket.closeTicket(bot, ctx)

@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def embed(ctx):
  await ticket.Embed(bot, ctx)

ticket.keepOnline()

bot.run(config.BOT_TOKEN)