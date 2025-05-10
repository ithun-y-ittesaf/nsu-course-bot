from discord.ext import commands
from utils.storage import add_course_for_user

@commands.command(name='addcourse')
async def add_course(ctx, course_code: str, section_code: str):
    add_course_for_user(str(ctx.author.id), course_code.upper(), section_code.upper())
    await ctx.send(f"Added {course_code.upper()} - {section_code.upper()} for <@{ctx.author.id}>.")
