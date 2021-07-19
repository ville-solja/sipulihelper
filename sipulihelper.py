import discord
from datetime import datetime
import os

TOKEN = os.environ['TOKEN']    

client = discord.Client()

@client.event
async def on_ready():
    print('{} bot started'.format(
        datetime.now().strftime("%d.%m.%Y, %H:%M:%S")))
    print('Client Name: {}'.format(
        client.user.name))
    print('Client ID: {}'.format(
        client.user.id))
    for guild in client.guilds:
        print('Guild: {}'.format(
            guild.name))
        for voice_channel in guild.voice_channels:
            if voice_channel.position == 1:
                print('Voice Channel: {}'.format(
                    voice_channel))

@client.event
async def on_voice_state_update(member, before, after):
    for voice_channel in member.guild.voice_channels:
        if voice_channel.position == 1:
            if len(voice_channel.members) > 0:
                print("Users in voice channel: {}".format(len(voice_channel.members)))
                #Start
            else:
                print("Users in voice channel: {}".format(len(voice_channel.members)))
                #Pause server

client.run(TOKEN)
