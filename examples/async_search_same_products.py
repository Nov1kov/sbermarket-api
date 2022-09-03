# type: ignore
"""Example of code."""
import asyncio
import json

from sbermarket_api.api.client import get_stores
from sbermarket_api.api.store import get_stores_store_id_products
from sbermarket_api.client import AuthenticatedClient, Client

DEFAULT_TOKEN = "7ba97b6f4049436dab90c789f946ee2f"


async def main():
    client = AuthenticatedClient(base_url="https://sbermarket.ru/api", token=DEFAULT_TOKEN)
    # Получить все магазины доступные для данной точки.
    stores = await get_stores.asyncio(client=client, lat="60.003526", lon="30.253471")
    # Собрать список, сколько уникальных товаров найдется по одной строке пойска.
    # Например: "Сок J7 яблоко 970 мл" и "Сок J7 яблочный 970 мл"
    products_tasks = [
        get_stores_store_id_products.asyncio(client=client, store_id=store.store_id, q="j7 томат") for store in stores
    ]
    count_list = {}
    products_responses = await asyncio.gather(*products_tasks)
    for products_response in products_responses:
        for product in products_response.products:
            count_list.setdefault(str(product), 0)
            count_list[str(product)] += 1
    print(json.dumps(count_list, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
