import asyncio
from scraper.scraper import fetch_seat_data
from utils.storage import load_data, save_data

async def check_seats(bot):
    while True:
        data = load_data()
        updated = False

        for user_id, courses in data.items():
            for course in courses:
                new_seats = fetch_seat_data(course['course'], course['section'])
                if course['seats'] is None:
                    course['seats'] = new_seats
                elif new_seats != course['seats']:
                    user = await bot.fetch_user(int(user_id))
                    channel = await user.create_dm()
                    await channel.send(f"🔔 {course['course']} has {new_seats} seats (was {course['seats']})")
                    course['seats'] = new_seats
                    updated = True

        if updated:
            save_data(data)

        await asyncio.sleep(300)  # Check every 5 min

def start_scheduler(bot):
    asyncio.create_task(check_seats(bot))
