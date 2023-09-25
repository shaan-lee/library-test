from typing import Optional

import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from beanie import Document, Indexed, init_beanie, Update, after_event, before_event
from pydantic import Field
from pymongo import ASCENDING
from pymongo.operations import IndexModel
from pymongo.errors import BulkWriteError, DuplicateKeyError

from datetime import datetime, timedelta
import asyncio
import time


class Test(Document):
    created_at: Indexed(datetime) = Field(default_factory=time.utcnow)
    test_string: str
    boolean_test: bool

    class Settings:
        indexes = [
            IndexModel(
                keys=[("test_string", ASCENDING)],
                name="test_string",
                unique=True,
            ),
        ]


# Call this from within your event loop to get beanie setup.
async def init():
    # Create Motor client
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    # Init beanie with the Product document class
    await init_beanie(database=client.test, document_models=[Test])


async def main():
    test = Test(test_string="hi", boolean_test=False)
    result = await test.insert()
    print(result)
    try:
        test2 = Test(test_string="hi", boolean_test=False)
        result2 = await test2.insert()
        print("=================")
        print(result2)
    except DuplicateKeyError:
        print("duplicate!!!!!!!!!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_until_complete(main())
    loop.close()
