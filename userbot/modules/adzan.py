import json
import requests
from userbot import CMD_HELP
from userbot.events import register

PLACE = ''


@register(pattern="^.adzan(12|24) (.*)")
async def get_adzan(adzan):
    if not adzan.pattern_match.group(2):
        LOCATION = PLACE
        if not LOCATION:
            await adzan.edit("Please specify a zone code.")
            return
    else:
        LOCATION = adzan.pattern_match.group(2).upper()
        type = adzan.pattern_match.group(1)
    await adzan.edit("Processing...")
    if type == "12":
        url = f'http://api.azanpro.com/times/today.json?zone={LOCATION}&format=12-hour'
    elif type == "24":
        url = f'http://api.azanpro.com/times/today.json?zone={LOCATION}&format=24-hour'
    else:
        await adzan.edit("Please use .adzan12 or .adzan24.\
            \nElse, refer `.help adzan` how to use it."
                         )
        return
    request = requests.get(url)
    parsed = json.loads(request.text)
    timezone = LOCATION
    try:
        city = parsed["locations"]
        date = parsed["prayer_times"]["date"]
        imsak = parsed["prayer_times"]["imsak"].upper()
        subuh = parsed["prayer_times"]["subuh"].upper()
        syuruk = parsed["prayer_times"]["syuruk"].upper()
        zohor = parsed["prayer_times"]["zohor"].upper()
        asar = parsed["prayer_times"]["asar"].upper()
        maghrib = parsed["prayer_times"]["maghrib"].upper()
        isyak = parsed["prayer_times"]["isyak"].upper()
        result = (f"**Jadual Solat**:\n"
                  f"📅` Date : {date} | {timezone}`\n"
                  f"📍` Location: {city}`\n\n"
                  f"`Imsak   : {imsak}`\n"
                  f"`Subuh   : {subuh}`\n"
                  f"`Syuruk  : {syuruk}`\n"
                  f"`Zohor   : {zohor}`\n"
                  f"`Asar    : {asar}`\n"
                  f"`Maghrib : {maghrib}`\n"
                  f"`Isyak   : {isyak}`\n"
                  )
        await adzan.edit(result)
    except KeyError:
        await adzan.edit(parsed["error_desc"])
        return

CMD_HELP.update({
    "adzan": ".adzan12(12-hour format) or .adzan24(24-hour format) <zone code>\
        \nWARNING!! This Module only works with States in Malaysia ONLY!!\
        \nUsage: Gets the prayer time for Muslim.\
        \n[Here](https://telegra.ph/Zone-Code-07-03) the zone code instructions."
})
