from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^.itv(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to a Link.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Reply to a Link```")
        return
    chat = "@chotamreaderbot"
    reply_message.sender
    await event.edit("```Processing```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=272572121))
            msg = await bot.forward_messages(chat, reply_message)
            response = await response
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("`RIP Check Your Blacklist Boss`")
            return
        if response.text.startswith(""):
            await event.edit("Am I Dumb Or Am I Dumb?")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)
            await bot.send_read_acknowledge(event.chat_id)
            """ - cleanup chat after completed - """
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])

CMD_HELP.update({
    'itv':
    '.itv <reply to link>\
        \nUsage: Make instant view from any article.'
})
