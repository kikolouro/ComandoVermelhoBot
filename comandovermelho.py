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
            flag = True
            for role in message.author.roles:
                if role.name == config("ADMINROLE"):
                    flag = False
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
            if flag:
                await message.channel.send(f"<@!{message.author.id}> não tens permissão para fazer isto nabo.")


        if message.content.startswith('!adduser') and message.author.id != self.user.id:
            await message.add_reaction('🤔')
            flag = True
            for role in message.author.roles:
                if role.name == config("ADMINROLE"):
                    flag = False
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
            if flag:
                await message.channel.send(f"<@!{message.author.id}> não tens permissão para fazer isto nabo.")

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
            if db.addDrug(message.author.id, "coca", amount):
                await logToChannel(f"<@!{message.author.id}> Farmou {amount} {command}", config('CHANNEL_LOG'))
            return

        if message.content.startswith('!getinfo') and message.author.id != self.user.id:
            await message.add_reaction('🤔')
            if len(msg.split()) == 1:
                data = db.getAllUserDrugs()
                for user in data:
                    e = discord.Embed(title=f"Stats do burro: " + data[user]["name"],
                                      description="", colour=0xfc03ca)
                    e.add_field(name="Erva:", value=str(
                        data[user]["erva"]) + "\n", inline=True)
                    e.add_field(name="Coca:", value=str(
                        data[user]["coca"]) + "\n", inline=True)
                    e.add_field(name="Opio:", value=str(
                        data[user]["opio"]) + "\n", inline=True)
                    e.add_field(name="Meta:", value=str(
                        data[user]["meta"]) + "\n", inline=True)
                    await message.channel.send("", embed=e)
            else:
                await message.channel.send("<@!" + message.author.id + "> Deixa de ser mongloide.")
            return


db = dbHandler(config('DBFILE'))
client = discordBot()
client.run(config("DISCORD_TOKEN"))
