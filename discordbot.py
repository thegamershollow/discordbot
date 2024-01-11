import discord
import asyncio
import sys
from datetime import datetime
import nest_asyncio
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
token=os.getenv('')
ethan = 917438708163182632
nest_asyncio.apply()
# asks what bot you would like to use
u = input("What user would you like to use? [botboy or ethan]: ")
#u = 'boyboy'
# checks if the selected bot exists
if u.lower() == "ethan":
    # passes the bot's token into the program
    token=os.getenv('ethan')
elif u.lower() == "botboy":
    # passes the bot's token into the program
    token=os.getenv('botboy')
else:
    print("please enter a valid username [botboy or ethan]")

# creates a dicord client class
class MyClient(discord.Client):
    # async function that runs when the program starts
    async def on_ready(self):
        # global variables for the log files
        global f
        global dtf2
        global dtf
        # sets discord bots' statuses depending on which bot is in use
        if u.lower() == "botboy":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Insane ADHD People'))
        if u.lower() == "ethan":
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Paw Patrol'))
        # prints that you have succesfully logged in
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        # tells you how to use the bot
        print("running bot\nUse !"+u+" [text] to send a message through "+u+"\n------")

        # variables for the log file
        dt = datetime.now()
        dtf = dt.strftime('%m-%d-%Y')
        dtf2 = dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        filename = f'{u}.log'
        f = open(filename,"a")
        f.write(f'{dtf2} - started bot: {u} ')
    # async function that runs when a discord message is sent by another user
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        channel2 = message.channel.id
        channel = self.get_channel(int(channel2))
        # checks if the message starts with the bots command and if the user running it is thattransgirl
        if message.content.startswith('!help'):
            await message.delete()
            await channel.send("Help Section")
        if message.content.startswith('!status'):
            m = message.content
            m = m.replace('!status ','')
            print(m)
            await message.delete()
        if message.content.startswith('!echo') and message.author.id == ethan:
            m = message.content
            m = m.replace('!echo ','')
            os.system(f'echo {m}')
            await message.delete()
        if message.content.startswith('!'+u) and message.author.id == ethan:
            # gets the message content
            m = message.content
            # replaces the bot command with nothing
            m = m.replace("!"+u+" ","")
            # basic logging for messages
            orig = f'{channel}-({message.author}): {m} [{message.created_at.strftime("%Y-%m-%d %H:%M:%S")}]'
            print(orig)
            f.write(f'{dtf2} - {orig}\n')
            # basic logging for deleting messages
            deleted = f"Deleted original message sent by {message.author}"
            print(deleted)
            f.write(f'{dtf2} - {deleted}\n')
            # deletes the original message
            await message.delete()
            # basic logging for sent messages
            sent = f"Sent ({m}) as {u}"
            print(sent)
            f.write(f'{dtf2} - {sent}\n')
            # sends the message to the specified channel
            await channel.send(m)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
