from .. import bot,openai_key
from telethon import events 
import asyncio
import openai

openai_key"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"

openai.my_api_key = openai_key

@bot.on(events.NewMessage(incoming = True ,        pattern = "/start")) 
async def start(event):
  await event.reply("Hello!")


@bot.on(events.NewMessage(incoming = True ,        pattern = "/get")) 
async def start(event):
    a=await event.reply("Hello This Is Get Command") 
    await asyncio.sleep(3) 
    await a.edit("this is edited msg")
    
    
    
@bot.on(events.NewMessage(incoming = True ,        pattern = "/eval")) 
async def start(event):
    await event.reply("Hello This Is Eval Command")