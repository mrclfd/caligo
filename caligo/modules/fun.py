import asyncio

from typing import ClassVar, Optional

from caligo import command, module


class Profiles(module.Module):
    name: ClassVar[str] = "Funny"

    @command.desc("")
    @command.usage(
        ".menyala"
    )
    @command.alias("mnyl")
    async def cmd_menyala(self, ctx: command.Context):  
        await ctx.respond("tipis tipis cakk 🔥🔥")
        await asyncio.sleep(1.2)
        await ctx.respond("sesekali 🙌🏼")
        await asyncio.sleep(1.2)
        await ctx.respond("kelas abangkuu 🔥🔝")
        await asyncio.sleep(1.2)
        await ctx.respond("izin abangkuu 🔥")
        await asyncio.sleep(1.2)
        await ctx.respond("panutan 🔝✊🏼🙌🏼")
        await asyncio.sleep(1.2)
        await ctx.respond("kelas abangda 🔥🫡")
        await asyncio.sleep(1.2)
        await ctx.respond("rispeekk 👍🏼🙌🏼")
        await asyncio.sleep(1.2)

        return f"Menyala abangku🔥🙌"

