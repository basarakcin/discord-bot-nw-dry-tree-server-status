import discord
import asyncio
from discord.ext import commands
from serverstatus import *

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

my_discord_channel_name = "<Insert Your Discord Channel Name Here>"

@client.event
async def on_ready(): 
    while True:
        category_list = []
        server_status = getServerStatus(serverName)
        availability = server_status.get("availability")
        availability += " " + status_emoji[availability]
        online_players = server_status.get("online-players")
        
        for server in client.guilds:
            if server.name == my_discord_channel_name: # Add desired channels here               
                for category in server.categories:
                    if category.name == nw_server_name:
                        await category.move(beginning=True)
                        category_list.append(category)
                        for channel in category.channels:
                            await channel.delete()
                        await category.create_voice_channel("Status: " + availability)
                        await category.create_voice_channel(online_players + " / 2,000")
                        for channel in category.channels:
                            for role in server.roles:
                                await channel.set_permissions(role, connect=False) 
                if len(category_list) == 0:
                    try:
                        # print("Adding \""+ nw_server_name + "\" category to: " + server.name) # DEBUG
                        await server.create_category("Dry Tree")
                    except:
                        # print("Failed to add \"" + nw_server_name + "\" category to: " + server.name) # DEBUG
                        continue
        await asyncio.sleep(30)

client.run(DISCORD_TOKEN)
