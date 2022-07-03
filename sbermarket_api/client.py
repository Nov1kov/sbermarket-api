from typing import List

from sbermarket_api.api import API
from sbermarket_api.store import Store

DEFAULT_TOKEN = "7ba97b6f4049436dab90c789f946ee2f"


class Client:
    def __init__(self, base_url="https://sbermarket.ru/api/", client_token: str = DEFAULT_TOKEN):
        self.api = API(base_url=base_url, client_token=client_token)

    def stores(self, lat: float, lon: float, shipping_method="delivery") -> List[Store]:
        """lat, lon - обязательные
        если указать shipping_method = None - выдаст 1000+ точек. Возможно все в России?
        возможные параметры еще: include=closest_shipping_options,labels,retailer,label_store_ids"""
        query = {"lat": lat, "lon": lon}
        if shipping_method:
            query["shipping_method"] = shipping_method
        return [Store(self.api, **store) for store in self.api.request("stores", query=query)]

    def store(self, id: int) -> Store:
        """Получить полную информацию по магазину"""
        result = self.api.request(f"stores/{id}")["store"]
        return Store(self.api, store_id=result["id"], **result)

    def shopping_session(self):
        """получить available_stores, favorite_product_skus, store_labels,
        В ответ если это не анонимная сессия может придти полная инфа о пользователе."""
        return self.api.request("shopping_session", auth=False)
