from discord.ext import commands
from utils.storage import get_user_courses

@commands.command(name='check')
async def check(ctx):
    user_id = str(ctx.author.id)
    courses = get_user_courses(user_id)
    if not courses:
        await ctx.send("You're not tracking any courses.")
        return
    lines = [f"{c['course']} - {c['section']}" for c in courses]
    await ctx.send(f"You're tracking:\n" + "\n".join(lines))
