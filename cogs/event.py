import disnake
from disnake.ext import commands, tasks


class event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(831397576107622420)
        await channel.send( embed = disnake.Embed( description = f'```Пользователь {member.name}, присоединился к нам!```', color= 0x2D3136))
        print (f'[Logs:info] Новый участник!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(831397576107622420)
        await channel.send( embed = disnake.Embed( description = f'```Пользователь {member.name}, покинул нас(!```', color= 0x2D3136))
        print (f'[Logs:info] Нас покинули!')

# Logs 
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.client.get_channel(880761120447664158)
        embed = disnake.Embed(title = f"Сообщение удалено.", description = f"**Автор:**{message.author} ({message.author.id})\n**Канал:**{message.channel.mention}\n**Содержание сообщения:**{message.content}", color = disnake.Colour.red())
        await channel.send(embed = embed)
        print (f'[Logs:info] Новый лог!')

    @commands.Cog.listener()
    async def on_connect(self, message):
        channel = self.client.get_channel(880761120447664158)
        embed = disnake.Embed(title = f"Сообщение удалено.", description = f"**Автор:**{message.author} ({message.author.id})\n**Канал:**{message.channel.mention}\n**Содержание сообщения:**{message.content}", color = disnake.Colour.red())
        await channel.send(embed = embed)
        print (f'[Logs:info] Новый лог!')
        


def setup(client):
    client.add_cog(event(client))
    print(f">Extension {__name__} is ready")