import asyncio
# import re
from typing import Any, ClassVar, Literal, Optional, Set, Tuple

from pyrogram.types import Message

from caligo import command, module, util

    @command.desc("Kocok")
    async def cmd_kocok(self, ctx: command.Context):
        
        await ctx.respond("1")
        await ctx.respond("2")
        await ctx.respond("3")

        return f"Terkocok!"

        await ctx.msg.delete()