# type: ignore
"""Example of code."""
from typing import Dict

import json

from sbermarket_api import AuthenticatedClient
from sbermarket_api.api.client import get_stores
from sbermarket_api.api.store import get_stores_store_id_products

DEFAULT_TOKEN = "7ba97b6f4049436dab90c789f946ee2f"

if __name__ == "__main__":
    client = AuthenticatedClient(base_url="https://sbermarket.ru/api", token=DEFAULT_TOKEN)
    # Получить все магазины доступные для данной точки.
    stores = get_stores.sync(client=client, lat="60.003526", lon="30.253471")
    # Найти где самые дешевые "j7 томат"
    lowest_prices = {}
    for store in stores:
        products_response = get_stores_store_id_products.sync(client=client, store_id=store.store_id, q="j7 томат")
        for product in products_response.products:
            if not lowest_prices or all(product.price <= p for p in lowest_prices.keys()):
                if lowest_prices and any(product.price < p for p in lowest_prices.keys()):
                    lowest_prices.clear()
                lowest_prices[product.price] = {"store": store.name, "url": product.canonical_url}
    print(json.dumps(lowest_prices, indent=2, ensure_ascii=False))
