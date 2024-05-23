from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import random


api_id = 26132191
api_hash = '1087750b408944ecbe7613c8f680b1dc'


from time import sleep

app = Client(name="myaccount", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    """typing_symbol2 = """
    """end_symbol = """

    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("s1mple", prefixes=".") & filters.me)

def simple(me, voice): 
    app.send_voice("@javochat", "simple.ogg")

@app.on_message(filters.command("simple", prefixes=".") & filters.me)

def simple(me, voice): 
    app.send_voice("@javochat", "simple.ogg")






@app.on_message(filters.command("timing", prefixes=".") & filters.me)

 
def timing(_, msg): 
    msg.edit(app.send_voice("@javochat", "timing.ogg"))


@app.on_message(filters.command("lastpeek", prefixes=".") & filters.me)

 
def timing(_, msg): 
    msg.edit(app.send_voice("@javochat", "lastpeek.ogg"))


@app.on_message(filters.command("huesos", prefixes=".") & filters.me)

 
def timing(me, voice): 
    app.send_voice("@javochat", "huesos.ogg")




@app.on_message(filters.command("kysokderma", prefixes=".") & filters.me)

def timing(me, voice): 
    app.send_voice("@javochat", "kysokderma.ogg")




@app.on_message(filters.command("ugaraete", prefixes=".") & filters.me)

def timing(me, voice): 
    app.send_voice("@javochat", "ugaraete.ogg")
    
    
@app.on_message(filters.command("neterplu", prefixes=".") & filters.me)

def timing(me, voice): 
    app.send_voice("@javochat", "neterplu.ogg")

@app.on_message(filters.command("bilabimat", prefixes=".") & filters.me)

def timing(me, voice): 
    app.send_voice("@javochat", "bilabimat.ogg")


@app.on_message(filters.command("bears", prefixes=".") & filters.me)

 
def timing(me, voice): 
    app.send_voice("@javochat", "3bears.ogg")




@app.on_message(filters.command("simplePhonk", prefixes=".") & filters.me)

def simplePhonk(me, voice): 
    app.send_voice("@javochat", "simplePhonk.ogg")

@app.on_message(filters.command("s1mplePhonk", prefixes=".") & filters.me)

def simplePhonk(me, voice): 
    app.send_voice("@javochat", "simplePhonk.ogg")

@app.on_message(filters.command("ivanzolo2004", prefixes=".") & filters.me)

def simplePhonk(me, voice): 
    app.send_voice("@javochat", "ivanzolo.ogg")
    
@app.on_message(filters.command("IswareIwould", prefixes=".") & filters.me)

def simplePhonk(me, voice): 
    app.send_voice("@javochat", "isware.ogg")

@app.on_message(filters.command("passenger", prefixes=".") & filters.me)

def passenger(me, voice): 
    app.send_voice("@javochat", "passenger.ogg")



@app.on_message(filters.command("mycommands", prefixes=".") & filters.me)
def mycommands(_, msg):
    app.send_message("@javochat", "\n"+".s1mple"+"\n"+".simple"+"\n"+".timing"+"\n"+".lastpeek"+"\n"+".huesos"+"\n"+".kysokderma"+"\n"+".ugaraete"+"\n"+".neterplu"+"\n"+".bilabimat"+"\n"+".bears"+"\n"+".simplePhonk"+"\n"+".ivanzolo2004"+"\n"+".IswareIwould"+"\n"+".passenger"+"\n"+".love"+"\n"+".loved"+"\n"+".vault"+"\n"+".temagay"+"\n"+".rwqgay");


@app.on_message(filters.command("love", prefixes=".") & filters.me)
def type(_, msg):
    first_text ="❤️💜💛💚"
    text1 = first_text
    edit_text= ""
    redHeart = "❤️"
    purpleHeart = "💜"
    yellowHeart = "💛"
    greenHeart = "💚"

    
    """typing_symbol2 = """
    """end_symbol = """

    while(edit_text != first_text):
        try:
            msg.edit(edit_text + redHeart)
            sleep(0.5)

            msg.edit(edit_text + purpleHeart)
            sleep(0.5)

            msg.edit(edit_text + yellowHeart)
            sleep(0.5)

            msg.edit(edit_text + greenHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart + purpleHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart + purpleHeart + yellowHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart)
            sleep(0.5)

            msg.edit(edit_text + purpleHeart)
            sleep(0.5)

            msg.edit(edit_text + yellowHeart)
            sleep(0.5)

            msg.edit(edit_text + greenHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart + purpleHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart + purpleHeart + yellowHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart)
            sleep(0.5)

            msg.edit(edit_text + purpleHeart)
            sleep(0.5)

            msg.edit(edit_text + yellowHeart)
            sleep(0.5)

            msg.edit(edit_text + greenHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart + purpleHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart + purpleHeart + yellowHeart)
            sleep(0.5)
            '''break'''
            """edit_text = edit_text + text1[0]
            text1 = text1[1:]

            msg.edit(edit_text)
            sleep(0.1)
"""
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("loved", prefixes=".") & filters.me)
def type(_, msg):
    first_text ="❤️"

    text1 = first_text
    text_line1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    text_line2 = "🤍🤍💚💚🤍💚💚🤍🤍"
    text_line3 = "🤍💚💚💚💚💚💚💚🤍"
    text_line4 = "🤍💚💚💚💚💚💚💚🤍"
    text_line5 = "🤍💚💚💚💚💚💚💚🤍"
    text_line6 = "🤍🤍💚💚💚💚💚🤍🤍"
    text_line7 = "🤍🤍🤍💚💚💚🤍🤍🤍"
    text_line8 = "🤍🤍🤍🤍💚🤍🤍🤍🤍"
    text_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    
    edit_text ="\n" + text_line1 + "\n" + text_line2 + "\n" + text_line3 + "\n" + text_line4 + "\n" + text_line5 + "\n" + text_line6 + "\n" + text_line7 + "\n" + text_line8 + "\n" + text_line9 + "\n"
    redHeart = "❤️"
    purpleHeart = "💜"
    yellowHeart = "💛"
    greenHeart = "💚"
    whiteHeart = "🤍"
    blackHeart = "🖤"


    
    anim1_line1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim1_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    anim1_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    anim1_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    anim1_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    anim1_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    anim1_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    anim1_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    anim1_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim1 = "\n"+anim1_line1 + "\n"+anim1_line2+ "\n"+anim1_line3+"\n"+anim1_line4+"\n"+anim1_line5+"\n"+anim1_line6+"\n"+anim1_line7+"\n"+anim1_line8+"\n"+anim1_line9+"\n"


    anim2_line1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim2_line2 = "🤍🤍💛💛🤍💛💛🤍🤍"
    anim2_line3 = "🤍💛💛💛💛💛💛💛🤍"
    anim2_line4 = "🤍💛💛💛💛💛💛💛🤍"
    anim2_line5 = "🤍💛💛💛💛💛💛💛🤍"
    anim2_line6 = "🤍🤍💛💛💛💛💛🤍🤍"
    anim2_line7 = "🤍🤍🤍💛💛💛🤍🤍🤍"
    anim2_line8 = "🤍🤍🤍🤍💛🤍🤍🤍🤍"
    anim2_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim2 = "\n"+anim2_line1 + "\n"+anim2_line2+ "\n"+anim2_line3+"\n"+anim2_line4+"\n"+anim2_line5+"\n"+anim2_line6+"\n"+anim2_line7+"\n"+anim2_line8+"\n"+anim2_line9+"\n"


    anim3_line1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim3_line2 = "🤍🤍💜💜🤍💜💜🤍🤍"
    anim3_line3 = "🤍💜💜💜💜💜💜💜🤍"
    anim3_line4 = "🤍💜💜💜💜💜💜💜🤍"
    anim3_line5 = "🤍💜💜💜💜💜💜💜🤍"
    anim3_line6 = "🤍🤍💜💜💜💜💜🤍🤍"
    anim3_line7 = "🤍🤍🤍💜💜💜🤍🤍🤍"
    anim3_line8 = "🤍🤍🤍🤍💜🤍🤍🤍🤍"
    anim3_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim3 = "\n"+anim3_line1 + "\n"+anim3_line2+ "\n"+anim3_line3+"\n"+anim3_line4+"\n"+anim3_line5+"\n"+anim3_line6+"\n"+anim3_line7+"\n"+anim3_line8+"\n"+anim3_line9+"\n"

    anim4_line1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim4_line2 = "🤍🤍💜💜🤍💜💜🤍🤍"
    anim4_line3 = "🤍💜💜💜💜💜💜💜🤍"
    anim4_line4 = "🤍💜💜💜💜💜💜💜🤍"
    anim4_line5 = "🤍💜💜💜🖤💜💜💜🤍"
    anim4_line6 = "🤍🤍💜💜💜💜💜🤍🤍"
    anim4_line7 = "🤍🤍🤍💜💜💜🤍🤍🤍"
    anim4_line8 = "🤍🤍🤍🤍💜🤍🤍🤍🤍"
    anim4_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim4 = "\n"+anim4_line1 + "\n"+anim4_line2+ "\n"+anim4_line3+"\n"+anim4_line4+"\n"+anim4_line5+"\n"+anim4_line6+"\n"+anim4_line7+"\n"+anim4_line8+"\n"+anim4_line9+"\n"

    anim5_line1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim5_line2 = "🤍🤍💜💜🤍💜💜🤍🤍"
    anim5_line3 = "🤍💜💜💜💜💜💜💜🤍"
    anim5_line4 = "🤍💜💜🖤🖤🖤💜💜🤍"
    anim5_line5 = "🤍💜💜🖤🖤🖤💜💜🤍"
    anim5_line6 = "🤍🤍💜🖤🖤🖤💜🤍🤍"
    anim5_line7 = "🤍🤍🤍💜💜💜🤍🤍🤍"
    anim5_line8 = "🤍🤍🤍🤍💜🤍🤍🤍🤍"
    anim5_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim5 = "\n"+anim5_line1 + "\n"+anim5_line2+ "\n"+anim5_line3+"\n"+anim5_line4+"\n"+anim5_line5+"\n"+anim5_line6+"\n"+anim5_line7+"\n"+anim5_line8+"\n"+anim5_line9+"\n"
    
    anim6_line1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim6_line2 = "🤍🤍💜💜🤍💜💜🤍🤍"
    anim6_line3 = "🤍💜🖤🖤🖤🖤🖤💜🤍"
    anim6_line4 = "🤍💜🖤🖤🖤🖤🖤💜🤍"
    anim6_line5 = "🤍💜🖤🖤🖤🖤🖤💜🤍"
    anim6_line6 = "🤍🤍🖤🖤🖤🖤🖤🤍🤍"
    anim6_line7 = "🤍🤍🤍💜💜💜🤍🤍🤍"
    anim6_line8 = "🤍🤍🤍🤍💜🤍🤍🤍🤍"
    anim6_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim6 = "\n"+anim6_line1 + "\n"+anim6_line2+ "\n"+anim6_line3+"\n"+anim6_line4+"\n"+anim6_line5+"\n"+anim6_line6+"\n"+anim6_line7+"\n"+anim6_line8+"\n"+anim6_line9+"\n"
    
    anim7_line1 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim7_line2 = "🤍🤍🖤🖤🤍🖤🖤🤍🤍"
    anim7_line3 = "🤍🖤🖤🖤🖤🖤🖤🖤🤍"
    anim7_line4 = "🤍🖤🖤🖤🖤🖤🖤🖤🤍"
    anim7_line5 = "🤍🖤🖤🖤🖤🖤🖤🖤🤍"
    anim7_line6 = "🤍🤍🖤🖤🖤🖤🖤🤍🤍"
    anim7_line7 = "🤍🤍🤍🖤🖤🖤🤍🤍🤍"
    anim7_line8 = "🤍🤍🤍🤍🖤🤍🤍🤍🤍"
    anim7_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍🤍"
    anim7 = "\n"+anim7_line1 + "\n"+anim7_line2+ "\n"+anim7_line3+"\n"+anim7_line4+"\n"+anim7_line5+"\n"+anim7_line6+"\n"+anim7_line7+"\n"+anim7_line8+"\n"+anim7_line9+"\n"
    
    
    
    
    
    fillred1_line1 = "❤️🤍🤍🤍🤍🤍🤍🤍🤍"
    fillred1_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred1_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred1_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred1_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred1_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred1_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred1_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred1_line9 = "🤍🤍🤍🤍🤍🤍🤍🤍❤️"
    fillred1 = "\n"+fillred1_line1 + "\n"+fillred1_line2+ "\n"+fillred1_line3+"\n"+fillred1_line4+"\n"+fillred1_line5+"\n"+fillred1_line6+"\n"+fillred1_line7+"\n"+fillred1_line8+"\n"+fillred1_line9+"\n"
    
    fillred2_line1 = "❤️❤️🤍🤍🤍🤍🤍🤍🤍"
    fillred2_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred2_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred2_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred2_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred2_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred2_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred2_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred2_line9 = "🤍🤍🤍🤍🤍🤍🤍❤️❤️"
    fillred2 = "\n"+fillred2_line1 + "\n"+fillred2_line2+ "\n"+fillred2_line3+"\n"+fillred2_line4+"\n"+fillred2_line5+"\n"+fillred2_line6+"\n"+fillred2_line7+"\n"+fillred2_line8+"\n"+fillred2_line9+"\n"
    
    fillred3_line1 = "❤️❤️❤️🤍🤍🤍🤍🤍🤍"
    fillred3_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred3_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred3_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred3_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred3_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred3_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred3_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred3_line9 = "🤍🤍🤍🤍🤍🤍❤️❤️❤️"
    fillred3 = "\n"+fillred3_line1 + "\n"+fillred3_line2+ "\n"+fillred3_line3+"\n"+fillred3_line4+"\n"+fillred3_line5+"\n"+fillred3_line6+"\n"+fillred3_line7+"\n"+fillred3_line8+"\n"+fillred3_line9+"\n"
    
    fillred4_line1 = "❤️❤️❤️❤️🤍🤍🤍🤍🤍"
    fillred4_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred4_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred4_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred4_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred4_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred4_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred4_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred4_line9 = "🤍🤍🤍🤍🤍❤️❤️❤️❤️"
    fillred4 = "\n"+fillred4_line1 + "\n"+fillred4_line2+ "\n"+fillred4_line3+"\n"+fillred4_line4+"\n"+fillred4_line5+"\n"+fillred4_line6+"\n"+fillred4_line7+"\n"+fillred4_line8+"\n"+fillred4_line9+"\n"
    
    fillred5_line1 = "❤️❤️❤️❤️❤️🤍🤍🤍🤍"
    fillred5_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred5_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred5_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred5_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred5_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred5_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred5_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred5_line9 = "🤍🤍🤍🤍❤️❤️❤️❤️❤️"
    fillred5 = "\n"+fillred5_line1 + "\n"+fillred5_line2+ "\n"+fillred5_line3+"\n"+fillred5_line4+"\n"+fillred5_line5+"\n"+fillred5_line6+"\n"+fillred5_line7+"\n"+fillred5_line8+"\n"+fillred5_line9+"\n"
    
    fillred6_line1 = "❤️❤️❤️❤️❤️❤️🤍🤍🤍"
    fillred6_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred6_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred6_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred6_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred6_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred6_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred6_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred6_line9 = "🤍🤍🤍❤️❤️❤️❤️❤️❤️"
    fillred6 = "\n"+fillred6_line1 + "\n"+fillred6_line2+ "\n"+fillred6_line3+"\n"+fillred6_line4+"\n"+fillred6_line5+"\n"+fillred6_line6+"\n"+fillred6_line7+"\n"+fillred6_line8+"\n"+fillred6_line9+"\n"
    
    fillred7_line1 = "❤️❤️❤️❤️❤️❤️❤️🤍🤍"
    fillred7_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred7_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred7_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred7_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred7_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred7_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred7_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred7_line9 = "🤍🤍❤️❤️❤️❤️❤️❤️❤️"
    fillred7 = "\n"+fillred7_line1 + "\n"+fillred7_line2+ "\n"+fillred7_line3+"\n"+fillred7_line4+"\n"+fillred7_line5+"\n"+fillred7_line6+"\n"+fillred7_line7+"\n"+fillred7_line8+"\n"+fillred7_line9+"\n"
    
    fillred8_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred8_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred8_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred8_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred8_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred8_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred8_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred8_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred8_line9 = "🤍❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred8 = "\n"+fillred8_line1 + "\n"+fillred8_line2+ "\n"+fillred8_line3+"\n"+fillred8_line4+"\n"+fillred8_line5+"\n"+fillred8_line6+"\n"+fillred8_line7+"\n"+fillred8_line8+"\n"+fillred8_line9+"\n"
    
    fillred9_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred9_line2 = "🤍🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred9_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred9_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred9_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred9_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred9_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred9_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍🤍"
    fillred9_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred9 = "\n"+fillred9_line1 + "\n"+fillred9_line2+ "\n"+fillred9_line3+"\n"+fillred9_line4+"\n"+fillred9_line5+"\n"+fillred9_line6+"\n"+fillred9_line7+"\n"+fillred9_line8+"\n"+fillred9_line9+"\n"
    
    fillred11_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred11_line2 = "❤️🤍❤️❤️🤍❤️❤️🤍🤍"
    fillred11_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred11_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred11_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred11_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred11_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred11_line8 = "🤍🤍🤍🤍❤️🤍🤍🤍❤️"
    fillred11_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred11 = "\n"+fillred11_line1 + "\n"+fillred11_line2+ "\n"+fillred11_line3+"\n"+fillred11_line4+"\n"+fillred11_line5+"\n"+fillred11_line6+"\n"+fillred11_line7+"\n"+fillred11_line8+"\n"+fillred11_line9+"\n"

    fillred12_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred12_line2 = "❤️❤️❤️❤️🤍❤️❤️🤍🤍"
    fillred12_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred12_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred12_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred12_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred12_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred12_line8 = "🤍🤍🤍🤍❤️🤍🤍❤️❤️"
    fillred12_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred12 = "\n"+fillred12_line1 + "\n"+fillred12_line2+ "\n"+fillred12_line3+"\n"+fillred12_line4+"\n"+fillred12_line5+"\n"+fillred12_line6+"\n"+fillred12_line7+"\n"+fillred12_line8+"\n"+fillred12_line9+"\n"
    
    fillred13_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred13_line2 = "❤️❤️❤️❤️❤️❤️❤️🤍🤍"
    fillred13_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred13_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred13_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred13_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred13_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred13_line8 = "🤍🤍🤍🤍❤️🤍❤️❤️❤️"
    fillred13_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred13 = "\n"+fillred13_line1 + "\n"+fillred13_line2+ "\n"+fillred13_line3+"\n"+fillred13_line4+"\n"+fillred13_line5+"\n"+fillred13_line6+"\n"+fillred13_line7+"\n"+fillred13_line8+"\n"+fillred13_line9+"\n"

    fillred14_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred14_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred14_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred14_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred14_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred14_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred14_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred14_line8 = "🤍🤍🤍🤍❤️❤️❤️❤️❤️"
    fillred14_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred14 = "\n"+fillred14_line1 + "\n"+fillred14_line2+ "\n"+fillred14_line3+"\n"+fillred14_line4+"\n"+fillred14_line5+"\n"+fillred14_line6+"\n"+fillred14_line7+"\n"+fillred14_line8+"\n"+fillred14_line9+"\n"

    fillred15_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred15_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred15_line3 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred15_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred15_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred15_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred15_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred15_line8 = "🤍🤍🤍❤️❤️❤️❤️❤️❤️"
    fillred15_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred15 = "\n"+fillred15_line1 + "\n"+fillred15_line2+ "\n"+fillred15_line3+"\n"+fillred15_line4+"\n"+fillred15_line5+"\n"+fillred15_line6+"\n"+fillred15_line7+"\n"+fillred15_line8+"\n"+fillred15_line9+"\n"

    fillred17_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred17_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred17_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred17_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred17_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred17_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred17_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred17_line8 = "🤍🤍❤️❤️❤️❤️❤️❤️❤️"
    fillred17_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred17 = "\n"+fillred17_line1 + "\n"+fillred17_line2+ "\n"+fillred17_line3+"\n"+fillred17_line4+"\n"+fillred17_line5+"\n"+fillred17_line6+"\n"+fillred17_line7+"\n"+fillred17_line8+"\n"+fillred17_line9+"\n"

    fillred18_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred18_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred18_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred18_line4 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred18_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred18_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred18_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred18_line8 = "🤍❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred18_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred18 = "\n"+fillred18_line1 + "\n"+fillred18_line2+ "\n"+fillred18_line3+"\n"+fillred18_line4+"\n"+fillred18_line5+"\n"+fillred18_line6+"\n"+fillred18_line7+"\n"+fillred18_line8+"\n"+fillred18_line9+"\n"

    fillred19_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred19_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred19_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred19_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred19_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred19_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred19_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍🤍"
    fillred19_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred19_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred19 = "\n"+fillred19_line1 + "\n"+fillred19_line2+ "\n"+fillred19_line3+"\n"+fillred19_line4+"\n"+fillred19_line5+"\n"+fillred19_line6+"\n"+fillred19_line7+"\n"+fillred19_line8+"\n"+fillred19_line9+"\n"

    fillred20_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred20_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred20_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred20_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred20_line5 = "🤍❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred20_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred20_line7 = "🤍🤍🤍❤️❤️❤️🤍🤍❤️"
    fillred20_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred20_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred20 = "\n"+fillred20_line1 + "\n"+fillred20_line2+ "\n"+fillred20_line3+"\n"+fillred20_line4+"\n"+fillred20_line5+"\n"+fillred20_line6+"\n"+fillred20_line7+"\n"+fillred20_line8+"\n"+fillred20_line9+"\n"

    fillred21_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred21_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred21_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred21_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred21_line5 = "❤️❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred21_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred21_line7 = "🤍🤍🤍❤️❤️❤️🤍❤️❤️"
    fillred21_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred21_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred21 = "\n"+fillred21_line1 + "\n"+fillred21_line2+ "\n"+fillred21_line3+"\n"+fillred21_line4+"\n"+fillred21_line5+"\n"+fillred21_line6+"\n"+fillred21_line7+"\n"+fillred21_line8+"\n"+fillred21_line9+"\n"

    fillred22_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred22_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred22_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred22_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred22_line5 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred22_line6 = "🤍🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred22_line7 = "🤍🤍🤍❤️❤️❤️❤️❤️❤️"
    fillred22_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred22_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred22 = "\n"+fillred22_line1 + "\n"+fillred22_line2+ "\n"+fillred22_line3+"\n"+fillred22_line4+"\n"+fillred22_line5+"\n"+fillred22_line6+"\n"+fillred22_line7+"\n"+fillred22_line8+"\n"+fillred22_line9+"\n"

    fillred23_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred23_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred23_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred23_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred23_line5 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred23_line6 = "❤️🤍❤️❤️❤️❤️❤️🤍🤍"
    fillred23_line7 = "🤍🤍❤️❤️❤️❤️❤️❤️❤️"
    fillred23_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred23_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred23 = "\n"+fillred23_line1 + "\n"+fillred23_line2+ "\n"+fillred23_line3+"\n"+fillred23_line4+"\n"+fillred23_line5+"\n"+fillred23_line6+"\n"+fillred23_line7+"\n"+fillred23_line8+"\n"+fillred23_line9+"\n"

    fillred24_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred24_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred24_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred24_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred24_line5 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred24_line6 = "❤️❤️❤️❤️❤️❤️❤️🤍🤍"
    fillred24_line7 = "🤍❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred24_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred24_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred24 = "\n"+fillred24_line1 + "\n"+fillred24_line2+ "\n"+fillred24_line3+"\n"+fillred24_line4+"\n"+fillred24_line5+"\n"+fillred24_line6+"\n"+fillred24_line7+"\n"+fillred24_line8+"\n"+fillred24_line9+"\n"

    fillred25_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred25_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred25_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred25_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred25_line5 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred25_line6 = "❤️❤️❤️❤️❤️❤️❤️❤️🤍"
    fillred25_line7 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred25_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred25_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred25 = "\n"+fillred25_line1 + "\n"+fillred25_line2+ "\n"+fillred25_line3+"\n"+fillred25_line4+"\n"+fillred25_line5+"\n"+fillred25_line6+"\n"+fillred25_line7+"\n"+fillred25_line8+"\n"+fillred25_line9+"\n"
    
    fillred26_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26_line5 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26_line6 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26_line7 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26_line9 = "❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    fillred26 = "\n"+fillred26_line1 + "\n"+fillred26_line2+ "\n"+fillred26_line3+"\n"+fillred26_line4+"\n"+fillred26_line5+"\n"+fillred26_line6+"\n"+fillred26_line7+"\n"+fillred26_line8+"\n"+fillred26_line9+"\n"



    finish1_line1 = "❤️❤️❤️❤️❤️❤️❤️❤️"
    finish1_line2 = "❤️❤️❤️❤️❤️❤️❤️❤️"
    finish1_line3 = "❤️❤️❤️❤️❤️❤️❤️❤️"
    finish1_line4 = "❤️❤️❤️❤️❤️❤️❤️❤️"
    finish1_line5 = "❤️❤️❤️❤️❤️❤️❤️❤️"
    finish1_line6 = "❤️❤️❤️❤️❤️❤️❤️❤️"
    finish1_line7 = "❤️❤️❤️❤️❤️❤️❤️❤️"
    finish1_line8 = "❤️❤️❤️❤️❤️❤️❤️❤️"
    finish1 = "\n"+finish1_line1 + "\n"+finish1_line2+ "\n"+finish1_line3+"\n"+finish1_line4+"\n"+finish1_line5+"\n"+finish1_line6+"\n"+finish1_line7+"\n"+finish1_line8+"\n"

    finish2_line1 = "❤️❤️❤️❤️❤️❤️❤️"
    finish2_line2 = "❤️❤️❤️❤️❤️❤️❤️"
    finish2_line3 = "❤️❤️❤️❤️❤️❤️❤️"
    finish2_line4 = "❤️❤️❤️❤️❤️❤️❤️"
    finish2_line5 = "❤️❤️❤️❤️❤️❤️❤️"
    finish2_line6 = "❤️❤️❤️❤️❤️❤️❤️"
    finish2_line7 = "❤️❤️❤️❤️❤️❤️❤️"
    finish2 = "\n"+finish2_line1 + "\n"+finish2_line2+ "\n"+finish2_line3+"\n"+finish2_line4+"\n"+finish2_line5+"\n"+finish2_line6+"\n"+finish2_line7+"\n"

    finish3_line1 = "❤️❤️❤️❤️❤️❤️"
    finish3_line2 = "❤️❤️❤️❤️❤️❤️"
    finish3_line3 = "❤️❤️❤️❤️❤️❤️"
    finish3_line4 = "❤️❤️❤️❤️❤️❤️"
    finish3_line5 = "❤️❤️❤️❤️❤️❤️"
    finish3_line6 = "❤️❤️❤️❤️❤️❤️"
    finish3 = "\n"+finish3_line1 + "\n"+finish3_line2+ "\n"+finish3_line3+"\n"+finish3_line4+"\n"+finish3_line5+"\n"+finish3_line6+"\n"

    finish4_line1 = "❤️❤️❤️❤️❤️"
    finish4_line2 = "❤️❤️❤️❤️❤️"
    finish4_line3 = "❤️❤️❤️❤️❤️"
    finish4_line4 = "❤️❤️❤️❤️❤️"
    finish4_line5 = "❤️❤️❤️❤️❤️"
    finish4 = "\n"+finish4_line1 + "\n"+finish4_line2+ "\n"+finish4_line3+"\n"+finish4_line4+"\n"+finish4_line5+"\n"

    finish5_line1 = "❤️❤️❤️❤️"
    finish5_line2 = "❤️❤️❤️❤️"
    finish5_line3 = "❤️❤️❤️❤️"
    finish5_line4 = "❤️❤️❤️❤️"
    finish5 = "\n"+finish5_line1 + "\n"+finish5_line2+ "\n"+finish5_line3+"\n"+finish5_line4+"\n"

    finish6_line1 = "❤️❤️❤️"
    finish6_line2 = "❤️❤️❤️"
    finish6_line3 = "❤️❤️❤️"
    finish6 = "\n"+finish6_line1 + "\n"+finish6_line2+ "\n"+finish6_line3+"\n"

    finish7 = "❤️"

    while(edit_text != first_text):
        try:
            msg.edit(edit_text)
            sleep(0.5)

            msg.edit(anim1)
            sleep(0.5)

            msg.edit(anim2)
            sleep(0.5)

            msg.edit(anim3)
            sleep(0.5)

            msg.edit(anim4)
            sleep(0.2)
            msg.edit(anim5)
            sleep(0.2)
            msg.edit(anim6)
            sleep(0.2)
            msg.edit(anim7)
            sleep(0.2)
            
            msg.edit(anim1)
            sleep(0.5)


            msg.edit(fillred1)
            sleep(0.05)           
            msg.edit(fillred2)
            sleep(0.05)
            msg.edit(fillred3)
            sleep(0.05)
            msg.edit(fillred4)
            sleep(0.05)
            msg.edit(fillred5)
            sleep(0.05)
            msg.edit(fillred6)
            sleep(0.05)
            msg.edit(fillred7)
            sleep(0.05)
            msg.edit(fillred8)
            sleep(0.05)
            msg.edit(fillred9)
            sleep(0.05)
            msg.edit(fillred11)
            sleep(0.05)
            msg.edit(fillred12)
            sleep(0.05)
            msg.edit(fillred13)
            sleep(0.05)
            msg.edit(fillred14)
            sleep(0.05)
            msg.edit(fillred15)
            sleep(0.05)
            msg.edit(fillred17)
            sleep(0.05)
            msg.edit(fillred18)
            sleep(0.05)
            msg.edit(fillred19)
            sleep(0.05)
            msg.edit(fillred20)
            sleep(0.05)
            msg.edit(fillred21)
            sleep(0.05)
            msg.edit(fillred22)
            sleep(0.05)
            msg.edit(fillred23)
            sleep(0.05)
            msg.edit(fillred24)
            sleep(0.05)
            msg.edit(fillred25)
            sleep(0.05)
            msg.edit(fillred26)
            sleep(0.2)

            msg.edit(finish1)
            sleep(0.2)
            msg.edit(finish2)
            sleep(0.2)
            msg.edit(finish3)
            sleep(0.2)
            msg.edit(finish4)
            sleep(0.2)
            msg.edit(finish5)
            sleep(0.2)
            msg.edit(finish6)
            sleep(0.2)

            msg.edit(finish7)
            sleep(0.1)
            break
        except FloodWait as e:
            sleep(e.x)
'''
            msg.edit(edit_text + purpleHeart)
            sleep(0.5)

            msg.edit(edit_text + yellowHeart)
            sleep(0.5)

            msg.edit(edit_text + greenHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart + purpleHeart)
            sleep(0.5)

            msg.edit(edit_text + redHeart + purpleHeart + yellowHeart)
            sleep(0.5)
'''
end_text = "✅Пентагон успешно взломан."
text_edit = "🟢👮‍♂️ Взламываю пентагон... "
vault_percent1 = random.randint(13, 27)
vault_percent2 = random.randint(32, 48)
vault_percent3 = random.randint(56, 74)
vault_percent4 = random.randint(78, 92)
vault_percent5 = 100

@app.on_message(filters.command("vault", prefixes=".") & filters.me)
def vault(_, msg):
    while(text_edit != end_text):
        try:
            msg.edit(text_edit + str(vault_percent1) + "%")
            sleep(random.randrange(1,2))

            msg.edit(text_edit + str(vault_percent2) + "%")
            sleep(random.randrange(1,2))
            msg.edit(text_edit + str(vault_percent3) + "%")
            sleep(random.randrange(1,2))
            msg.edit(text_edit + str(vault_percent4) + "%")
            sleep(random.randrange(1,2))
            msg.edit(text_edit + str(vault_percent5)+ "%")
            sleep(random.randrange(1,2))

            msg.edit(end_text)
            break
        except FloodWait as e:
            sleep(e.x)


tema_text_end = "👀😰🌈тема, ты педик на "
tema_text_edit = "👀😰🌈тема, ты педик на..."
@app.on_message(filters.command("temagay", prefixes=".") & filters.me)
def tema(_, msg):
            msg.edit(tema_text_edit + str(random.randint(0,100)) + "%")
            sleep(random.randrange(1,2))
            msg.edit(tema_text_edit + str(random.randint(0,100)) + "%")
            sleep(random.randrange(1,2))
            msg.edit(tema_text_edit + str(random.randint(0,100)) + "%")
            sleep(random.randrange(1,2))

            msg.edit(tema_text_end+str(random.randint(0,100))+ "%")


rwq_text_end = "👀😰🌈рвк, ты педик на "
rwq_text_edit = "👀😰🌈рвк, ты педик на..."
@app.on_message(filters.command("rwqgay", prefixes=".") & filters.me)
def rwq(_, msg):
            msg.edit(rwq_text_edit + str(random.randint(0,100)) + "%")
            sleep(random.randrange(1,2))
            msg.edit(rwq_text_edit + str(random.randint(0,100)) + "%")
            sleep(random.randrange(1,2))
            msg.edit(rwq_text_edit + str(random.randint(0,100)) + "%")
            sleep(random.randrange(1,2))

            msg.edit(rwq_text_end+str(random.randint(0,100))+ "%")
      
app.run()
