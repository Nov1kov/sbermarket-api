"""Example of code."""

from sbermarket_api.client import Client

if __name__ == "__main__":
    client = Client()
    # Получить все магазины доступные для данной точки.
    stores = client.stores(lat=60.003526, lon=30.253471)
    # Найти где самые дешевые "Сок J7 томат 970 мл"
    lowest_prices = {}
    for store in stores:
        products = store.search_products("Сок J7 томат 970 мл")
        for product in products:
            if not lowest_prices or all(product.price <= p for p in lowest_prices.keys()):
                if lowest_prices and any(product.price < p for p in lowest_prices.keys()):
                    lowest_prices.clear()
                lowest_prices[product.price] = {"store": str(store), "url": product.canonical_url}
    print(lowest_prices)
