import os, discord, asyncio, random
from discord.ext import commands
from keep_alive import keep_alive

keep_alive()
TOKEN = os.environ['DISCORD_TOKEN']

if TOKEN is not None:
  intents = discord.Intents.all()
  intents.message_content = True

  # create a connection to discord through an instance of Client
  client = discord.Client(intents=intents)

  #event decorators tell the program to register an event
  @client.event
  #we use async keyword to designate a callback function for the on_ready event
  async def on_ready():
    print(f'{client.user} has connected to Discord!')

  @client.event
  async def on_message(message):
    if message.author != client.user and message.content.startswith("!roll"):
      await message.channel.send("Which-sided die?:\n**4**,**6**,**8**,**10**,**12**,**20**")

      try:
        die = await client.wait_for("message", timeout = 30.0)
        d = die.content

        check_die = [4,6,8,10,12,20]

        if d not in check_die:
            await message.channel.send("Sorry, invalid choice.")
            return
          
        await message.channel.send("Number of rolls?")
        number_of_rolls = await client.wait_for("message", timeout=30.0)

        n = int(number_of_rolls.content)
        if n < 1:
          await message.channel.send("Sorry, invalid choice.")
          return
          
        for each in range(n):
          await message.channel.send(f"roll {each+1}: " + str(random.randint(1, int(d))))

      except asyncio.TimeoutError:
        await message.channel.send("Timed out.")

  @client.event
  async def on_member_join(member):
    if member.guild.system_channel is not None:
      to_send = f'Welcome to {member.guild.name}, {member.mention}!'
      await member.guild.system_channel.send(to_send)

    await member.send(f"""Welcome to {member.guild.name}, {member.mention}!

    Which role would you like to assign to yourself? 

    test role 🧪

    React to this message with the role you want! 
    """)
    
    def check(reaction, user):
      return str(reaction.emoji) == '🧪' and user.name == member.name
      
    try:
      reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
      await member.add_roles(discord.Object(1198344146881097868))
  
    except asyncio.TimeoutError:
      await member.send('You took too long to respond!')

  @client.event
  async def on_member_remove(member):
    if member.guild.system_channel is not None:
      to_send = f'We hate to see you go, {member.mention}!'
      await member.guild.system_channel.send(to_send)

  @client.event
  async def on_member_ban(member):
    if member.guild.system_channel is not None:
      await member.guild.system_channel.send('See ya later, stinko.')

  client.run(TOKEN)


# commands

  bot = commands.Bot(command_prefix='!', intents=intents)
  
  @bot.command()
  async def foo(ctx, arg):
      await ctx.send("Will this ever work!?")
    
else:
  print('DISCORD_TOKEN environment variable is not set.')