from discord.ext import commands
from utils.storage import remove_course_for_user

@commands.command(name='removecourse')
async def remove_course(ctx, course_code: str, section_code: str):
    removed = remove_course_for_user(str(ctx.author.id), course_code.upper(), section_code.upper())
    if removed:
        await ctx.send(f"Removed {course_code.upper()} - {section_code.upper()} for <@{ctx.author.id}>.")
    else:
        await ctx.send("That course wasn't found.")
