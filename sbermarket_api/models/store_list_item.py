from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.store_list_item_shipping_methods_item import StoreListItemShippingMethodsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreListItem")


@attr.s(auto_attribs=True)
class StoreListItem:
    """
    Attributes:
        id (Union[Unset, str]):
        store_id (Union[Unset, int]):
        name (Union[Unset, str]):
        min_order_amount (Union[Unset, int]):
        min_order_amount_pickup (Union[Unset, int]):
        min_first_order_amount (Union[Unset, int]):
        min_first_order_amount_pickup (Union[Unset, int]):
        delivery_forecast_text (Union[Unset, str]):
        on_demand (Union[Unset, bool]):
        express_delivery (Union[Unset, bool]):
        minimum_order_amount (Union[Unset, int]):
        minimum_order_amount_pickup (Union[Unset, int]):
        shipping_methods (Union[Unset, List[StoreListItemShippingMethodsItem]]):
    """

    id: Union[Unset, str] = UNSET
    store_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    min_order_amount: Union[Unset, int] = UNSET
    min_order_amount_pickup: Union[Unset, int] = UNSET
    min_first_order_amount: Union[Unset, int] = UNSET
    min_first_order_amount_pickup: Union[Unset, int] = UNSET
    delivery_forecast_text: Union[Unset, str] = UNSET
    on_demand: Union[Unset, bool] = UNSET
    express_delivery: Union[Unset, bool] = UNSET
    minimum_order_amount: Union[Unset, int] = UNSET
    minimum_order_amount_pickup: Union[Unset, int] = UNSET
    shipping_methods: Union[Unset, List[StoreListItemShippingMethodsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        store_id = self.store_id
        name = self.name
        min_order_amount = self.min_order_amount
        min_order_amount_pickup = self.min_order_amount_pickup
        min_first_order_amount = self.min_first_order_amount
        min_first_order_amount_pickup = self.min_first_order_amount_pickup
        delivery_forecast_text = self.delivery_forecast_text
        on_demand = self.on_demand
        express_delivery = self.express_delivery
        minimum_order_amount = self.minimum_order_amount
        minimum_order_amount_pickup = self.minimum_order_amount_pickup
        shipping_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipping_methods, Unset):
            shipping_methods = []
            for shipping_methods_item_data in self.shipping_methods:
                shipping_methods_item = shipping_methods_item_data.to_dict()

                shipping_methods.append(shipping_methods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if store_id is not UNSET:
            field_dict["store_id"] = store_id
        if name is not UNSET:
            field_dict["name"] = name
        if min_order_amount is not UNSET:
            field_dict["min_order_amount"] = min_order_amount
        if min_order_amount_pickup is not UNSET:
            field_dict["min_order_amount_pickup"] = min_order_amount_pickup
        if min_first_order_amount is not UNSET:
            field_dict["min_first_order_amount"] = min_first_order_amount
        if min_first_order_amount_pickup is not UNSET:
            field_dict["min_first_order_amount_pickup"] = min_first_order_amount_pickup
        if delivery_forecast_text is not UNSET:
            field_dict["delivery_forecast_text"] = delivery_forecast_text
        if on_demand is not UNSET:
            field_dict["on_demand"] = on_demand
        if express_delivery is not UNSET:
            field_dict["express_delivery"] = express_delivery
        if minimum_order_amount is not UNSET:
            field_dict["minimum_order_amount"] = minimum_order_amount
        if minimum_order_amount_pickup is not UNSET:
            field_dict["minimum_order_amount_pickup"] = minimum_order_amount_pickup
        if shipping_methods is not UNSET:
            field_dict["shipping_methods"] = shipping_methods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        store_id = d.pop("store_id", UNSET)

        name = d.pop("name", UNSET)

        min_order_amount = d.pop("min_order_amount", UNSET)

        min_order_amount_pickup = d.pop("min_order_amount_pickup", UNSET)

        min_first_order_amount = d.pop("min_first_order_amount", UNSET)

        min_first_order_amount_pickup = d.pop("min_first_order_amount_pickup", UNSET)

        delivery_forecast_text = d.pop("delivery_forecast_text", UNSET)

        on_demand = d.pop("on_demand", UNSET)

        express_delivery = d.pop("express_delivery", UNSET)

        minimum_order_amount = d.pop("minimum_order_amount", UNSET)

        minimum_order_amount_pickup = d.pop("minimum_order_amount_pickup", UNSET)

        shipping_methods = []
        _shipping_methods = d.pop("shipping_methods", UNSET)
        for shipping_methods_item_data in _shipping_methods or []:
            shipping_methods_item = StoreListItemShippingMethodsItem.from_dict(shipping_methods_item_data)

            shipping_methods.append(shipping_methods_item)

        store_list_item = cls(
            id=id,
            store_id=store_id,
            name=name,
            min_order_amount=min_order_amount,
            min_order_amount_pickup=min_order_amount_pickup,
            min_first_order_amount=min_first_order_amount,
            min_first_order_amount_pickup=min_first_order_amount_pickup,
            delivery_forecast_text=delivery_forecast_text,
            on_demand=on_demand,
            express_delivery=express_delivery,
            minimum_order_amount=minimum_order_amount,
            minimum_order_amount_pickup=minimum_order_amount_pickup,
            shipping_methods=shipping_methods,
        )

        store_list_item.additional_properties = d
        return store_list_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
