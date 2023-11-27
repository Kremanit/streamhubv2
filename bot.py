import datetime
import disnake

from disnake.ext import commands, tasks

client = commands.Bot(command_prefix=";", 
                    intents = disnake.Intents.all(), 
                    activity = disnake.Game("/help", 
                                            status=disnake.Status.idle))

client.remove_command('help')

client.load_extension("cogs.slash_commands")
client.load_extension("cogs.event")
client.load_extension("cogs.moderation")








#░░░██╗░██╗░████████╗░█████╗░████████╗░░░░░░██╗░░██╗███╗░░░███╗██╗░░██╗
#██████████╗╚══██╔══╝██╔══██╗╚══██╔══╝░░░░░░██║░██╔╝████╗░████║██║░░██║
#╚═██╔═██╔═╝░░░██║░░░██║░░╚═╝░░░██║░░░█████╗█████═╝░██╔████╔██║███████║
#██████████╗░░░██║░░░██║░░██╗░░░██║░░░╚════╝██╔═██╗░██║╚██╔╝██║██╔══██║
#╚██╔═██╔══╝░░░██║░░░╚█████╔╝░░░██║░░░░░░░░░██║░╚██╗██║░╚═╝░██║██║░░██║
#░╚═╝░╚═╝░░░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝

@client.slash_command(description='test-embed')
async def testembed(inter):
    embed = disnake.Embed(title="title", description="description", url="https://test.com/", color=0x2D3136)
    embed.add_field(name="name1", value="value1", inline=True)
    embed.add_field(name="name2", value="value2", inline=False)
    embed.add_field(name="name3", value="value3", inline=True)
    embed.add_field(name="name4", value="value4", inline=True)
    embed.set_image(url="https://cataas.com/cat/gif")
    embed.set_author(name="author", url="https://vk.com/kremabit", icon_url="https://32.img.avito.st/208x156/8147078432.jpg")
    embed.set_footer(text="footer")
    embed.set_thumbnail(url="https://i.ytimg.com/vi/3sCAg_Ex0Jc/maxresdefault.jpg")
    await inter.send(embed=embed)


@client.slash_command()
async def ping(inter):
    await inter.response.send_message("Pong!")





#░░░██╗░██╗░███████╗██████╗░██████╗░░█████╗░██████╗░
#██████████╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
#╚═██╔═██╔═╝█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
#██████████╗██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
#╚██╔═██╔══╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
#░╚═╝░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝







token = '***********'
client.run(token)
