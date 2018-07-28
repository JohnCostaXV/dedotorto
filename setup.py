import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import asyncio
import time
import datetime
import sys
import io
import os
import re
import json
import base64

RANDOM_STATUS = ['em Desenvolvendo']
RANDOM_MENSAGENS = ['AsCD', 'BabV', 'KaOx', 'LdXa', 'AuTi', 'MsGi', 'PoNti']


client = discord.Client()
COR = 0x3498DB
testmsgid = None
testmsguser = None

minutes = 0
hour = 0
msg_id = None
msg_user = None
user_timer = {}
user_spam_count = {}

@client.event
async def on_ready():
    print('Iniciado com sucesso!')
    print(client.user.name)
    print(client.user.id)
    print('Versão 1.0')
    print('Status = {}'.format(RANDOM_STATUS))
    try:
        choice = random.choice(RANDOM_STATUS)
        await client.change_presence(game=discord.Game(name=choice, type=1))
        await client.send_message(client, "Online!")
    except Exception as e:
        print("Todos direitos {}.".format("reservados"))
    print("Copyright ©")

@client.event
async def on_member_join(member):
    canal = client.get_channel('470361261930971148')
    embed = discord.Embed(
        title='',
        color=COR,
        description='Seja bem-vindo(a) ao nosso servidor de Discord **Debuggers**!'
    )
    embed.set_author(name='Olá {}!'.format(member.name))
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text='Debuggers', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
    await client.send_message(canal, embed=embed)
    cargo = discord.utils.get(member.server.roles, name="Registrado")
    await client.add_roles(member, cargo)
    print("Adicionado o cargo '" + cargo.name + "' para " + member.name)

@client.event
async def on_message(message):
    if message.content.lower().startswith('/ban'):
        try:
            cargos = [
                # IDs dos cargos:
                "470362038116286474", #Dono
                "470728749243957249", #Administrador
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    asyncio.sleep(10)
                    args = message.content.split(" ")
                    await client.delete_message(message)
                    channel1 = client.get_channel('470673691827634176')
                    user = message.mentions[0]
                    await client.ban(user)
                    join = (" ".join(args[2:]))
                    embed = discord.Embed(
                        title='BANIDO ⛔',
                        color=COR,
                        description='O usuário **{}#{}**, foi banido!\n\n**Motivo**: {}\n**Autor**: {}'.format(user.name, user.discriminator, join, message.author.mention)
                    )
                    embed.set_thumbnail(
                        url='https://i.imgur.com/1iJeEea.jpg'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(channel1, embed=embed)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/ban [username] [motivo]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass

    if message.content.lower().startswith('/unmute'):
        try:
            cargos = [
                # IDs dos cargos:
                "470362038116286474", #Dono
                "470728749243957249", #Administrador
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    user = message.mentions[0]
                    cargo = discord.utils.get(user.server.roles, name='Silenciado')
                    canal = client.get_channel('448449971629588481')
                    embed = discord.Embed(
                        title='DESMUTADO 🔊',
                        color=COR,
                        description='O usuário **{}#{}**, não está mais silenciado!\n\nAutor: {}'.format(user.name, user.discriminator, message.author.mention)
                    )
                    embed.set_thumbnail(
                        url='https://i.imgur.com/1iJeEea.jpg'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(canal, embed=embed)
                    await client.remove_roles(user, cargo)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/unmute [username]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass

    if message.content.lower().startswith('/mute'):
        try:
            cargos = [
                # IDs dos cargos:
                "470362038116286474", #Dono
                "470728749243957249", #Administrador
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    join = (" ".join(args[2:]))
                    user = message.mentions[0]
                    canal = client.get_channel('448449971629588481')
                    cargo = discord.utils.get(user.server.roles, name="Silenciado")
                    embed = discord.Embed(
                        title='SILENCIADO 🔈',
                        color=COR,
                        description='O usuário **{}#{}**, foi silenciado!\n\n**Motivo**: {}\n**Autor**: {}'.format(user.name, user.discriminator, join, message.author.mention))
                    embed.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='End', icon_url='https://i.imgur.com/1iJeEea.jpg')
                    await client.send_message(canal, embed=embed)
                    await client.add_roles(user, cargo)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/mute [username] [motivo]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass

    if message.content.lower().startswith('/say'):
        try:
            cargos = [
                # IDs dos cargos:
                "470362038116286474", #Dono
                "470728749243957249", #Administrador
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    await client.send_message(message.channel, (" ".join(args[1:])))
                    asyncio.sleep(1)
                    await client.delete_message(message)
                    asyncio.sleep(1)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `/say [mensagem]`'
            )
            embedd.timestamp = datetime.datetime.utcnow()
            embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embedd)
        except:
            await client.delete_message(message)
            embed2 = discord.Embed(
                title='Permissão negada!',
                color=COR,
                description='Você não tem permissão para executar esse comando.'
            )
            embed2.timestamp = datetime.datetime.utcnow()
            embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed2)
        finally:
            pass

    if message.content.lower().startswith('/anunciar'):
            try:
                cargos = [
                    # IDs dos cargos:
                    "470362038116286474", #Dono
                    "470728749243957249", #Administrador
                ]
                for r in message.author.roles:
                    if r.id in cargos:
                        await client.delete_message(message)
                        args = message.content.split(" ")
                        embed = discord.Embed(
                            title="",
                            color=COR,
                            description=" ".join(args[1:])
                        )
                        embed.set_author(name='Anúncio', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
                        embed.timestamp = datetime.datetime.utcnow()
                        embed.set_footer(
                            text="Enviado por: {}".format(message.author.name),
                            icon_url=message.author.avatar_url
                        )
                        await client.send_message(message.channel, "@everyone")
                        await client.send_message(message.channel, embed=embed)
            except IndexError:
                await client.delete_message(message)
                embedd = discord.Embed(
                    title='Comando incorreto!',
                    color=COR,
                    description='Use `/anunciar [mensagem]`'
                )
                embedd.timestamp = datetime.datetime.utcnow()
                embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=embedd)
            except:
                await client.delete_message(message)
                embed2 = discord.Embed(
                    title='Permissão negada!',
                    color=COR,
                    description='Você não tem permissão para executar esse comando.'
                )
                embed2.timestamp = datetime.datetime.utcnow()
                embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=embed2)
            finally:
                pass

    if message.content.lower().startswith('/avatar'):
        try:
            user = message.mentions[0]
            embed = discord.Embed(
                title="",
                color=COR,
                description='Clique [aqui](' + user.avatar_url + ') para acessar o avatar do {}.'.format(user.name)
            )
            embed.set_author(
                name=message.server.name,
                icon_url='https://i.imgur.com/1iJeEea.jpg'
            )
            embed.set_image(
                url=user.avatar_url
            )
            await client.send_message(message.channel, embed=embed)
        except IndexError:
            await client.delete_message(message)
            msg = await client.send_message(message.channel, '{}, mencione um usuário existente, por exemplo, `/avatar @{}`.'.format(message.author.mention, message.author.name))
            time.sleep(10)
            await client.delete_message(msg)
        except:
            msg1 = await client.send_message(message.channel, 'Desculpe pelo erro.')
            time.sleep(5)
            await client.delete_message(msg1)
        finally:
            pass

    if message.content.lower().startswith('/serverinfo'):
        embed = discord.Embed(
            title='Informações do Servidor',
            color=0x03c3f5,
            descripition='Essas são as informações\n')
        embed.set_author(name=message.server.name, icon_url='https://i.imgur.com/1iJeEea.jpg')
        embed.add_field(name="Nome:", value=message.server.name, inline=True)
        embed.add_field(name=":crown: Dono:", value=message.server.owner.mention)
        embed.add_field(name="ID:", value=message.server.id, inline=True)
        embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        embed.add_field(name=":family: Membros:", value=len(message.server.members), inline=True)
        embed.add_field(name=":date: Criado em:", value=message.server.created_at.strftime("%d de %bho, %Y às %H:%M"))
        embed.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embed.add_field(name=":flag_br: Região:", value=str(message.server.region).title())
        embed.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="End", icon_url="https://i.imgur.com/1iJeEea.jpg")
        await client.send_message(message.channel, embed=embed)

client.run(os.environ.get("BOT_TOKEN"))
