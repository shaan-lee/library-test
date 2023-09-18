import asyncio
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from beanie import Document, Indexed, init_beanie


class Category(BaseModel):
    name: str
    description: str


class Product(Document):
    name: str  # You can use normal types just like in pydantic
    description: Optional[str] = None
    price: Indexed(
        float
    )  # You can also specify that a field should correspond to an index
    category: Category  # You can include pydantic models as well


# This is an asynchronous example, so we will access it from an async function
async def example():
    # Beanie uses Motor async client under the hood
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    # Initialize beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[Product])

    chocolate = Category(
        name="Chocolate", description="A preparation of roasted and ground cacao seeds."
    )
    # Beanie documents work just like pydantic models
    tonybar = Product(name="Tony's", price=5.95, category=chocolate)
    # And can be inserted into the database
    await tonybar.insert()

    # You can find documents with pythonic syntax
    product = await Product.find_one(Product.price < 10)

    # And update them
    await product.set({Product.name: "Gold bar"})


if __name__ == "__main__":
    asyncio.run(example())
