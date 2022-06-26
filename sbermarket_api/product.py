from sbermarket_api.api import API


class Product:
    """{
    'id': '482975',
    'legacy_offer_id': 268013250,
    'legacy_product_id': 66942,
    'sku': '60020', # Иногда этот параметр может совпадать между товарами.
    'retailer_sku': '482975',
    'name': 'Сок J7 яблоко 970 мл',
    'price': 159.01,
    'original_price': 159.01,
    'discount': 0.0,
    'human_volume': '970 мл.',
    'volume': 970.0,
    'volume_type': 'ml',
    'items_per_pack': 1,
    'discount_ends_at': None,
    'price_type': 'per_item',
    'grams_per_unit': 970,
    'unit_price': 159.01,
    'original_unit_price': 159.01,
    'slug': 'sok-j7-iabloko-4',
    'max_select_quantity': 999,
    'canonical_url': 'https://sbermarket.ru/products/60020-sok-j7-iabloko-4',
    'available': True,
    'vat_info': None,
    'bmpl_info': None,
    'promo_badge_ids': [],
    'requirements': [],
    'image_urls': ['https://sbermarket.ru/spree/products/3139001/original/60020_2.jpg?1636780049',
                    'https://sbermarket.ru/spree/products/3139000/original/60020.jpg?1636780048']
                }
    """

    def __init__(self, api: API, name: str = "", sku: str = "", **kwargs):
        self.api = api
        self.sku = sku
        self.name = name
        self.__dict__.update(kwargs)

    def __str__(self):
        return f"{self.name} #{self.sku}"
