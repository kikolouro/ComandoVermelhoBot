from __future__ import division, print_function

import discord
from decouple import config

from dbHandler import dbHandler


async def logToChannel(message, channel):
    channel = client.get_channel(int(channel))
    await channel.send(message)


class discordBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        game = discord.Game("na Favela 🔫")
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        msg = str(message.content)

        if message.content.startswith('!removeuser') and message.author.id != self.user.id:

            await message.add_reaction('🤔')
            if len(msg.split()) == 1:
                await message.channel.send(f"<@!{message.author.id}> Tens que mencionar alguem oh burro")
                return
            elif len(msg.split()) > 2:
                await message.channel.send(f"<@!{message.author.id}> Não sejas burro e faz as merdas direito")
                return

            userid = msg.split()[1].replace(
                '<', '').replace('>', '').replace('@', '')

            if db.removeUser(userid):
                await logToChannel(f"<@!{message.author.id}> Removeu o <@!{userid}>. Adeus cabrão.", config('CHANNEL_LOG'))
            else:
                await message.channel.send(f"<@!{message.author.id}> Já existe o <@!{userid}>. Deixa de ser burro")
            return

        if message.content.startswith('!adduser') and message.author.id != self.user.id:

            await message.add_reaction('🤔')
            if len(msg.split()) == 1:
                await message.channel.send(f"<@!{message.author.id}> Tens que mencionar alguem oh burro")
                return
            elif len(msg.split()) > 2:
                await message.channel.send(f"<@!{message.author.id}> Não sejas burro e faz as merdas direito")
                return
            userid = msg.split()[1].replace(
                '<', '').replace('>', '').replace('@', '')

            user = await client.fetch_user(int(userid))
            if db.addUser(userid, str(user)):
                await logToChannel(f"<@!{message.author.id}> Adicionou o <@!{userid}>.", config('CHANNEL_LOG'))
            else:
                await message.channel.send(f"<@!{message.author.id}> Já existe o <@!{userid}>. Deixa de ser burro")
            return

        if message.content.startswith('!coca') and message.author.id != self.user.id:
            await message.add_reaction('🤔')
            command = 'coca'

            if len(msg.split()) == 1:
                await message.channel.send(f"<@!{message.author.id}> Não sejas burro, mete a quantidade de {command} que farmaste!")
                return
            elif len(msg.split()) > 2 or not msg.split()[1].isdigit() or int(msg.split()[1]) < 1:
                await message.channel.send(f"<@!{message.author.id}> Não sejas atrasado mental e mete apenas a quantidade de {command} que farmaste!")
                return

            amount = int(msg.split()[1])
            await logToChannel(f"<@!{message.author.id}> Farmou {amount} {command}", config('CHANNEL_LOG'))

            return

        if message.content.startswith('!getinfo') and message.author.id != self.user.id:

            await message.channel.send("<@!" + "264507064863162368" + "> Burro")
            return


db = dbHandler(config('DBFILE'))
client = discordBot()
client.run(config("DISCORD_TOKEN"))
