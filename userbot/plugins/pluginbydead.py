import asyncio
import io

from telethon import events

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="mkc"))
async def monu(mkc):
    name = mkc.pattern_match.group(1)
    f = (
        "{name} madharchod h uski maa ki choot uski maa ko ulta taang ke pelangai tab usko pata chalega \n"
        "\n"
        "Uski maa ka bhosra \n"
        "Sale randi ke aulad \n"
        "{name} Madharjatt \n"
        "Tere khandan ko kutta chode \n"
        "Randi Jatt {name} ki MKC \n"
    )

    await mkc.edit(f)


# ©VaibhavRaj jo edit kiya uski maa chod deni h
