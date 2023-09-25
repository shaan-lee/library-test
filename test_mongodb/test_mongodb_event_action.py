from typing import Optional

import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from beanie import Document, Indexed, init_beanie, Update, after_event, before_event
from pydantic import Field

from datetime import datetime
import asyncio
import time


class Event(Document):
    created_at: Indexed(datetime) = Field(default_factory=time.utcnow)
    updated_at: Indexed(datetime) = Field(default_factory=time.utcnow)
    test_string: str
    boolean_test: bool

    @after_event(Update)
    async def update_updated_at(self):
        await self.update(
            {"$set": {"updated_at": datetime.utcnow()}},
            skip_actions=["update_updated_at"],
        )


# Call this from within your event loop to get beanie setup.
async def init():
    # Create Motor client
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    # Init beanie with the Product document class
    await init_beanie(database=client.test, document_models=[Event])


async def main():
    event = Event(test_string="hi", boolean_test=False)
    await event.insert()
    time.sleep(2)
    event = await Event.find_one({"boolean_test": "false"})
    time.sleep(2)
    await event.update({"$set": {"boolean_test": True}})


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_until_complete(main())
    loop.close()
