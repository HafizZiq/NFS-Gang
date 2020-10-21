# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from covid import Covid
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.covid (.*)")
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
        output_text = (
            f"`😷Confirmed   : {format_integer(country_data['confirmed'])} (+{format_integer(country_data['new_cases'])})`\n" +
            f"`🤒Active      : {format_integer(country_data['active'])}`\n" +
            f"`🤕Critical    : {format_integer(country_data['critical'])}`\n" +
            f"`⚰Deaths      : {format_integer(country_data['deaths'])} (+{format_integer(country_data['new_deaths'])})`\n" +
            f"`😇Recovered   : {format_integer(country_data['recovered'])}`\n" +
            f"`🧪Total tests : {format_integer(country_data['total_tests'])}`\n" +
            f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})")
        await event.edit(f"`Corona Virus Info in {country}:`\n\n{output_text}")
    except ValueError:
        await event.edit(
            f"No information found for: {country}!\nCheck your spelling and try again."
        )


@register(outgoing=True, pattern="^.covid$")
async def corona(event):
    await event.edit("`Processing...`")
    country = "World"
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
        output_text = (
            f"`😷Confirmed   : {format_integer(country_data['confirmed'])} (+{format_integer(country_data['new_cases'])})`\n" +
            f"`🤒Active      : {format_integer(country_data['active'])}`\n" +
            f"`🤕Critical    : {format_integer(country_data['critical'])}`\n" +
            f"`⚰Deaths      : {format_integer(country_data['deaths'])} (+{format_integer(country_data['new_deaths'])})`\n" +
            f"`😇Recovered   : {format_integer(country_data['recovered'])}`\n" +
            f"`🧪Total tests : N/A`\n" +
            f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})")
        await event.edit(f"`Corona Virus Info in {country}:`\n\n{output_text}")
    except ValueError:
        await event.edit(
            f"No information found for: {country}!\nCheck your spelling and try again."
        )


@register(outgoing=True, pattern="^.covidsk$")
async def corona(event):
    await event.edit("`Processing...`")
    country = "s. korea"
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
        output_text = (
            f"`😷Confirmed   : {format_integer(country_data['confirmed'])} (+{format_integer(country_data['new_cases'])})`\n" +
            f"`🤒Active      : {format_integer(country_data['active'])}`\n" +
            f"`🤕Critical    : {format_integer(country_data['critical'])}`\n" +
            f"`⚰Deaths      : {format_integer(country_data['deaths'])} (+{format_integer(country_data['new_deaths'])})`\n" +
            f"`😇Recovered   : {format_integer(country_data['recovered'])}`\n" +
            f"`🧪Total tests : {format_integer(country_data['total_tests'])}`\n" +
            f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})")
        await event.edit(f"`Corona Virus Info in {country}:`\n\n{output_text}")
    except ValueError:
        await event.edit(
            f"No information found for: {country}!\nCheck your spelling and try again."
        )


def format_integer(number, thousand_separator="."):
    def reverse(string):
        string = "".join(reversed(string))
        return string

    s = reverse(str(number))
    count = 0
    result = ""
    for char in s:
        count = count + 1
        if count % 3 == 0:
            if len(s) == count:
                result = char + result
            else:
                result = thousand_separator + char + result
        else:
            result = char + result
    return result


CMD_HELP.update({"covid": "`.covid `**<country>**"
                 "\n`Usage: Get an information about covid-19 data in your country.`\n\n"
                 "`.covid`"
                 "\n`Usage: Get an information about covid-19 data in Worldwide.`\n\n"
                 "`.covidsk`"
                 "\n`Usage: Get an information about covid-19 data in South Korea/Korea`.\n"})
