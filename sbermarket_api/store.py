from sbermarket_api.api import API
from sbermarket_api.product import Product


class Store:
    def __init__(self, api: API, store_id: int, name: str, **kwargs):
        self.api = api
        self.store_id = store_id
        self.name = name
        self.__dict__.update(kwargs)

    def search_products(self, search: str, per_page: int = 24, page: int = 1):
        """Поиск по товарам per_page 24 это максимум"""
        query = {"q": search, "per_page": per_page, "page": page}
        response = self.api.request(f"stores/{self.store_id}/products", query=query)
        return [Product(self.api, **product) for product in response["products"]]

    def categories(self, depth: int = 2):
        """Получить инфу по категориям, товаров там не будет"""
        query = {}
        if depth:
            query["depth"] = depth
        return self.api.request(f"stores/{self.store_id}/categories", query=query)

    def product(self, id: str):
        """Получить инфу по одному товару"""
        url = f"stores/{self.store_id}/products/{id}"
        return Product(self.api, **self.api.request(url))

    def __str__(self):
        return self.name
