import discord
from discord import message
from discord import member
from discord.ext import commands
from discord.ext.commands import Bot
from discord import member
import os
import shutil
import sys
#import pymysql
import mysql
import mysql.connector
client = commands.Bot(command_prefix = '.')

num_delo = 1
pl1 = None
pl2 = str()
st = str()
more = str()
nick = str()
verd = str()

@client.event
async def on_message(ctx):
    if ctx.content == ('.новое дело'):
        global num_delo
        nick = ctx.author.display_name
        pl1 = ctx.author.id

        await ctx.reply('Укажите ник игрока (User#0000)')
        #await ctx.channel.send('Укажите ник игрока (User#0000)')
        print(pl1)
        def check(q):
            return q.author.id == pl1
        msg = await client.wait_for('message', check=check)
        print (msg.content+' это дс наушителя')
        pl2 = str(msg.content)
        await ctx.channel.purge(limit=3)

        #await ctx.reply('Укажите возможные статьи. Если таковых нет - введите 0')
        await ctx.channel.send('Укажите возможные статьи. Если таковых нет - введите 0')
        def check2(w):
            return w.author.id == pl1
        msg2 = await client.wait_for('message', check=check2)
        print (msg2.content+' это статьи')
        st = msg2.content
        await ctx.channel.purge(limit=2)

        #await ctx.reply('Опишите подробности дела', mention_author=True)
        await ctx.channel.send('Опишите подробности дела')
        def check3(e):
            return e.author.id == pl1
        msg3 = await client.wait_for('message', check=check3)
        print (msg3.content+' это подобности дела')
        more = str(msg3.content)
        await ctx.channel.purge(limit=2)

        num_delo += 1

        embed = discord.Embed(
        title = '---------------------------------------------------------------------',
        colour = discord.Colour.dark_magenta()
        )
        embed.add_field(name='Дело:', value=num_delo, inline=False)
        embed.add_field(name='Подающий:', value=nick, inline=False)
        embed.add_field(name='Виновный:', value=pl2, inline=False)
        embed.add_field(name='Статьи:', value=st, inline=False)
        embed.add_field(name='Подобности:', value=more, inline=False)
        await ctx.channel.send(embed=embed)
        try:
            connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            database='bof',
            cursorclass=pymysql.cursors.DictCursor
            )

            try:
                with connection.cursor() as cursor:
                    sql = '''INSERT INTO sud(
              pl1, pl2, st, more,disid)
              VALUES'''
                    params = str(nick), str(pl2), str(st), str(more), str(pl1)
                    print(sql+ str(params))
                    cursor.execute(sql+ str(params))
                    connection.commit()
            finally:
                connection.close()

        except Exception as ex:
            print('not work')
            print(ex)

    if ctx.author.id == 279311290688602112 and ctx.content == ('.решение'):
        delo = 0
        pl1 = ctx.author.id
        await ctx.reply('Укажите номе дела')
        def check(r):
            return r.author.id == pl1
        answ = await client.wait_for('message', check=check)
        delo = answ.content

        await ctx.channel.purge(limit=3)

        await ctx.channel.send('Итог суда')
        def check(t):
            return t.author.id == pl1
        answ2 = await client.wait_for('message', check=check)
        verd = answ2.content

        await ctx.channel.purge(limit=2)

        embed = discord.Embed(
        title = '---------------------------------------------------------------------',
        colour = discord.Colour.dark_magenta()
        )
        embed.add_field(name='Дело:', value=delo, inline=False)
        embed.add_field(name='Вердикт:', value=verd, inline=False)
        await ctx.channel.send(embed=embed)

        try:
            connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            database='bof',
            cursorclass=pymysql.cursors.DictCursor
            )

            try:
                with connection.cursor() as cursor:
                    sqlupdate = "UPDATE sud SET verd = '"+ str(verd) + "' " + '''WHERE id = ''' + "'" + str(delo) + "'"
                    print(sqlupdate)
                    cursor.execute(sqlupdate)
                    connection.commit()
            finally:
                connection.close()

        except Exception as ex:
            print('not work')
            print(ex)
    if ctx.content == ('.дело'):
        pl1 = ctx.author.id
        await ctx.reply('Укажите номе дела')
        def check(r):
            return r.author.id == pl1
        deloinfoansw = await client.wait_for('message', check=check)
        deloansw = deloinfoansw.content
        try:
            connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            database='bof',
            cursorclass=pymysql.cursors.DictCursor
            )
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM sud WHERE id='%s'" % (deloansw))
                    rows = cursor.fetchall()
                    print(rows)

                for row in rows:
                    print(row[0] + 'dfjgu9gdfuifdijuhndfgdfgjuihodfginjdfgijiunj')
                    print(row)


                #    embed = discord.Embed(
                #    title = '---------------------------------------------------------------------',
                #    colour = discord.Colour.dark_magenta()
                #    )
                #    embed.add_field(name='Дело:', value=deloansw, inline=False)
                #    embed.add_field(name='Подающий:', value=rows[1], inline=False)
                #    embed.add_field(name='Виновный:', value=rows[2], inline=False)
                #    embed.add_field(name='Статьи:', value=rows[3], inline=False)
                #    embed.add_field(name='Подобности:', value=rows[4], inline=False)
                #    embed.add_field(name='Вердикт:', value=rows[5], inline=False)
                #    await ctx.channel.send(embed=embed)
                #    print("#"*30)
            finally:
                connection.close()
    
        except Exception as ex:
            print('not work')
            print(ex)

    if ctx.content == ('.отмена'):
        pl1 = ctx.author.id
        await ctx.reply('Укажите номе дела')
        def check(r):
            return r.author.id == pl1
        deloinfoansw = await client.wait_for('message', check=check)
        deloansw = deloinfoansw.content
        try:
            connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            database='bof',
            cursorclass=pymysql.cursors.DictCursor
            )
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT disid FROM sud WHERE id = " + deloansw)
                    rows = cursor.fetchall()
                    print(str(rows)[12:-3])
                    print(pl1)
                    if str(rows)[12:-3] == str(pl1):
                        cursor.execute("DELETE FROM sud WHERE id = " + deloansw)
                        connection.commit()
                        await ctx.channel.send('удалено!')
                    else:
                        await ctx.channel.send('у вас нет прав')

            finally:
                connection.close()
        except Exception as ex:
            print('not work')
            print(ex)

client.run('ODQzMDUzNzA4MTQ0Mjc5NTYy.YJ-Q8w.hlawkv3z0FAQ_96YaW9IvP2x5UY')
#.новое дело
#Tesaurus#0294
#1.3
#бла бла бла бла
#.решение
