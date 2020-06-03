
from telethon import events
import asyncio
import os
import sys
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.plane(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
        
        
    await event.edit("✈-------------")
    await event.edit("-✈------------")
    await event.edit("--✈-----------")
    await event.edit("---✈----------")
    await event.edit("----✈---------")
    await event.edit("-----✈--------")
    await event.edit("------✈-------")
    await event.edit("-------✈------")
    await event.edit("--------✈-----") 
    await event.edit("---------✈----")
    await event.edit("----------✈---")
    await event.edit("-----------✈--")
    await event.edit("------------✈-")
    await event.edit("-------------✈")
    await event.edit("plane is gone, what are you waitin for.")
    await asyncio.sleep(3)
    await event.delete()
    CMD_HELP.update({
"plane":
"#meme\
\nUse:- .plane"
})

