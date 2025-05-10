from discord.ext import commands

@commands.command(name='helpme')
async def helpme(ctx):
    help_text = (
        "**Available Commands:**\n"
        "`!helpme` - Show this message\n"
        "`!addcourse <COURSE_CODE> <SECTION_CODE>` - Add a course to track\n"
        "`!removecourse <COURSE_CODE> <SECTION_CODE>` - Stop tracking a course\n"
        "`!check` - Show your followed courses"
    )
    await ctx.send(help_text)
