import asyncio
from asyncio.windows_events import NULL
import math
from pickle import TRUE
from re import S
import time
from turtle import right
import discord
from discord.ext import commands
from matplotlib import image
import mysql.connector
import random
import datetime
from datetime import datetime, timedelta
import requests
import base64
from io import BytesIO #from io import StringIO.
import PIL.Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageFile
import io
import string
from discord_slash.utils import manage_components
from discord_slash.model import ButtonStyle
import emoji
from threading import Lock

def get_custom_image(card_unique_id):
    def center_text_top(img, font, text, height, color=(0, 0, 0), ):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-text_width)/2, height)
        draw.text(position, text, color, font=font)
        return img

    def center_text_bot(img, font, text, height, color=(0, 0, 0)):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-text_width)/2,height)
        draw.text(position, text, color, font=font)
        return img

    def text_code(img, font, text, color=(0, 0, 0)):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-text_width-200)/2,9)
        draw.text(position, text, color, font=font)
        return img

    """ def text_print(img, font, text, color=(0, 0, 0)):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width+245)/2,765)
        draw.text(position, text, color, font=font, direction='rtl')
        return img """

    def text_edition(img, font, text, color=(0, 0, 0)):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-text_width+200)/2,765)
        draw.text(position, text, color, font=font)
        return img

    mycursor.execute("SELECT * FROM unique_card JOIN card_info ON unique_card.card_id = card_info.card_id WHERE unique_card.card_unique_id = '" + str(card_unique_id) + "'")
    res = mycursor.fetchone()   

    file_like= BytesIO(res["card_img"])
    background = PIL.Image.open(file_like)
    background = background.resize((500, 810))
    foreground = ""
    if res["card_edition"] == 1:
        foreground = PIL.Image.open("./borders/level1.png")
        background.paste(foreground, (0, 0), foreground)
    elif res["card_edition"] == 2:
        foreground = PIL.Image.open("./borders/level2.png")
        background.paste(foreground, (0, 0), foreground)
    elif res["card_edition"] == 3:
        foreground = PIL.Image.open("./borders/level3.png")
        background.paste(foreground, (0, 0), foreground)
    else:
        foreground = PIL.Image.open("./borders/level1.png")
        background.paste(foreground, (0, 0), foreground)


    strip_width, strip_height = 500, 810

    name_font = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 48)
    name_font2 = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 39)
    name_font3 = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 32)
    anime_font = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 51)
    anime_font2 = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 38)
    anime_font3 = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 32)
    small_font = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 28)
    if len(res["char_name"]) <= 20:
        background = center_text_top(background, name_font, res["char_name"], 65)
    elif len(res["char_name"]) > 20 and len(res["char_name"]) <= 30:
        strip_width += 20
        background = center_text_top(background, name_font2, res["char_name"], 75)
    elif len(res["char_name"]) > 30:
        background = center_text_top(background, name_font3, res["char_name"], 75)
    strip_width = 500
    if len(res["anime_origin"]) <= 20:
        background = center_text_bot(background, anime_font, res["anime_origin"],675)
    elif len(res["anime_origin"]) > 17 and len(res["anime_origin"]) <= 25:
        strip_width += 20
        background = center_text_bot(background, anime_font2, res["anime_origin"],685)
    elif len(res["anime_origin"]) > 25:
        background = center_text_bot(background, anime_font3, res["anime_origin"],685)
    strip_width = 500
    background = text_edition(background, small_font, str(res["card_edition"]) + " · " + str(res["card_print"]))
    #background = text_print(background, small_font, str(res["card_print"]))
    background = text_code(background, small_font, str(res["card_unique_id"]))

    buffer = BytesIO()     
    background.save(buffer, 'jpeg')
    buffer.seek(0)        
    bg_image = buffer         

    return bg_image

def get_custom_image_drop(card_id):
    def center_text_top(img, font, text, height, color=(0, 0, 0), ):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-text_width)/2, height)
        draw.text(position, text, color, font=font)
        return img

    def center_text_bot(img, font, text, height, color=(0, 0, 0)):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-text_width)/2,height)
        draw.text(position, text, color, font=font)
        return img

    def text_edition(img, font, text, color=(0, 0, 0)):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-text_width+200)/2,765)
        draw.text(position, text, color, font=font)
        return img

    """ def text_print(img, font, text, color=(0, 0, 0)):
        draw = ImageDraw.Draw(img)
        text_width, text_height = draw.textsize(text, font)
        position = ((strip_width-245)/2,640)
        draw.text(position, text, color, font=font)
        return img """

    mycursor.execute("SELECT * FROM card_info WHERE card_id = " + str(card_id))
    res = mycursor.fetchone()   

    file_like= BytesIO(res["card_img"])
    background = PIL.Image.open(file_like)
    background = background.resize((500, 810))
    if res["card_edition"] == 1:
        foreground = PIL.Image.open("./borders/level1.png")
    elif res["card_edition"] == 2:
        foreground = PIL.Image.open("./borders/level2.png")
    elif res["card_edition"] == 3:
        foreground = PIL.Image.open("./borders/level3.png")

    background.paste(foreground, (0, 0), foreground)

    strip_width, strip_height = 500, 810

    name_font = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 48)
    name_font2 = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 39)
    name_font3 = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 32)
    anime_font = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 51)
    anime_font2 = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 38)
    anime_font3 = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 32)
    small_font = ImageFont.truetype("./fonts/liga_sans_heavy.ttf", 28)
    if len(res["char_name"]) <= 20:
        background = center_text_top(background, name_font, res["char_name"], 65)
    elif len(res["char_name"]) > 20 and len(res["char_name"]) <= 30:
        strip_width += 20
        background = center_text_top(background, name_font2, res["char_name"], 75)
    elif len(res["char_name"]) > 30:
        background = center_text_top(background, name_font3, res["char_name"], 75)
    strip_width = 500
    if len(res["anime_origin"]) <= 20:
        background = center_text_bot(background, anime_font, res["anime_origin"],675)
    elif len(res["anime_origin"]) > 20 and len(res["anime_origin"]) <= 30:
        strip_width += 20
        background = center_text_bot(background, anime_font2, res["anime_origin"],685)
    elif len(res["anime_origin"]) > 30:
        background = center_text_bot(background, anime_font3, res["anime_origin"],685)
    strip_width = 500
    background = text_edition(background, small_font, str(res["card_edition"]) + " · #" + str(res["card_total_count"] + 1))
    #background = text_print(background, small_font, str(res["card_total_count"] + 1))

    buffer = BytesIO()     
    background.save(buffer, 'jpeg')
    buffer.seek(0)        
    bg_image = buffer         

    return bg_image

def get_args(message):
        return message.split()

ImageFile.LOAD_TRUNCATED_IMAGES = True
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="oni-cards",
    use_unicode=True,
    charset="utf8mb4",
    collation='utf8mb4_general_ci',)
mydb.set_charset_collation('utf8mb4', 'utf8mb4_general_ci')

mycursor = mydb.cursor(dictionary=True, buffered=True)
print('We have logged into MySQL')

client = discord.Client()
my_secret = "MTAwMTU1MjYyMjgyNzg2NDEwNA.G_52Aq.TF14t_PIGFJQ70GNd4ShQxNsPJTmPQm3WDKf-U"

@client.event
async def on_ready():
    print('We have logged into Discord as {0.user}'.format(client))

@client.event
async def on_message(message):
    userExists = True
    if message.author == client.user:
        return

    """ Oni.Verify """

    if get_args(message.content)[0] == 'overify':
        words = requests.get("https://random-word-api.herokuapp.com/word?number=5")
        user_secret = words.json()[0] + " " + words.json()[1] + " " + words.json()[2] + " " + words.json()[3] + " " + words.json()[4]
        mycursor.execute("SELECT COUNT(user.user_uid) as count FROM user WHERE user.user_uid = '" + str(message.author.id) + "'")
        userCheck = mycursor.fetchone()
        if userCheck["count"] == 1:
            await message.channel.send("<@" + str(message.author.id) + "> you are already verified.")
            return
        else:
            await message.channel.send("<@" + str(message.author.id) + "> please repeat the following words: " + user_secret)
            res = await client.wait_for(
            "message",
            check=lambda x: x.channel.id == message.channel.id
            and message.author.id == x.author.id
            and x.content.lower() == user_secret
            or x.content.lower() == user_secret,
            timeout=None
        )

        if res.content.lower() == user_secret:
            mycursor.execute("INSERT INTO user (user_uid) VALUES (" + str(message.author.id) + ")")
            mycursor.execute("INSERT INTO inv (user_uid) VALUES (" + str(message.author.id) + ")")
            mydb.commit()
            await message.channel.send("Great! " + "<@" + str(message.author.id) + "> you are now verified! Have fun!")

    """ Oni.Verify Check """

    if message.content.startswith('o'):
        mycursor.execute("SELECT COUNT(user.user_uid) as count FROM user WHERE user.user_uid = '" + str(message.author.id) + "'")
        userCheck = mycursor.fetchone()
        if userCheck["count"] != 1:
            userExists = False
            await message.channel.send("Please use **overify** before accessing this bot.")
            return

    """ Oni.Collection """

    if get_args(message.content)[0] == 'ocollection' or get_args(message.content)[0] == 'oc':

        async def _search(uid, f_prefix, f_arg):
            global tag_id
            tag_id = 0
            if(f_prefix == "t:"):
                mycursor.execute("SELECT tag_id FROM tags WHERE user_uid = '" + uid + "' and tag_name = '" + f_arg + "'")
                tag_id = mycursor.fetchone()["tag_id"]
                mycursor.execute("SELECT COUNT(card_unique_id) as amount FROM `unique_card` JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_tag = " + str(tag_id) + " and card_owner_id = " + str(uid) + ";")
                amount = mycursor.fetchone()["amount"]
            elif(f_prefix == "c:"):
                mycursor.execute("SELECT COUNT(card_unique_id) as amount FROM `unique_card` JOIN card_info ON unique_card.card_id = card_info.card_id WHERE char_name LIKE '%" + str(f_arg) + "%' and card_owner_id = " + str(uid) + ";")
                amount = mycursor.fetchone()["amount"]
            elif(f_prefix == "a:"):
                mycursor.execute("SELECT COUNT(card_unique_id) as amount FROM `unique_card` JOIN card_info ON unique_card.card_id = card_info.card_id WHERE anime_origin LIKE '%" + str(f_arg) + "%' and card_owner_id = " + str(uid) + ";")
                amount = mycursor.fetchone()["amount"]
            elif(f_prefix == "o:" and f_arg[0:1] == "w"):
                mycursor.execute("SELECT COUNT(card_unique_id) as amount FROM `unique_card` JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + ";")
                amount = mycursor.fetchone()["amount"]
            elif(f_prefix == "o:" and f_arg[0:1] == "p"):
                mycursor.execute("SELECT COUNT(card_unique_id) as amount FROM `unique_card` JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + ";")
                amount = mycursor.fetchone()["amount"]
            else:
                mycursor.execute("SELECT COUNT(card_unique_id) as amount FROM `unique_card` JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + ";")
                amount = mycursor.fetchone()["amount"]
            global offset
            offset = 0
            if(f_prefix == "t:"):
                mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_tag = " + str(tag_id) + " and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
            elif(f_prefix == "c:"):
                mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE char_name LIKE '%" + str(f_arg) + "%' and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
            elif(f_prefix == "a:"):
                mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE anime_origin LIKE '%" + str(f_arg) + "%' and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
            elif(f_prefix == "o:" and f_arg[0:1] == "w"):
                mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " ORDER BY card_info.card_wishlist desc LIMIT 10 OFFSET " + str(offset) + ";")
            elif(f_prefix == "o:" and f_arg[0:1] == "p"):
                mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " ORDER BY unique_card.card_print asc LIMIT 10 OFFSET " + str(offset) + ";")
            else:
                mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
            myresult = mycursor.fetchall()
            completeString = ""
            custom_add = ""
            for r in myresult:
                quality = ""
                for q in range(4):
                    if q >= r["card_quality"]:
                        quality += "☆"
                    else:
                        quality += "★"
                    
                if r["card_tag"] == 0: 
                    tag_emoji = "◾"
                else:
                    tag_emoji = r["tag_emoji"]

                if(f_prefix == "o:" and f_arg[0:1] == "w"):
                    custom_add = " `♡ " + str(r["card_wishlist"]) + "` · "

                completeString += tag_emoji + custom_add + ' **`' + r["card_unique_id"] + '`** · `' + quality + '` · `#' + str(r["card_print"]) + '` · `◈' + str(r["card_edition"]) + '` · ' + r["anime_origin"] + ' · **' + r["char_name"] + '**\n'
            
            embedVar = discord.Embed(title="Card Collection", description='Cards carried by <@' + str(uid) + '> \n \n' + completeString, color=0xffffff)
            embedVar.set_footer(text='Showing Cards 1-10')
            """ embedVar.add_field(name=completeString, value='** **', inline=False) """

            ocmsg = await message.channel.send(embed=embedVar)
            await ocmsg.add_reaction("⬅️")
            await ocmsg.add_reaction("➡️")

            def check(reaction, user):
                global _emoji
                _emoji = str(reaction.emoji)
                return user == message.author and str(reaction.emoji) == '➡️' or user == message.author and str(reaction.emoji) == '⬅️'

            t_end = time.time() + 30
            while time.time() < t_end:
                res = await client.wait_for('reaction_add', check=check)
                if res:
                    if _emoji == "⬅️":
                        if offset > 0:
                            offset -= 10
                        custom_add = ""
                        """ if offset < 0:
                            offset = 0 """
                        if(f_prefix == "t:"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_tag = " + str(tag_id) + " and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
                        elif(f_prefix == "c:"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE char_name LIKE '%" + str(f_arg) + "%' and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
                        elif(f_prefix == "a:"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE anime_origin LIKE '%" + str(f_arg) + "%' and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
                        elif(f_prefix == "o:" and f_arg[0:1] == "w"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " ORDER BY card_info.card_wishlist desc LIMIT 10 OFFSET " + str(offset) + ";")
                        elif(f_prefix == "o:" and f_arg[0:1] == "p"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " ORDER BY unique_card.card_print asc LIMIT 10 OFFSET " + str(offset) + ";")
                        else:
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
                        myresult = mycursor.fetchall()
                        completeString = ""
                        for r in myresult:
                            quality = ""
                            for q in range(4):
                                if q >= r["card_quality"]:
                                    quality += "☆"
                                else:
                                    quality += "★"
                                
                            if r["card_tag"] == 0: 
                                tag_emoji = "◾"
                            else:
                                tag_emoji = r["tag_emoji"]

                            if(f_prefix == "o:" and f_arg[0:1] == "w"):
                                custom_add = " `♡ " + str(r["card_wishlist"]) + "` · "

                            completeString += tag_emoji + custom_add + ' **`' + r["card_unique_id"] + '`** · `' + quality + '` · `#' + str(r["card_print"]) + '` · `◈' + str(r["card_edition"]) + '` · ' + r["anime_origin"] + ' · **' + r["char_name"] + '**\n'
                        _embedVar = discord.Embed(title="Card Collection", description='Cards carried by <@' + str(uid) + '> \n \n' + completeString, color=0xffffff)
                        _embedVar.set_footer(text='Showing Cards ' + str(offset + 1) + '-' + str(offset + 10))
                        await ocmsg.edit(embed=_embedVar)
                    elif _emoji == "➡️":
                        if offset <= amount - 10:
                            offset += 10
                        custom_add = ""
                        if(f_prefix == "t:"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_tag = " + str(tag_id) + " and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
                        elif(f_prefix == "c:"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE char_name LIKE '%" + str(f_arg) + "%' and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
                        elif(f_prefix == "a:"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE anime_origin LIKE '%" + str(f_arg) + "%' and card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
                        elif(f_prefix == "o:" and f_arg[0:1] == "w"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " ORDER BY card_info.card_wishlist desc LIMIT 10 OFFSET " + str(offset) + ";")
                        elif(f_prefix == "o:" and f_arg[0:1] == "p"):
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " ORDER BY unique_card.card_print asc LIMIT 10 OFFSET " + str(offset) + ";")
                        else:
                            mycursor.execute("SELECT * FROM `unique_card` LEFT JOIN tags ON unique_card.card_tag = tags.tag_id JOIN card_info ON unique_card.card_id = card_info.card_id WHERE card_owner_id = " + str(uid) + " LIMIT 10 OFFSET " + str(offset) + ";")
                        myresult = mycursor.fetchall()
                        completeString = ""
                        for r in myresult:
                            quality = ""
                            for q in range(4):
                                if q >= r["card_quality"]:
                                    quality += "☆"
                                else:
                                    quality += "★"
                                
                            if r["card_tag"] == 0: 
                                tag_emoji = "◾"
                            else:
                                tag_emoji = r["tag_emoji"]

                            if(f_prefix == "o:" and f_arg[0:1] == "w"):
                                custom_add = " `♡ " + str(r["card_wishlist"]) + "` · "

                            completeString += tag_emoji + custom_add + ' **`' + r["card_unique_id"] + '`** · `' + quality + '` · `#' + str(r["card_print"]) + '` · `◈' + str(r["card_edition"]) + '` · ' + r["anime_origin"] + ' · **' + r["char_name"] + '**\n'
                        _embedVar = discord.Embed(title="Card Collection", description='Cards carried by <@' + str(uid) + '> \n \n' + completeString, color=0xffffff)
                        _embedVar.set_footer(text='Showing Cards ' + str(offset + 1) + '-' + str(offset + 10))
                        await ocmsg.edit(embed=_embedVar)

        async def valid_arg(uid, pref, arg):
            if pref == "o:" and arg == "w" or pref == "o:" and arg == "wishlist" or pref == "o:" and arg == "p" or pref == "o:" and arg == "print":
                return True
            elif pref == "t:" and arg:
                mycursor.execute("SELECT COUNT(tag_id) AS amount FROM tags WHERE user_uid = '" + uid + "' and tag_name = '" + arg + "'")
                amount = mycursor.fetchone()["amount"]
                if amount > 0:
                    return True
                else:
                    return False
            elif pref == "c:" and arg:
                mycursor.execute("SELECT COUNT(unique_card.card_id) AS amount FROM unique_card JOIN card_info ON card_info.card_id = unique_card.card_id WHERE unique_card.card_owner_id = '" + uid + "' and card_info.char_name LIKE '%" + arg + "%'")
                amount = mycursor.fetchone()["amount"]
                if amount > 0:
                    return True
                else:
                    return False
            elif pref == "a:" and arg:
                mycursor.execute("SELECT COUNT(unique_card.card_id) AS amount FROM unique_card JOIN card_info ON card_info.card_id = unique_card.card_id WHERE unique_card.card_owner_id = '" + uid + "' and card_info.anime_origin LIKE '%" + arg + "%'")
                amount = mycursor.fetchone()["amount"]
                if amount > 0:
                    return True
                else:
                    return False
            else:
                return False
            
        args = get_args(message.content)

        valid_pref = ["o:", "t:", "c:", "a:"]

        if len(args) > 2: 
            if args[1][0:2] in valid_pref:                                                                #User and Filter 
                user = args[2]
                user = args[2][args[2].index('@')+1:args[2].index('>')]
                filter_prefix = args[1][0:2]
                filter_arg = args[1][2:]
                if not await valid_arg(user, filter_prefix, filter_arg):
                    await message.channel.send("Invalid Filter.")
                    return
                await _search(user, filter_prefix, filter_arg)

        elif len(args) > 1:             
            if '@' in args[1]:                                                                              #Only User
                user = args[1][args[1].index('@')+1:args[1].index('>')]
                await _search(user, None, None)

            elif args[1][0:2] in valid_pref:                                                                    #Only Filter
                filter_prefix = args[1][0:2]
                filter_arg = args[1][2:]
                user = str(message.author.id)
                if not await valid_arg(user, filter_prefix, filter_arg):
                    await message.channel.send("Invalid Filter.")
                    return
                await _search(user, filter_prefix, filter_arg)

        else:                                                           #None
            user = str(message.author.id)
            await _search(user, None, None)

    """ Oni.View """

    if get_args(message.content)[0] == 'oview' or get_args(message.content)[0] == 'ov':
        async def sendCard(myres, id):
            quality = ""
            for q in range(4):
                if q >= myres["card_quality"]:
                    quality += "☆"
                else:
                    quality += "★"

            embedVar = discord.Embed(title="Card-Details", description='Owned by <@' + myres["card_owner_id"] + '> \n \n `' + myres["card_unique_id"] + '` **·** `' + quality + '` **·** `#' + str(myres["card_print"]) + '` **·** `◈' + str(myres["card_edition"]) + '` **·** ' + str(myres["anime_origin"]) + ' **·** **' + str(myres["char_name"]) + '**', color=0xffffff)      

            mycursor.execute("UPDATE user SET last_card = '" + str(myres["card_unique_id"]) + "' WHERE user_uid = '" + str(message.author.id) + "'")
            mydb.commit()

            if str(message.author.id) == str(myres["card_owner_id"]):
                mycursor.execute("UPDATE user SET last_own_card = '" + str(myres["card_unique_id"]) + "' WHERE user_uid = '" + str(message.author.id) + "'")
                mydb.commit()

            file = discord.File(get_custom_image(id), filename="image.png")
            embedVar.set_image(url="attachment://image.png")
            await message.reply(file=file, embed=embedVar, mention_author=False)

        args = get_args(message.content)

        if len(args) > 1:
            viewcode = str(args[1])
        else:
            viewcode = ""
        mycursor.execute("SELECT u.card_unique_id, u.card_id, u.card_quality, u.card_print, c.card_edition, c.char_name, c.anime_origin, u.card_custom_image as cimg, u.card_owner_id FROM unique_card u JOIN card_info c ON u.card_id = c.card_id WHERE u.card_unique_id = '" + viewcode + "';")
        myresult = mycursor.fetchone()
        if myresult == None:
            mycursor.execute("SELECT last_card from user WHERE user_uid = " + str(message.author.id))
            last_id = mycursor.fetchone()["last_card"]
            if(last_id != "000000" and not viewcode):
                mycursor.execute("SELECT u.card_unique_id, u.card_id, u.card_quality, u.card_print, c.card_edition, c.char_name, c.anime_origin, u.card_custom_image as cimg, u.card_owner_id FROM unique_card u JOIN card_info c ON u.card_id = c.card_id WHERE u.card_unique_id = '" + last_id + "';")
                myresult = mycursor.fetchone()
                if myresult == None:
                    await message.channel.send('No Card found.')
                else:
                    await sendCard(myresult, last_id)
            else:
                await message.channel.send('No Card found.')
        else:
            await sendCard(myresult, viewcode)
    
    """ Oni.Lookup """

    if get_args(message.content)[0] == 'olookup' or get_args(message.content)[0] == 'olu':
        lookupterm = str(message.content)[len(get_args(message.content)[0]) + 1:]
        if not lookupterm:
            mycursor.execute("SELECT last_card FROM user WHERE user_uid = " + str(message.author.id))
            last_card = mycursor.fetchone()["last_card"]
            if last_card != "000000":
                mycursor.execute("SELECT * FROM unique_card JOIN card_info ON card_info.card_id = unique_card.card_id WHERE card_unique_id = '" + str(last_card) + "'")
                a = mycursor.fetchone()
                if not a:
                    await message.channel.send('Non valid search term!')
                    return
                else:
                    lookupterm = a["char_name"]
        #V1 Searching mycursor.execute("select * from card_info where char_name like '%" + lookupterm + "%' order by locate('" + lookupterm + "', char_name) asc, char_name asc LIMIT 10 OFFSET 0;")
        mycursor.execute("select * from card_info where char_name like '%" + lookupterm + "%' or anime_origin like '%" + lookupterm + "%' order by card_wishlist desc, locate('" + lookupterm + "', anime_origin) asc, locate('" + lookupterm + "', char_name) desc, char_name asc LIMIT 10 OFFSET 0;")
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            await message.channel.send('No Characters found by Term: **' + lookupterm + '**')
            return
        elif len(lookupterm) == 0:
            await message.channel.send('Non valid search term!')
            return
        elif len(myresult) == 1:
            #V1 Searching mycursor.execute("select * from card_info where char_name like '%" + lookupterm + "%' order by locate('" + lookupterm + "', char_name) asc, char_name asc;")           
            mycursor.execute("select * from card_info where char_name like '%" + lookupterm + "%' or anime_origin like '%" + lookupterm + "%' order by card_wishlist desc, locate('" + lookupterm + "', anime_origin) asc, locate('" + lookupterm + "', char_name) desc, char_name asc; ")
            charresult = mycursor.fetchone()
            _embedVar = discord.Embed(title="Character Lookup", description='\n \n Character · **' + charresult["char_name"] + '**\n Anime · **' + charresult["anime_origin"] + '**\n Wishlisted · **' + str(charresult["card_wishlist"]) + '** \n \n Total Generated · **' + str(charresult["card_generated"]) + '**\n Total claimed · **' + str(charresult["card_total_count"]) + '**\n Total in circulation · **' + str(charresult["card_used"]) + '**', color=0xffffff)            
            file_like= BytesIO(charresult["card_img"])
            img = PIL.Image.open(file_like)

            buffer = BytesIO(charresult["card_img"])     
            img.save(buffer, 'jpeg') 
            buffer.seek(0)        
            bg_image = buffer         

            file = discord.File(bg_image, filename="image.png")
            _embedVar.set_thumbnail(url="attachment://image.png")

            await message.channel.send(file=file, embed=_embedVar)
        else:
            embedVar = discord.Embed(title="Character Results", description='<@' + str(message.author.id) + '>, please select a character by typing a number from 1-10.', color=0xffffff)
            completeString = ""
            for r in range(len(myresult)):
                completeString += str(r + 1) + ". `♡ " + str(myresult[r]["card_wishlist"]) + "` **·** " + myresult[r]["anime_origin"] + " **·** **" + myresult[r]["char_name"] + "**\n"
            embedVar.add_field(name="Showing Characters 1-10", value=completeString, inline=False)
            await message.channel.send(embed=embedVar)
            
            def check(m):
                global ses 
                ses = m.content
                return True
            
            msg = await client.wait_for('message', check=check, timeout=None)
            
            if ses in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                mycursor.execute("select * from card_info where char_name like '%" + lookupterm + "%' order by locate('" + lookupterm + "', char_name) asc, char_name asc LIMIT 1 OFFSET " + str(int(ses) - 1) + ";")
                charresult = mycursor.fetchone()
                _embedVar = discord.Embed(title="Character Lookup", description='\n \n Character · **' + charresult["char_name"] + '**\n Anime · **' + charresult["anime_origin"] + '**\n Wishlisted · **' + str(charresult["card_wishlist"]) + '** \n \n Total Generated · **' + str(charresult["card_generated"]) + '**\n Total claimed · **' + str(charresult["card_total_count"]) + '**\n Total in circulation · **' + str(charresult["card_used"]) + '**', color=0xffffff)

                
                file_like= BytesIO(charresult["card_img"])
                img = PIL.Image.open(file_like)

                buffer = BytesIO(charresult["card_img"])     
                img.save(buffer, 'jpeg') 
                buffer.seek(0)        
                bg_image = buffer         

                file = discord.File(bg_image, filename="image.png")
                _embedVar.set_thumbnail(url="attachment://image.png")

                await message.channel.send(file=file, embed=_embedVar)

    """ Oni.Drop """

    if get_args(message.content)[0] == 'odrop' or get_args(message.content)[0] == 'od':
        mycursor.execute("SELECT last_drop FROM user WHERE user_uid = " + str(message.author.id) + "; ")
        myresult = mycursor.fetchone()

        dt = datetime.now().replace(microsecond=0)
        ld = myresult["last_drop"]
        nd = ld + timedelta(0,0,0,0,15)

        time_interval = ""
        
        time_interval_minutes = (nd - dt).total_seconds() / 60.0
        if time_interval_minutes > 1:
            time_interval = "`" + str(math.floor(time_interval_minutes)) + " minutes`"
        else:
            time_interval = "`" + str(int((nd - dt).total_seconds())) + " seconds`"

        if nd >= dt:
            await message.channel.send("<@" + str(message.author.id) + "> you have to wait another " + str(time_interval) + " before dropping cards!")
        else:
            mycursor.execute("SELECT * FROM card_amount")
            cardamount = mycursor.fetchone()["amount"]
            randomlist = []
            cards = []
            for i in range(3):
                n = random.randint(0, cardamount - 1)
                mycursor.execute("SELECT * from card_info LIMIT 1 OFFSET " + str(n))
                randomlist.append(n)
                cards.append(mycursor.fetchone())

            list_im = []
            test = []
            for m in range(3):
                mycursor.execute("UPDATE card_info SET card_generated = card_generated + 1 WHERE card_id = " + str(cards[m]["card_id"]))
                mydb.commit()
                file_like = BytesIO(cards[m]["card_img"])
                list_im.append(file_like)
                test.append(get_custom_image_drop(cards[m]["card_id"]))

            images = [PIL.Image.open(x) for x in list_im]
            images = [PIL.Image.open(x) for x in test]
            widths, heights = zip(*(i.size for i in images))

            total_width = sum(widths)
            max_height = max(heights)

            new_im = PIL.Image.new('RGBA', (total_width + 100, max_height), (255, 0, 0, 0))

            x_offset = -50
            l = 0
            for im in images:
                x_offset += 50
                new_im.paste(im, (x_offset,0))
                x_offset += im.size[0]
                l += 1

            buf = io.BytesIO()
            new_im.save(buf, format='PNG')
            buf.seek(0)    
            byte_im = buf

            file = discord.File(byte_im, filename="image.png")

            drop_msg = await message.channel.send("<@" + str(message.author.id) + "> is dropping 3 cards!", file=file)
            await drop_msg.add_reaction("1️⃣")
            await drop_msg.add_reaction("2️⃣")
            await drop_msg.add_reaction("3️⃣")
            time.sleep(1)
            global _emoji
            
            def check(reaction, user):
                global _emoji
                _emoji = str(reaction.emoji)
                return user == message.author and str(reaction.emoji) == '1️⃣' or user == message.author and str(reaction.emoji) == '2️⃣' or user == message.author and str(reaction.emoji) == '3️⃣'

            try:
                time.sleep(0.5)
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                time.sleep(0.5)
            except asyncio.TimeoutError:
                old_drop = await message.channel.fetch_message(drop_msg.id)
                await old_drop.edit(content= drop_msg.content + "\n *This drop is expired and no cards can be picked up anymore.*")
            else:
                if _emoji == '1️⃣':
                    _emoji = 0
                elif _emoji == '2️⃣':
                    _emoji = 1
                elif _emoji == '3️⃣':
                    _emoji = 2
                else:
                    await message.channel.send('Sorry, there has been an error while collecting your card. Please contact the support to get help.')
                    return
                old_drop = await message.channel.fetch_message(drop_msg.id)
                await old_drop.edit(content= drop_msg.content + "\n *This drop is used and no cards can be picked up anymore.*")
                card = cards[_emoji]

                def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
                    i = 1
                    while i < 2:
                        id = ''.join(random.choice(chars) for _ in range(size)).lower()
                        mycursor.execute("SELECT COUNT(card_unique_id) as count FROM unique_card WHERE card_unique_id = '" + str(id) + "'")
                        amount = mycursor.fetchone()["count"]
                        if(amount < 1):
                            i = 2
                            return id
                
                def print_counter(card_id):
                    mycursor.execute("SELECT card_total_count FROM card_info WHERE card_id = " + str(card_id))
                    count = mycursor.fetchone()["card_total_count"]
                    mycursor.execute("UPDATE card_info SET card_used = card_used + 1, card_total_count = card_total_count + 1 WHERE card_id = " + str(card_id))
                    mydb.commit()
                    return count + 1

                unique_id = id_generator()
                card_quality = random.randint(0,4)
                card_print = print_counter(card["card_id"])
                
                file_like= BytesIO(card["card_img"])
                img = PIL.Image.open(file_like)

                stream = io.BytesIO()
                img.save(stream, format="JPEG")

                imagebytes = stream.getvalue()

                sql = """INSERT INTO unique_card (card_unique_id, card_id, card_quality, card_print, card_custom_image, card_owner_id) VALUES ('""" + str(unique_id) + """', """ + str(card["card_id"]) + """, """ + str(card_quality) + """, """ + str(card_print) + """, %s, """ + str(message.author.id) + """)"""
                mycursor.execute(sql, (imagebytes,))
                mydb.commit()
                mycursor.execute("UPDATE user SET last_drop=now() WHERE user_uid = " + str(message.author.id))
                mydb.commit()
                mycursor.execute("UPDATE user SET last_card = '" + str(unique_id) + "', last_own_card = '" + str(unique_id) + "' WHERE user_uid = '" + str(message.author.id) + "'")
                mydb.commit()
                await message.channel.send('<@' + str(message.author.id) + '> grabbed **' + card["char_name"] + '** `' + str(unique_id) + '` . It\'s quality is ' + str(card_quality) + '/4.')

    """ Oni.Inventory """

    if get_args(message.content)[0] == 'oinventory' or get_args(message.content)[0] == 'oi':
        async def open(uid):
            mycursor.execute("SELECT * FROM inv JOIN user ON user.user_uid = inv.user_uid WHERE inv.user_uid = " + str(uid))
            items = mycursor.fetchone()
            embedVar = discord.Embed(title="Inventory", description='Items carried by <@' + str(uid) + '> \n \n' +  "💰 **" + str(items["gold"]) + "** · `gold` · *Gold* \n" +  "🎟️ **" + str(items["ticket"]) + "** · `ticket` · *Ticket* \n" +  "✨ **" + str(items["damaged_dust"]) + "** · `damaged dust` · *Dust (☆☆☆☆)* \n" +  "✨ **" + str(items["poor_dust"]) + "** · `poor dust` · *Dust (★☆☆☆)* \n" +  "✨ **" + str(items["good_dust"]) + "** · `good dust` · *Dust (★★☆☆)* \n" +  "✨ **" + str(items["excellent_dust"]) + "** · `excellent dust` · *Dust (★★★☆)* \n" +  "✨ **" + str(items["mint_dust"]) + "** · `mint dust` · *Dust (★★★★)* \n" +  "💎 **" + str(items["gems"]) + "** · `gems` · *Gems* \n", color=0xffffff)
            await message.reply(embed=embedVar, mention_author=False) 
        
        args = get_args(message.content)

        user_check = message.content

        if len(args) > 1:
            if '@' in args[1]:
                user = args[1][args[1].index('@')+1:len(args[1])-1]
                await open(user)
            else:
                id = str(message.author.id)
                await open(id)
        else:
            id = str(message.author.id)
            await open(id)

    """ Oni.Wishlist """
    
    if get_args(message.content)[0] == 'owishlist' or get_args(message.content)[0] == 'owl':
        args = get_args(message.content)  

        add_check = message.content[4:7]
        remove_check = message.content[4:10]
        et_check = message.content[4:]

        if len(args) > 2:
            if args[1] == "add":
                search_term = args[2]
                mycursor.execute("select * from card_info where char_name like '%" + search_term + "%' order by locate('" + search_term + "', char_name) asc, char_name asc LIMIT 10 OFFSET 0;")
                myresult = mycursor.fetchall()
                if len(myresult) == 0:
                    await message.channel.send('No Characters found by Term: **' + search_term + '**')
                    return
                elif len(search_term) == 0:
                    await message.channel.send('Non valid search term!')
                    return
                elif len(myresult) == 1:
                    mycursor.execute("select * from card_info where char_name like '%" + search_term + "%' order by locate('" + search_term + "', char_name) asc, char_name asc;")
                    charresult = mycursor.fetchone()

                    mycursor.execute("SELECT COUNT(card_id) as c FROM wishlist WHERE user_uid = '" + str(message.author.id) + "' and card_id = " + str(charresult["card_id"]))
                    mydouble = mycursor.fetchone()["c"]
                    if mydouble > 0:
                        await message.reply("This character is already on your wishlist!", mention_author=False)
                        return

                    mycursor.execute("SELECT COUNT(user_uid) as amount FROM wishlist WHERE user_uid = '" + str(message.author.id) + "'")
                    myamount = mycursor.fetchone()["amount"]
                    
                    if myamount >= 10:
                        await message.reply("You can not have more than 10 Cards on your wishlist!", mention_author=False)
                        return

                    mycursor.execute("INSERT INTO wishlist (user_uid, card_id) VALUES ('" + str(message.author.id) + "', " + str(charresult["card_id"]) + ")")
                    mydb.commit()

                    mycursor.execute("UPDATE card_info SET card_wishlist = card_wishlist + 1 WHERE card_id = " + str(charresult["card_id"]))
                    mydb.commit()

                    await message.reply("`" + charresult["anime_origin"] + " · " + charresult["char_name"] + "` has been was added to your wishlist.", mention_author=False)
                else:
                    embedVar = discord.Embed(title="Character Results", description='<@' + str(message.author.id) + '>, please select a character by typing a number from 1-10.', color=0xffffff)
                    completeString = ""
                    for r in range(len(myresult)):
                        completeString += str(r + 1) + ". `♡ " + str(myresult[r]["card_wishlist"]) + "` **·** " + myresult[r]["anime_origin"] + " **·** **" + myresult[r]["char_name"] + "**\n"
                    embedVar.add_field(name="Showing Characters 1-10", value=completeString, inline=False)
                    await message.channel.send(embed=embedVar)
                    
                    def check(m):
                        global ses 
                        ses = m.content
                        return True
                    
                    msg = await client.wait_for('message', check=check, timeout=None)
                    
                    if ses in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                        mycursor.execute("select * from card_info where char_name like '%" + search_term + "%' order by locate('" + search_term + "', char_name) asc, char_name asc LIMIT 1 OFFSET " + str(int(ses) - 1) + ";")
                        charresult = mycursor.fetchone()

                        mycursor.execute("SELECT COUNT(card_id) as c FROM wishlist WHERE user_uid = '" + str(message.author.id) + "' and card_id = " + str(charresult["card_id"]))
                        mydouble = mycursor.fetchone()["c"]
                        if mydouble > 0:
                            await message.reply("This character is already on your wishlist!", mention_author=False)
                            return

                        mycursor.execute("SELECT COUNT(user_uid) as amount FROM wishlist WHERE user_uid = '" + str(message.author.id) + "'")
                        myamount = mycursor.fetchone()["amount"]

                        if myamount >= 10:
                            await message.reply("You can not have more than 10 Cards on your wishlist!", mention_author=False)
                            return

                        mycursor.execute("INSERT INTO wishlist (user_uid, card_id) VALUES ('" + str(message.author.id) + "', " + str(charresult["card_id"]) + ")")
                        mydb.commit()

                        mycursor.execute("UPDATE card_info SET card_wishlist = card_wishlist + 1 WHERE card_id = " + str(charresult["card_id"]))
                        mydb.commit()
                        
                        await message.reply("`" + charresult["anime_origin"] + " · " + charresult["char_name"] + "` has been added to your wishlist.", mention_author=False)
            elif args[1] == "remove":
                search_term = args[2]
                mycursor.execute("SELECT * FROM wishlist JOIN card_info ON wishlist.card_id = card_info.card_id WHERE wishlist.user_uid = '" + str(message.author.id) + "' and card_info.char_name Like '%" + search_term + "%' order by locate('" + search_term + "', card_info.char_name) asc, card_info.char_name asc")
                res = mycursor.fetchone()
                if(res):
                    mycursor.execute("UPDATE card_info SET card_wishlist = card_wishlist - 1 WHERE card_id = " + str(res["card_id"]))
                    mydb.commit()

                    mycursor.execute("DELETE FROM wishlist WHERE wish_id = " + str(res["wish_id"]))
                    await message.reply("`" + res["anime_origin"] + " · " + res["char_name"] + "` has been removed from your wishlist.", mention_author=False)
                else:
                    await message.reply("There was no card found on your wishlist, using this search term.", mention_author=False)
        elif len(args) > 1:
            if '@' in args[1]:
                user = args[1][args[1].index('@')+1:len(args[1])-1]
                mycursor.execute("SELECT * FROM wishlist JOIN card_info ON wishlist.card_id = card_info.card_id WHERE user_uid = '" + str(user) + "'")
                mywishes = mycursor.fetchall()
                if(len(mywishes) == 0):
                    await message.reply("This users wishlist is empty.", mention_author=False)
                else:
                    embedVar = discord.Embed(title="Wishlist", description='User: <@' + str(user) + '> \n Available Slots: ' + str(10 - len(mywishes))  + '/10', color=0xffffff)
                    res = ""
                    for m in range(len(mywishes)):
                        res += mywishes[m]["anime_origin"] + " · **" + mywishes[m]["char_name"] + "**"
                        if(m != len(mywishes)):
                            res += "\n"
                    embedVar.add_field(name="Wishlisted Cards:", value=res)

                    await message.reply(embed=embedVar, mention_author=False)
            else:
                mycursor.execute("SELECT * FROM wishlist JOIN card_info ON wishlist.card_id = card_info.card_id WHERE user_uid = '" + str(message.author.id) + "'")
                mywishes = mycursor.fetchall()
                if(len(mywishes) == 0):
                    await message.reply("Your wishlist is empty.", mention_author=False)
                else:
                    embedVar = discord.Embed(title="Wishlist", description='User: <@' + str(message.author.id) + '> \n Available Slots: ' + str(10 - len(mywishes))  + '/10', color=0xffffff)
                    res = ""
                    for m in range(len(mywishes)):
                        res += mywishes[m]["anime_origin"] + " · **" + mywishes[m]["char_name"] + "**"
                        if(m != len(mywishes)):
                            res += "\n"
                    embedVar.add_field(name="Wishlisted Cards:", value=res)

                    await message.reply(embed=embedVar, mention_author=False)
        else:
            mycursor.execute("SELECT * FROM wishlist JOIN card_info ON wishlist.card_id = card_info.card_id WHERE user_uid = '" + str(message.author.id) + "'")
            mywishes = mycursor.fetchall()
            if(len(mywishes) == 0):
                await message.reply("Your wishlist is empty.", mention_author=False)
            else:
                embedVar = discord.Embed(title="Wishlist", description='User: <@' + str(message.author.id) + '> \n Available Slots: ' + str(10 - len(mywishes))  + '/10', color=0xffffff)
                res = ""
                for m in range(len(mywishes)):
                    res += mywishes[m]["anime_origin"] + " · **" + mywishes[m]["char_name"] + "**"
                    if(m != len(mywishes)):
                        res += "\n"
                embedVar.add_field(name="Wishlisted Cards:", value=res)

                await message.reply(embed=embedVar, mention_author=False)

    """ Oni.Burn """

    if get_args(message.content)[0] == 'oburn' or get_args(message.content)[0] == 'ob':
        def percentage(percent, whole):
            return (percent * whole) / 100.0

        async def burn(id):
            mycursor.execute("SELECT * FROM unique_card JOIN card_info ON card_info.card_id = unique_card.card_id WHERE unique_card.card_unique_id = '" + str(id) + "'")
            card = mycursor.fetchone()
            mycursor.execute("SELECT MAX(card_info.card_wishlist) AS wsm FROM card_info")
            maxWish = mycursor.fetchone()["wsm"]
            
            wishlisted = card["card_wishlist"] + 1
            max_gold = maxWish
            if max_gold > 2000:
                max_gold = 2000
            elif max_gold < 50:
                max_gold = 50
            base_gold = 10
            if card["card_quality"] == 0:
                dust_tax = 0.65
                dust_name = "damaged_dust"
            elif card["card_quality"] == 1:
                dust_tax = 0.7
                dust_name = "poor_dust"
            elif card["card_quality"] == 2:
                dust_tax = 0.75
                dust_name = "good_dust"
            elif card["card_quality"] == 3:
                dust_tax = 0.8
                dust_name = "excellent_dust"
            else:
                dust_tax = 1
                dust_name = "mint_dust"
            wishlist_worth = (wishlisted / maxWish) * 100
            gold = math.floor((percentage(wishlist_worth, max_gold) * dust_tax) + base_gold)
            dust = 1
            dust_quality = ""
            for q in range(4):
                if q >= card["card_quality"]:
                    dust_quality += "☆"
                else:
                    dust_quality += "★"

            file = discord.File(get_custom_image(id), filename="image.png")
            embedVar = discord.Embed(title="Burn Card", description='<@' + str(message.author.id) + '>, you will receive: \n \n 💰 ' + str(gold) + ' Gold \n ✨ ' + str(dust) + ' Dust (' + str(dust_quality) + ')' +  "", color=0xffffff)
            embedVar.set_thumbnail(url="attachment://image.png")

            burnmsg = await message.reply(embed=embedVar, file=file, mention_author=False)
            await burnmsg.add_reaction('❌')
            await burnmsg.add_reaction('☑️')
            burnedit = await message.channel.fetch_message(burnmsg.id)

            def check(reaction, user):
                global _emoji
                _emoji = str(reaction.emoji)
                return user == message.author and str(reaction.emoji) == '❌' or user == message.author and str(reaction.emoji) == '☑️'

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                """ _embedVar = discord.Embed(title="Burn Card", description='<@' + str(message.author.id) + '>, you will receive: \n \n 💰 ' + str(gold) + ' Gold \n ✨ ' + str(dust) + ' Dust (' + str(dust_quality) + ')' +  " \n \n ** Card burning has been canceled. **", color=0xf23a56)
                _embedVar.set_thumbnail(url="attachment://image.png")
                await burnmsg.edit(embed=_embedVar, file=file) """
                await message.channel.send('❌')
            else:
                if _emoji == '☑️':
                    _embedVar = discord.Embed(title="Burn Card", description='<@' + str(message.author.id) + '>, you will receive: \n \n 💰 ' + str(gold) + ' Gold \n ✨ ' + str(dust) + ' Dust (' + str(dust_quality) + ')' +  " \n \n ** The card has been burned. **", color=0x03fc20)
                    _embedVar.set_thumbnail(url="attachment://image.png")

                    mycursor.execute("DELETE FROM unique_card WHERE card_unique_id = '" + id + "'")
                    mydb.commit()
                    mycursor.execute("UPDATE inv SET gold = gold + " + str(gold) + ", " + str(dust_name) + " = " + str(dust_name) + " + 1 WHERE user_uid = " + str(message.author.id) )
                    mydb.commit()
                    mycursor.execute("UPDATE card_info SET card_used = card_used - 1 WHERE card_id = " + str(card["card_id"]))
                    mydb.commit()

                    await burnedit.edit(embed=_embedVar, mention_author=False)
                else:
                    _embedVar = discord.Embed(title="Burn Card", description='<@' + str(message.author.id) + '>, you will receive: \n \n 💰 ' + str(gold) + ' Gold \n ✨ ' + str(dust) + ' Dust (' + str(dust_quality) + ')' +  " \n \n ** Card burning has been canceled. **", color=0xf23a56)
                    _embedVar.set_thumbnail(url="attachment://image.png")
                    await burnedit.edit(embed=_embedVar, mention_author=False)

        def card_exists(unique_id):
            mycursor.execute("SELECT COUNT(card_id) as amount FROM unique_card WHERE card_unique_id = '" + str(unique_id) + "' and card_owner_id = '" + str(message.author.id) + "'")
            res = mycursor.fetchone()["amount"]
            if res > 0:
                return True
            else:
                return False
        
        args = get_args(message.content)
        param = ""
        if len(args) > 1:
            param = args[1]
        if not param:
            mycursor.execute("SELECT last_own_card from user WHERE user_uid = " + str(message.author.id))
            last_id = mycursor.fetchone()["last_own_card"]
            if last_id != "000000":
                if card_exists(last_id):
                    await burn(last_id)
                else:
                    await message.reply("You don't own a card with this code.", mention_author=False)
            else:
                await message.reply("No card found.", mention_author=False)
        else:
            if card_exists(param):
                await burn(param)
            else:
                await message.reply("You don't own a card with this code: " + str(param) + ".", mention_author=False)
    
    """ Oni.Tag """

    if get_args(message.content)[0].startswith('ot'):

        args = get_args(message.content)

        if args[0] == 'otagcreate' or args[0] == "otc":
            if len(args) < 3:
                await message.channel.send("Please use the command as the following: `otagcreate *tag_name* *tag_emoji*`")
                return 
            mycursor.execute("SELECT COUNT(tag_id) as amount FROM tags WHERE user_uid = '" + str(message.author.id) + "'")
            amount = mycursor.fetchone()["amount"]
            msg = args[1]
            if amount >= 10:
                await message.channel.send("You can not have more than 10 tags.")
                return 
            tag_name = args[1]
            tag_emoji = args[2]
            if not emoji.is_emoji(tag_emoji):
                await message.channel.send("Invalid Tag Emoji.")
                return   
            elif emoji.is_emoji(tag_name):
                await message.channel.send("Invalid Tag Name.")
                return 

            unicode = str('0x0{:X}'.format(ord(tag_emoji)))
            
            mycursor.execute("SELECT * FROM tags WHERE WEIGHT_STRING(tag_emoji COLLATE 'utf8mb4_bin') = " + unicode + " and user_uid = '" + str(message.author.id) + "'")
            r = mycursor.fetchone()
            if r:
                await message.channel.send("Tag emoji is already in use.")
                return
            mycursor.execute("SELECT * FROM tags WHERE user_uid = '" + str(message.author.id) + "' and tag_name = '" + str(tag_name) + "'")
            res = mycursor.fetchall()
            if len(res) > 0:
                await message.channel.send("Tag name is already in use.")
                return
            mycursor.execute("INSERT INTO tags (user_uid, tag_name, tag_emoji) VALUES ('" + str(message.author.id) + "', '" + str(tag_name) + "', '" + str(tag_emoji) + "')")
            mydb.commit()
            await message.channel.send("Tag: **" + tag_name + "** was created.")            
        elif args[0] == 'otagdelete' or args[0] == "otd":
            if len(args) < 3:
                await message.channel.send("Please use the command as the following: `otagdelete *tag_name* *tag_emoji*`")
                return 
            arg = args[1]
            if not arg:
                await message.channel.send('Invalid Tag Name.')
                return
            mycursor.execute("SELECT tag_id FROM tags WHERE user_uid = '" + str(message.author.id) + "' and tag_name = '" + str(arg) + "'")
            tag = mycursor.fetchone()
            if not tag:
                await message.channel.send('Could not find a tag with a matching name.')
                return
            mycursor.execute("UPDATE unique_card SET card_tag = 0 WHERE card_owner_id = '" + str(message.author.id) + "' and card_tag = '" + str(tag["tag_id"]) + "'")
            mydb.commit()
            mycursor.execute("DELETE FROM tags WHERE user_uid = '" + str(message.author.id) + "' and tag_name = '" + str(arg) + "'")
            mydb.commit()
            await message.channel.send('Tag: `' + str(arg) + '` has been deleted and all cards have been untagged.')
            return
        elif args[0] == 'otagrename' or args[0] == "otr":
            if len(args) < 3:
                await message.channel.send("Please use the command as the following: `otagrename *old_tag_name* *new_tag_name*`")
                return   
            old_tag_name = args[1]
            new_tag_name = args[2]
            if emoji.is_emoji(old_tag_name) or emoji.is_emoji(new_tag_name):
                await message.channel.send("Invalid Tag Names.")
                return
            if old_tag_name == new_tag_name:
                await message.channel.send("The old and the new Tag Name can not match!")
                return
            mycursor.execute("SELECT tag_id FROM tags WHERE user_uid = '" + str(message.author.id) + "' and tag_name = '" + str(new_tag_name) + "'")
            alr_exists = mycursor.fetchone()
            if alr_exists:
                await message.channel.send('You already have a tag with the name **' + str(new_tag_name) + '**.')
                return
            mycursor.execute("SELECT tag_id FROM tags WHERE user_uid = '" + str(message.author.id) + "' and tag_name = '" + str(old_tag_name) + "'")
            tag = mycursor.fetchone()
            if not tag:
                await message.channel.send('Could not find a tag with a matching name.')
                return
            mycursor.execute("UPDATE tags SET tag_name = '" + str(new_tag_name) + "' WHERE user_uid = '" + str(message.author.id) + "' and tag_name = '" + str(old_tag_name) + "'")
            mydb.commit()
            await message.channel.send('Tag: `' + str(old_tag_name) + '` has been renamed to ' + str(new_tag_name) + '.')
            return
        elif args[0] == 'otagemoji' or args[0] == "ote":
            if len(args) < 3:
                await message.channel.send("Please use the command as the following: `otagemoji *old_emoji* *new_emoji*`")
                return   
            old_emoji = args[1]
            new_emoji = args[2]
            if not emoji.is_emoji(old_emoji) or not emoji.is_emoji(new_emoji):
                await message.channel.send("Invalid Emojis.")
                return
            if old_emoji == new_emoji:
                await message.channel.send("The old and the new Emoji can not match!")
                return
            old_unicode = str('0x0{:X}'.format(ord(old_emoji)))
            new_unicode = str('0x0{:X}'.format(ord(new_emoji)))

            mycursor.execute("SELECT * FROM tags WHERE WEIGHT_STRING(tag_emoji COLLATE 'utf8mb4_bin') = " + new_unicode + " and user_uid = '" + str(message.author.id) + "'")
            alr_exists = mycursor.fetchone()
            if alr_exists:
                await message.channel.send('You already have a tag with the emoji: ' + str(new_emoji) + '.')
                return
            mycursor.execute("SELECT * FROM tags WHERE WEIGHT_STRING(tag_emoji COLLATE 'utf8mb4_bin') = " + old_unicode + " and user_uid = '" + str(message.author.id) + "'")
            tag = mycursor.fetchone()
            if not tag:
                await message.channel.send('Could not find a tag with a matching emoji.')
                return
            mycursor.execute("UPDATE tags SET tag_emoji = '" + str(new_emoji) + "' WHERE user_uid = '" + str(message.author.id) + "' and WEIGHT_STRING(tag_emoji COLLATE 'utf8mb4_bin') = " + old_unicode)
            mydb.commit()
            await message.channel.send('Tag: `' + str(old_emoji) + '` has been renamed to `' + str(new_emoji) + '`.')
            return
        elif args[0] == 'otags' or args[0] == "ots":
            async def search(uid):
                mycursor.execute("SELECT * FROM tags WHERE tags.user_uid = '" + str(uid) + "'")
                res = mycursor.fetchall()
                if len(res) == 0:
                    await message.channel.send("No existing tags.")
                    return
                completeString = ""
                for r in range(len(res)):
                    mycursor.execute("SELECT COUNT(unique_card.card_id) as amount FROM unique_card JOIN tags ON unique_card.card_tag = tags.tag_id WHERE unique_card.card_tag = " + str(res[r]["tag_id"]))
                    amount = mycursor.fetchone()["amount"]
                    completeString += str(emoji.emojize(res[r]["tag_emoji"])) + " `" + str(res[r]["tag_name"]) + "` · **" + str(amount) + "** cards \n"

                embedVar = discord.Embed(title="Tags", description='User: <@' + str(uid) + '> \n \n' + completeString, color=0xffffff)
                await message.channel.send(embed=embedVar)
             
            if len(args) > 1:
                if '@' in args[1]:
                    user = args[1][args[1].index('@')+1:len(args[1])-1]
                    await search(user)
                else:
                    id = str(message.author.id)
                    await search(id)
            else:
                    id = str(message.author.id)
                    await search(id)
        else:
            def tag_card(tag_name, unique_id):
                mycursor.execute("SELECT tag_id FROM tags WHERE user_uid = '" + str(message.author.id) + "' and tag_name = '" + str(tag_name) + "'")
                tag_id = mycursor.fetchone()["tag_id"]
                mycursor.execute("UPDATE unique_card SET card_tag = " + str(tag_id) + " WHERE card_unique_id = '" + str(unique_id) + "' and card_owner_id = '" + str(message.author.id) + "'")
                mydb.commit()

                return

            def card_exists(unique_id):
                mycursor.execute("SELECT COUNT(card_id) as amount FROM unique_card WHERE card_unique_id = '" + str(unique_id) + "' and card_owner_id = '" + str(message.author.id) + "'")
                res = mycursor.fetchone()["amount"]
                if res > 0:
                    return True
                else:
                    return False

            def tag_exists(tag_name):
                mycursor.execute("SELECT tag_id FROM tags WHERE user_uid = '" + str(message.author.id) + "' and tag_name = '" + str(tag_name) + "'")
                tag = mycursor.fetchone()
                if not tag:
                    return False
                return True

            args = get_args(message.content)

            if len(args) < 2:
                await message.channel.send("Please use the command as the following: `otag *tag_name* *card_code*`")
                return

            card_code = ""
            tag_name = ""

            if len(args) > 2: 
                tag_name = args[1]
                card_code = args[2]
            else:
                tag_name = args[1]

            if not card_code:
                mycursor.execute("SELECT last_own_card from user WHERE user_uid = " + str(message.author.id))
                last_id = mycursor.fetchone()["last_own_card"]
                if last_id != "000000":
                    if card_exists(last_id):
                        card_code = last_id
                        if tag_exists(tag_name):
                            tag_card(tag_name, card_code)
                        else:
                            await message.reply("Could not find the given tag.", mention_author=False)
                            return
                    else:
                        await message.reply("No card selected.", mention_author=False)
                        return
                else:
                    await message.reply("No card selected.", mention_author=False)
                    return
            else:
                if card_exists(card_code):
                    if tag_exists(tag_name):
                            tag_card(tag_name, card_code)
                    else:
                        await message.reply("Could not find the given tag.", mention_author=False)
                        return
                else:
                    await message.reply("You don't own a card with this code: " + str(card_code) + ".", mention_author=False)
                    return

            await message.reply("Your card **" + str(card_code) + "** is now tagged with **" + str(tag_name) + "**.", mention_author=False)

    """ Oni.Untag """

    if get_args(message.content)[0] == 'ountag' or get_args(message.content)[0] == 'out':
        def card_exists(unique_id):
            mycursor.execute("SELECT COUNT(card_id) as amount FROM unique_card WHERE card_unique_id = '" + str(unique_id) + "' and card_owner_id = '" + str(message.author.id) + "'")
            res = mycursor.fetchone()["amount"]
            if res > 0:
                return True
            else:
                return False
        
        def untag(unique_id):
            mycursor.execute("UPDATE unique_card SET card_tag = 0 WHERE card_unique_id = '" + str(unique_id) + "'")
            mydb.commit()
            return
        
        args = get_args(message.content)

        if len(args) > 1:
            param = args[1]
        else: param = ""

        if not param:
            mycursor.execute("SELECT last_own_card from user WHERE user_uid = " + str(message.author.id))
            last_id = mycursor.fetchone()["last_own_card"]
            if last_id != "000000":
                if card_exists(last_id):
                    param = last_id
                    #
                    untag(param)
                    #
                else:
                    await message.reply("You don't own a card with this code.", mention_author=False)
                    return
            else:
                await message.reply("No card found.", mention_author=False)
                return
        else:
            if card_exists(param):
                #
                untag(param)
                #
            else:
                await message.reply("You don't own a card with this code: " + str(param) + ".", mention_author=False)
                return
        await message.reply("Your card **" + str(param) + "** is now untagged.", mention_author=False)

    """ Oni.Give """

    if get_args(message.content)[0] == 'ogive' or get_args(message.content)[0] == 'og':

        def card_exists(unique_id):
            mycursor.execute("SELECT COUNT(card_id) as amount FROM unique_card WHERE card_unique_id = '" + str(unique_id) + "' and card_owner_id = '" + str(message.author.id) + "'")
            res = mycursor.fetchone()["amount"]
            if res > 0:
                return True
            else:
                return False

        async def sendConfirmation(user, cid):
            mycursor.execute("SELECT * FROM unique_card JOIN card_info ON card_info.card_id = unique_card.card_id WHERE card_unique_id = '" + str(cid) + "'")
            card = mycursor.fetchone()

            quality = ""
            for q in range(4):
                if q >= card["card_quality"]:
                    quality += "☆"
                else:
                    quality += "★"

            _embedVar = discord.Embed(title="Card Transfer", description='\n <@' + str(message.author.id) + '> → <@' + str(user) + '> \n \n `' + card["card_unique_id"] + '` · `' + str(quality) + '` · `#' + str(card["card_print"]) + '` · `◈' + str(card["card_edition"]) + '` · ' + card["anime_origin"] + " · **" + card["char_name"] + "**", color=0xffffff)                 

            file = discord.File(get_custom_image(cid), filename="image.png")
            _embedVar.set_image(url="attachment://image.png")

            msg = await message.channel.send(file=file, embed=_embedVar)

            await msg.add_reaction("❌")
            await msg.add_reaction("✅")

            def check(reaction, _user):
                global _emoji
                _emoji = str(reaction.emoji) 
                return _user == message.author and str(reaction.emoji) == '✅' or _user == message.author and str(reaction.emoji) == '❌' or str(user) == str(_user.id) and str(reaction.emoji) == '✅' or str(user) == str(_user.id) and str(reaction.emoji) == '❌'

            t_end = time.time() + 60
            while time.time() < t_end:
                res, r_user = await client.wait_for('reaction_add', check=check, timeout=60.0)
                if res: 
                    if _emoji == "❌":
                        __embedVar = discord.Embed(title="Card Transfer", description='\n <@' + str(message.author.id) + '> → <@' + str(user) + '> \n \n `' + card["card_unique_id"] + '` · `' + str(quality) + '` · `#' + str(card["card_print"]) + '` · `◈' + str(card["card_edition"]) + '` · ' + card["anime_origin"] + " · **" + card["char_name"] + "**", color=0xf23a56)                 

                        file = discord.File(get_custom_image(cid), filename="image.png")
                        __embedVar.set_image(url="attachment://image.png")

                        await msg.edit(embed=__embedVar)
                        break;
                    elif _emoji == "✅":
                        getmsg = await message.channel.fetch_message(msg.id)
                        users = await getmsg.reactions[1].users().flatten()
                        user_ids = [x.id for x in users] 
                        if message.author.id in user_ids and int(user) in user_ids:
                            __embedVar = discord.Embed(title="Card Transfer", description='\n <@' + str(message.author.id) + '> → <@' + str(user) + '> \n \n `' + card["card_unique_id"] + '` · `' + str(quality) + '` · `#' + str(card["card_print"]) + '` · `◈' + str(card["card_edition"]) + '` · ' + card["anime_origin"] + " · **" + card["char_name"] + "**", color=0x03fc20)                 

                            file = discord.File(get_custom_image(cid), filename="image.png")
                            __embedVar.set_image(url="attachment://image.png")

                            await msg.edit(embed=__embedVar)

                            mycursor.execute("UPDATE unique_card SET card_owner_id = " + user + " WHERE card_unique_id = '" + str(cid) + "'")
                            mydb.commit()

                            await message.channel.send("<@" + user + "> has recieved the card: `" + cid + "`")

        args = get_args(message.content)
        
        if len(args) < 3:
            await message.channel.send("Please use the command as the following: `ogive *card_id* *user*`")
            return

        if card_exists(args[1]):
            if('@' in args[2]):
                user = args[2][args[2].index('@')+1:len(args[2])-1]
                await sendConfirmation(user, args[1])
            else:
                await message.channel.send("Please use the command as the following: `ogive *card_id* *user*`")
                return
        else:
            await message.channel.send("You do not own this card: `" + str(args[1]) + "`")
            return

    if get_args(message.content)[0] == 'ohelp':
        user = await client.fetch_user(message.author.id)
        _embedVar = discord.Embed(title="Oni-Cards Commands", description="To see more details about a particular command just type it and you will see how to use it.", color=0xffffff) 

        _embedVar.add_field(name="🃏 Basic", value="`drop`, `daily`, `upgrade`, `burn`, `multiburn`")  
        _embedVar.add_field(name="📖 Collection", value="`collection`, `view`, `tags`, `tagcreate`, `tagdelete`, `tagrename`, `tagemoji`, `tag`, `untag`, `inventory`")    
        _embedVar.add_field(name="ℹ Information", value="`cooldowns`, `reminders`, `lookup`")                
        _embedVar.add_field(name="🤞 Wishlist", value="`wishlist`, `wishlist add`, `wishlist delete`")      
        _embedVar.add_field(name="💱 Trade", value="`give`, `trade`")  
        _embedVar.add_field(name="❓ Other", value="`private`, `help`")  

        await user.send(embed=_embedVar)

client.run(my_secret)