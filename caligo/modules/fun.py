
from typing import ClassVar, Optional

from caligo import command, module


class Profiles(module.Module):
    name: ClassVar[str] = "Funny"

    @command.desc("Kocok")
    @command.usage(
        ".kocok"
    )
    @command.alias("kc")
    async def cmd_kocok(self, ctx: command.Context):  
        await ctx.respond("1")
        await ctx.respond("2")
        await ctx.respond("3")
        await ctx.respond("4")

        return f"Terkocok!!"

