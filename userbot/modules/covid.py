# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from datetime import datetime
from covid import Covid
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.covid (.*)")
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text =  f"`😷Confirmed   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`🤒Active      : {country_data['active']}`\n"
        output_text += f"`🤕Critical    : {country_data['critical']}`\n"
        output_text += f"`⚰Deaths      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😇Recovered   : {country_data['recovered']}`\n"
        output_text += f"`🧪Total tests : {country_data['total_tests']}`\n"
        output_text += f"`Data provided by worldometers`\n"
        covid2 = Covid(source="john_hopkins")
        country_data = covid2.get_status_by_country_name(country)
        if country_data:
            output_text += (
                "`📅Last update : "
                f"{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%Y-%m-%d %H:%M:%S')}`\n"
            )
            output_text += f"`Date provided by `[Johns Hopkins University](https://j.mp/2xf6oxF)"
        else:
            output_text = "No date information yet about this country!"
    else:
        output_text = "No information yet about this country!"

    await event.edit(f"`Corona Virus Info in {country}:`\n\n{output_text}")

@register(outgoing=True, pattern="^.covid$")
async def corona(event):
    await event.edit("`Processing...`")
    country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text =  f"`😷Confirmed   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`🤒Active      : {country_data['active']}`\n"
        output_text += f"`🤕Critical    : {country_data['critical']}`\n"
        output_text += f"`⚰Deaths      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😇Recovered   : {country_data['recovered']}`\n"
        output_text += f"`🧪Total tests : N/A`\n"
        output_text += f"`Data provided by worldometers`\n"
        output_text += f"`📅Last update : Timer are not yet available for World status`"
    else:
        output_text = "No information yet about this country!"

    await event.edit(f"`Corona Virus Info in {country}:`\n\n{output_text}")

@register(outgoing=True, pattern="^.covidsk$")
async def corona(event):
    await event.edit("`Processing...`")
    country = "s. korea"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text =  f"`😷Confirmed   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`🤒Active      : {country_data['active']}`\n"
        output_text += f"`🤕Critical    : {country_data['critical']}`\n"
        output_text += f"`⚰Deaths      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😇Recovered   : {country_data['recovered']}`\n"
        output_text += f"`🧪Total tests : {country_data['total_tests']}`\n"
        output_text += f"`Data provided by worldometers`\n"
        country = "Korea, South"
        covid2 = Covid(source="john_hopkins")
        country_data = covid2.get_status_by_country_name(country)
        if country_data:
            output_text += (
                "`📅Last update : "
                f"{datetime.utcfromtimestamp(country_data['last_update'] // 1000).strftime('%Y-%m-%d %H:%M:%S')}`\n"
            )
            output_text += f"`Date provided by `[Johns Hopkins University](https://j.mp/2xf6oxF)"
        else:
            output_text = "No date information yet about this country!"
    else:
        output_text = "No information yet about this country!"

    await event.edit(f"`Corona Virus Info in {country}:`\n\n{output_text}")



CMD_HELP.update({
        "covid": 
        "`.covid `**<country>**"
        "\n`Usage: Get an information about data covid-19 in your country.`\n"
        "`.covid`"
        "\n`Usage: Get an information about data covid-19 in Worldwide.`\n"
        "`.covidsk`"
        "\n`Usage: Get an information about data covid-19 in South Korea/Korea`.\n"
    })
