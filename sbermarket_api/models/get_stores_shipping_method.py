from enum import Enum


class GetStoresShippingMethod(str, Enum):
    DELIVERY = "delivery"

    def __str__(self) -> str:
        return str(self.value)
