from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

# Define the intents required for the bot to work
intents = discord.Intents.default()
intents.message_content = True  # Enable intents for reading message content

# Pass the intents to the Bot instance
bot = commands.Bot(command_prefix="$", intents=intents)  # <--- Intents are added here

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='poll')
async def poll(ctx, question: str, *options):
    if len(options) < 2:
        await ctx.send("You need at least two options to create a poll.")
        return
    elif len(options) > 10:
        await ctx.send("You can only provide a maximum of 10 options.")
        return

    description = ""
    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    for i, option in enumerate(options):
        description += f"{emojis[i]} {option}\n"

    embed = discord.Embed(title=question, description=description, color=0x00ff00)
    poll_message = await ctx.send(embed=embed)

    for i in range(len(options)):
        await poll_message.add_reaction(emojis[i])

bot.run(token)