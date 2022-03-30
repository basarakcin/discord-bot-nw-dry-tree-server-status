import discord
import asyncio
from discord.ext import commands
from serverstatus import *

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

my_discord_channel_name = "<Insert Your Discord Channel Name Here>"

@client.event
async def on_ready(): 
    print("Starting bot...")
    while True:
        server_status = getServerStatus(serverName)

        for server in client.guilds:
            if server.name == my_discord_channel_name: # Add desired channels here               
                is_available = False            
                for category in server.categories:
                    if category.name == nw_server_name:                        
                        is_available = True
                        for channel in category.channels:
                            if "2,000" in channel.name:
                                await asyncio.sleep(5)
                                print(channel.name)
                                await channel.edit(name=server_status[1])
                                print("2,000 done")
                            elif channel.name == server_status[0]:   
                                continue
                            else:                           
                                await asyncio.sleep(5)
                                print(channel.name)
                                await channel.edit(name=server_status[0])       
                                print("else done")                  
                    else:
                        continue
                if is_available:
                    continue
                else:
                    try:
                        category = await server.create_category("Dry Tree")
                        # print("Adding \""+ nw_server_name + "\" category to: " + server.name) # DEBUG
                        await category.move(beginning=True)
                        for role in server.roles:
                            await category.set_permissions(role, connect=False) 
                        await create_vc(category, server_status)
                    except:
                         # print("Failed to add \"" + nw_server_name + "\" category to: " + server.name) # DEBUG
                        continue
        await asyncio.sleep(30)

async def create_vc(category, server_status):
    await category.create_voice_channel(server_status[0])
    await category.create_voice_channel(server_status[1])
    
client.run(DISCORD_TOKEN)
