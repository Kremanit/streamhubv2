import disnake
from disnake.ext import commands, tasks


class SlashCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description='Список команд')
    async def help (self, inter):
        embed = disnake.Embed(title = 'ДОСТУПНЫЕ КОМАНДЫ:', description = '', color= 0x2D3136)

        embed.set_author(name = inter.author.name, icon_url = inter.author.avatar.url)
        embed.add_field(name = 'Информация', value = f'`/time` `/info` `/rank` `/leaderboard` ', inline=False)
        embed.add_field(name = 'Музыка', value = f'`/play` `/pause` `/resume` `/seek` `/queue` `/volume` `/loop` ', inline=False)
        embed.set_footer(icon_url = self.client.user.avatar.url, text = f'{self.client.user.name} © Copyright 2022 | Все права защищены')

        await inter.send(embed = embed)

        print(f'[Logs:info] Справка по командам была успешно выведена | /help ')

    @commands.slash_command(description='Информация о сервере')
    async def info(self, inter):
        owner = inter.guild.owner.mention
        all = len(inter.guild.members)
        members = len(list(filter(lambda m: not m.bot, inter.guild.members)))
        bots = len(list(filter(lambda m: m.bot, inter.guild.members)))
        statuses = [len(list(filter(lambda m: str(m.status) == "online", inter.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", inter.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", inter.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", inter.guild.members)))]
        channels = [len(list(filter(lambda m: str(m.type) == "text", inter.guild.channels))),
                    len(list(filter(lambda m: str(m.type) == "voice", inter.guild.channels)))]

        embed = disnake.Embed(title=f"{inter.guild} команды")
        embed.add_field(name="Участники:", value=f"All: {all} Humans: {members} Bots: {bots}")
        embed.add_field(name="Статусы", value=f"Online: {statuses[0]} Idle: {statuses[1]} DND: {statuses[2]} Offline: {statuses[3]}")
        embed.add_field(name="Каналы", value=f"All: {channels[0] + channels[1]} Text: {channels[0]} Voice: {channels[1]}")
        embed.add_field(name="Owner", value=owner)
        await inter.send(embed=embed)

    @commands.slash_command(description='Информация о пользователе')
    async def user(self, inter, member: disnake.Member):

        if member==None:
            member=inter.author


        embed = disnake.Embed(title = 'ДОСТУПНЫЕ КОМАНДЫ:', description = '', color= 0x2D3136)

        embed.set_author(name=f"User Info - {member}"),
        embed.set_thumbnail(url=member.avatar_url),
        embed.set_footer(text=f'Requested by - {inter.author}', icon_url=inter.author.avatar_url)

        embed.add_field(name='ID:', value=member.id, inline=False)
        embed.add_field(name='Name:', value=member.display_name, inline=False)

        embed.add_field(name='Created at:', value=member.created_at, inline=False)
        embed.add_field(name='Joined  at:', value=member.joined_at, inline=False)


        embed.add_field(name='Bot?', value=member.bot, inline=False)

        

def setup(client):
    client.add_cog(SlashCommands(client))
    print(f">Extension {__name__} is ready")