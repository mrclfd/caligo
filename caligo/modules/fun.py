import asyncio

from typing import ClassVar, Optional

from caligo import command, module


class Profiles(module.Module):
    name: ClassVar[str] = "Funny"

    @command.desc("Menyala abangku🔥🙌")
    @command.usage(
        ".menyala"
    )
    @command.alias("mnyl")
    async def cmd_menyala(self, ctx: command.Context):  
        await ctx.respond("")
        #await asyncio.sleep(1)
        await ctx.respond("siap panutan🆙✊🙌")
        #await asyncio.sleep(1)
        await ctx.respond("tipis tipis abangda🦅🎣")
        #await asyncio.sleep(1)
        await ctx.respond("tetap ilmu padi abangkuh🌾")
        #await asyncio.sleep(1)
        await ctx.respond("tetap rispek🫡🙌")
        #await asyncio.sleep(1)
        await ctx.respond("kelas bangda👍🔥")
        #await asyncio.sleep(1)
        await ctx.respond("kasi paham bos")
        #await asyncio.sleep(1)

        return f"Menyala abangku🔥🙌"

