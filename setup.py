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

RANDOM_STATUS = ['Debuggers', 'Use d!help p/ suporte']


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
        await client.change_presence(game=discord.Game(name=choice, url='https://www.twitch.tv/johncostaxv', type=1))
        await client.send_message(client, "Online!")
    except Exception as e:
        print("Todos direitos {}.".format("reservados"))
    print("Copyright ©")

@client.event
async def on_member_join(member):
    cargo = discord.utils.get(member.server.roles, name="Registrado")
    await client.add_roles(member, cargo)

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


    #global msg_id
    #msg_id = botmsg.id

    #global msg_user
    #msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🔐" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Registrado", msg.server.roles)
     await client.add_roles(user, role)
     role1 = discord.utils.find(lambda r: r.name == "Sem registro", msg.server.roles)
     await client.remove_roles(user, role1)
     await client.delete_message(msg_id)

     canal = client.get_channel('472896652110331924')

     embed = discord.Embed(
         title='Instruções abaixo:',
         color=COR,
         description='Para se autenticar e, ter acesso à todos os canais, você deve clicar na reação da mensagem (`🔐`).'
     )
     embed.set_author(name='Sistema de verificação', icon_url='https://media.giphy.com/media/fdkbq4UIYpRMk/giphy.gif')
     embed.set_thumbnail(url='https://media.giphy.com/media/8maYChvLIGU8jhsHl2/giphy.gif')
     embed.set_footer(text='Debuggers', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')

     botmsg = await client.send_message(canal, embed=embed)

     await client.add_reaction(botmsg, "🔐")

     canal = client.get_channel('470361261930971148')
     embed = discord.Embed(
        title='',
        color=COR,
        description='Seja bem-vindo(a) ao nosso servidor de Discord **Debuggers**!'
     )
     embed.set_author(name='Olá {}!'.format(user.name))
     embed.set_thumbnail(url=user.avatar_url)
     embed.set_footer(text='Debuggers', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
     await client.send_message(canal, embed=embed)


@client.event
async def on_message(message):
    if message.content.lower().startswith('d!publicar'):
        cargos = [
            # IDs dos cargos:
            "472535248408674304", #Vendedor
        ]
        for r in message.author.roles:
            if r.id in cargos:
                await client.delete_message(message)
                canal = client.get_channel('472921735805534240')
                remover_publicacao = message.content.replace("d!publicar ", "")
                separar = remover_publicacao.split("|", 2)
                embed = discord.Embed(
                    title='Produto à venda!',
                    color=COR,
                    description='Caso queria saber mais sobre este produto, entre em contato com o vendedor! Clique na reação abaixo (reaction) para solicitar atendimento (tenha a sua DM liberada)'
                )
                embed.add_field(
                    name='Vendedor:',
                    value=message.author.mention,
                    inline=False
                )
                embed.add_field(
                    name='Produto:',
                    value='%s' % ''.join(separar[0]),
                    inline=False
                )
                embed.add_field(
                    name='Descrição do produto:',
                    value='%s' % ''.join(separar[1]),
                    inline=False
                )
                embed.add_field(
                    name='Linguagem do produto:',
                    value='%s' % ''.join(separar[2]),
                    inline=False
                )
                embed.add_field(
                    name='Valor do produto:',
                    value='%s' % ''.join(separar[3]),
                    inline=False
                )
                embed.set_thumbnail(url='https://media.giphy.com/media/26uf4LsTj87JjVDbO/giphy.gif')
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text='Debuggers', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
                await client.send_message(canal, embed=embed)

    if message.content.lower().startswith('d!ban'):
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
                        title='Membro banido!',
                        color=COR,
                        description='O usuário **{}#{}**, foi banido permanentemente!\n\n**Motivo**: {}\n**Autor**: {}'.format(user.name, user.discriminator, join, message.author.mention)
                    )
                    embed.set_thumbnail(
                        url='https://media.giphy.com/media/qPD4yGsrc0pdm/giphy.gif'
                    )
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text='Debuggers', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
                    await client.send_message(channel1, embed=embed)
            else:
                 embed2 = discord.Embed(
                     title='Permissão negada!',
                     color=COR,
                     description='Você não tem permissão para executar esse comando.'
                 )
                 embed2.timestamp = datetime.datetime.utcnow()
                 embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
                 await client.send_message(message.channel, embed=embed2)
        except IndexError:
            await client.delete_message(message)
            embedd = discord.Embed(
                title='Comando incorreto!',
                color=COR,
                description='Use `!ban [username] [motivo]`'
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

    if message.content.lower().startswith('d!unmute'):
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
                description='Use `!unmute [username]`'
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

    if message.content.lower().startswith('d!mute'):
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
                description='Use `!mute [username] [motivo]`'
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

    if message.content.lower().startswith('d!say'):
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
                description='Use `!say [mensagem]`'
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

    if message.content.lower().startswith('d!anunciar'):
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
                    description='Use `!anunciar [mensagem]`'
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

    if message.content.lower().startswith('d!avatar'):
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

    if message.content.lower().startswith('d!serverinfo'):
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
        embed.add_field(name=":flag_br: Região:", value='Brasil')#str(message.server.region).title())
        embed.set_thumbnail(url='https://i.imgur.com/1iJeEea.jpg')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="End", icon_url="https://i.imgur.com/1iJeEea.jpg")
        await client.send_message(message.channel, embed=embed)


    if message.content.lower().startswith('d!javav'):
        embed1 = discord.Embed(
            title='Procurando atualizações...',
            description='⏳ Estamos procurando por atualizações!'
        )
        embed1.set_thumbnail(url='https://media.giphy.com/media/26u4arvdZ1v42ZVBK/giphy.gif')
        sc = await client.send_message(message.channel, embed=embed1)
        await client.add_reaction(message, '🔍')
        await asyncio.sleep(10)
        await client.delete_message(sc)
        await client.clear_reactions(message)
        embed = discord.Embed(
            title='Links:',
            description='Java - https://www.java.com/inc/BrowserRedirect1.jsp?locale=pt_BR (Version 8 Update 181 - 17/07/2018)\n\n'
                        'Java/Bukkit - https://getbukkit.org/get/uedXO8YBkhXjZwDTUVfO85a7DzAn01aD (1.13 - 22/07/2018)'
        )
        embed.set_author(name='Debuggers BOT - Java versions', icon_url='https://i.imgur.com/SadzyMQ.png')
        embed.set_thumbnail(url='https://i.imgur.com/kbK3X8k.png')
        embed.set_footer(text='Versões mais recente do java.', icon_url='https://i.imgur.com/u4qmnVX.png')

        msg = await client.send_message(message.channel, embed = embed)
        await client.add_reaction(msg, '📌')

    if message.content.lower().startswith('d!pythonv'):
        embed1 = discord.Embed(
            title='Procurando atualizações...',
            description='⏳ Estamos procurando por atualizações!'
        )
        embed1.set_thumbnail(url='https://media.giphy.com/media/26u4arvdZ1v42ZVBK/giphy.gif')
        sc = await client.send_message(message.channel, embed=embed1)
        await client.add_reaction(message, '🔍')
        await asyncio.sleep(10)
        await client.delete_message(sc)
        await client.clear_reactions(message)
        embed = discord.Embed(
            title='Links:',
            description='Python - https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz (Python 3.7.0 - 27/06/2018)\n\n'
                        'Python/Bots - https://files.pythonhosted.org/packages/97/3c/2a97b47fd8839f8863241857bbd6a3998d1de1662b788c8d9322e5a40901/discord.py-0.16.12.tar.gz (0.16.12 - 01/10/2017)'
        )
        embed.set_author(name='Debuggers BOT - Python versions', icon_url='https://i.imgur.com/SadzyMQ.png')
        embed.set_thumbnail(url='https://i.imgur.com/7pL7JMN.jpg')
        embed.set_footer(text='Versões mais recente do Python.', icon_url='https://i.imgur.com/FLmaZKT.png')

        msg = await client.send_message(message.channel, embed = embed)
        await client.add_reaction(msg, '📌')

    if message.content.lower().startswith('d!publicar'):
        cargos = [
            # IDs dos cargos:
            "472535248408674304", #Vendedor
        ]
        for r in message.author.roles:
            if r.id in cargos:
                await client.delete_message(message)
                canal = client.get_channel('472921735805534240')
                remover_publicacao = message.content.replace("d!publicar ", "")
                separar = remover_publicacao.split("|", 2)
                embed = discord.Embed(
                    title='Produto à venda!',
                    color=COR,
                    description='Caso queria saber mais sobre este produto, entre em contato com o vendedor! Clique na reação abaixo (📩) para solicitar atendimento (tenha a sua DM liberada)'
                )
                embed.add_field(
                    name='Vendedor:',
                    value=message.author.mention,
                    inline=False
                )
                embed.add_field(
                    name='Produto:',
                    value='%s' % ''.join(separar[0]),
                    inline=False
                )
                embed.add_field(
                    name='Descrição do produto:',
                    value='%s' % ''.join(separar[1]),
                    inline=False
                )
                embed.add_field(
                    name='Valor do produto:',
                    value='%s' % ''.join(separar[2]),
                    inline=False
                )
                embed.set_thumbnail(url='https://media.giphy.com/media/26uf4LsTj87JjVDbO/giphy.gif')
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text='Debuggers', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
                botmsg = await client.send_message(canal, embed=embed)
                await client.add_reaction(botmsg, "📩")

                global msg_id
                msg_id = botmsg.id

                global msg_user
                msg_user = message.author

                msg = reaction.message

                try:
                    if reaction.emoji == "📩" and msg.id == msg_id: #and user == msg_user:
                        await client.send_message(message.author, "O {} solicitou contato com o senhor, para tratar sobre o seu produto!".format(msg.author.name))
                except IndexError:
                    await client.send_message(canal, "{}, libere seu privado!".format(message.author.mention))
                except:
                    await client.send_message(canal, "{}, libere seu privadu!".format(message.author.mention))
                finally:
                    pass



client.run(os.environ.get("BOT_TOKEN"))
