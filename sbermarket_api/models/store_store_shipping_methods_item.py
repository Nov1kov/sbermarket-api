from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.store_store_shipping_methods_item_shipping_method import StoreStoreShippingMethodsItemShippingMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreStoreShippingMethodsItem")


@attr.s(auto_attribs=True)
class StoreStoreShippingMethodsItem:
    """
    Attributes:
        id (Union[Unset, int]):
        store_id (Union[Unset, int]):
        tenant_id (Union[Unset, str]):
        available_on (Union[Unset, str]):
        shipping_method (Union[Unset, StoreStoreShippingMethodsItemShippingMethod]):
    """

    id: Union[Unset, int] = UNSET
    store_id: Union[Unset, int] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    available_on: Union[Unset, str] = UNSET
    shipping_method: Union[Unset, StoreStoreShippingMethodsItemShippingMethod] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        store_id = self.store_id
        tenant_id = self.tenant_id
        available_on = self.available_on
        shipping_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_method, Unset):
            shipping_method = self.shipping_method.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if store_id is not UNSET:
            field_dict["store_id"] = store_id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if available_on is not UNSET:
            field_dict["available_on"] = available_on
        if shipping_method is not UNSET:
            field_dict["shipping_method"] = shipping_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        store_id = d.pop("store_id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        available_on = d.pop("available_on", UNSET)

        _shipping_method = d.pop("shipping_method", UNSET)
        shipping_method: Union[Unset, StoreStoreShippingMethodsItemShippingMethod]
        if isinstance(_shipping_method, Unset):
            shipping_method = UNSET
        else:
            shipping_method = StoreStoreShippingMethodsItemShippingMethod.from_dict(_shipping_method)

        store_store_shipping_methods_item = cls(
            id=id,
            store_id=store_id,
            tenant_id=tenant_id,
            available_on=available_on,
            shipping_method=shipping_method,
        )

        store_store_shipping_methods_item.additional_properties = d
        return store_store_shipping_methods_item

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
