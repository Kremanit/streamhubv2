import datetime
import disnake
from disnake.ext import commands, tasks


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(pass_context = True)
    @commands.has_permissions( administrator = True)

    async def clear(self, inter, amount: int):
        await inter.channel.purge( limit = amount)
        await inter.send(embed = disnake.Embed(description = f'✅Удалено {amount} собщений', colour = disnake.Color.orange()))
        await inter.message.delete()

    @commands.slash_command(pass_context = True)
    @commands.has_permissions(administrator = True)

    async def kick(self, inter, member: disnake.Member, *, reason = None):
        await inter.channel.purge(limit = 1)
        await member.kick(reason = reason)
        await inter.send(f'kick user {member.mention}')

    @commands.slash_command(pass_context = True)
    @commands.has_permissions(administrator = True)

    async def ban(self, inter, member: disnake.Member, *, reason = None):
        emb = disnake.Embed(title = 'Бан', colour = disnake.Color.red())

        await inter.channel.purge( limit = 1)
        await member.ban(reason = reason)

        emb.set_author(name = member.name, icon_url = member.avatar.url )
        emb.add_field(name = 'Забанненый пользователь', value = 'Пользователь: {}'.format(member.mention))
        emb.set_footer(text = 'Был забанен администратором {}'.format(inter.author.name), icon_url = inter.author.avatar.url)

        now_date = datetime.datetime.now()

        emb.add_field(name = 'Время бана', value = 'Time : {}'.format( now_date ))

        await inter.send(embed = emb)

        await inter.send(f'ban user {member.mention}')

    @clear.error
    async def clear_error(self, inter, error):
        if isinstance( error, commands.MissingRequiredArgument ):
            await inter.send(f'{ inter.author.name }, обязательно укажите аргумент!')

        if isinstance( error, commands.MissingPermissions ):
            await inter.send(f'{ inter.author.name }, у вас недостаточно прав!')

    @ban.error
    async def clear_error(self, inter, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await inter.send(f'{ inter.author.name }, обязательно укажите человека!')

        if isinstance(error, commands.MissingPermissions):
            await inter.send(f'{ inter.author.name }, у вас недостаточно прав!')

    @kick.error
    async def clear_error(self, inter, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await inter.send(f'{ inter.author.name }, обязательно укажите человека!')

        if isinstance(error, commands.MissingPermissions):
            await inter.send(f'{ inter.author.name }, у вас недостаточно прав!')


def setup(client):
    client.add_cog(moderation(client))
    print(f">Extension {__name__} is ready")