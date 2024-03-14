import asyncio
# import re
from typing import Any, ClassVar, Literal, Optional, Set, Tuple

from pyrogram.types import Message

from caligo import command, module, util

    @command.desc("Kocok")
    async def cmd_kocok(self, ctx: command.Context):
        
        await ctx.msg.edit("1")
        await ctx.msg.edit("2")
        await ctx.msg.edit("3")

        return f"Terkocok!"

        await ctx.msg.delete()
