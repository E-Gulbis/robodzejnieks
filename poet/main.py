import discord
from discord.ext import commands
import os
import random

# === Intents ===
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# === 1. Bot Starts ===
@bot.event
async def on_ready():
    print(f'{bot.user.name} is online.')
    print('Bot works in these servers:')
    for guild in bot.guilds:
        print(f'- {guild.name}')

# === 2. Random poem command ===
@bot.command(name='dzeja')
async def send_random_poem(ctx):
    poems = os.listdir('poems')
    if not poems:
        await ctx.send("❌ Nav pieejamu dzejoļu.")
        return

    poem_file = random.choice(poems)
    with open(os.path.join('poems', poem_file), 'r', encoding='utf-8') as f:
        content = f.read()
    await ctx.send(f'📜 Nejaušs dzejolis:\n\n{content}')

# === 3. Generate new poem from existing ===
@bot.command(name='ģenerēt')
async def generate_poem(ctx):
    lines = []
    for fname in os.listdir('poems'):
        with open(os.path.join('poems', fname), 'r', encoding='utf-8') as f:
            lines.extend(f.readlines())

    lines = [line.strip() for line in lines if line.strip()]
    if len(lines) < 4:
        await ctx.send("❌ Nepietiek rindu, lai ģenerētu jaunu dzejoli.")
        return

    new_poem = "\n".join(random.sample(lines, 4))  # 4 rindas
    await ctx.send(f'🧠 Ģenerēts dzejolis:\n\n{new_poem}')

# === 4. Simple test command ===
@bot.command()
async def dzivs(ctx):
    await ctx.send("Esmu dzīvs!")

# === 5. Run bot using token from file ===
def get_token():
    with open('bot_key.txt', 'r', encoding='utf-8') as f:
        return f.read().strip()

bot.run(get_token())
