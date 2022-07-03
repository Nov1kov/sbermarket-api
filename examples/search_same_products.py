"""Example of code."""

from sbermarket_api.client import Client

if __name__ == "__main__":
    client = Client()
    # Получить все магазины доступные для данной точки.
    stores = client.stores(lat=60.003526, lon=30.253471)
    # Собрать список, сколько уникальных товаров найдется по одной строке пойска.
    # Например: "Сок J7 яблоко 970 мл" и "Сок J7 яблочный 970 мл"
    count_list = {}
    for store in stores:
        products = store.search_products("Сок J7 яблоко 970 мл")
        for product in products:
            count_list.setdefault(str(product), 0)
            count_list[str(product)] += 1
    print(count_list)
