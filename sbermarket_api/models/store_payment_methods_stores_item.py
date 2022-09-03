from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.store_payment_methods_stores_item_payment_method import StorePaymentMethodsStoresItemPaymentMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="StorePaymentMethodsStoresItem")


@attr.s(auto_attribs=True)
class StorePaymentMethodsStoresItem:
    """
    Attributes:
        id (Union[Unset, int]):
        store_id (Union[Unset, int]):
        tenant_id (Union[Unset, str]):
        payment_method (Union[Unset, StorePaymentMethodsStoresItemPaymentMethod]):
    """

    id: Union[Unset, int] = UNSET
    store_id: Union[Unset, int] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    payment_method: Union[Unset, StorePaymentMethodsStoresItemPaymentMethod] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        store_id = self.store_id
        tenant_id = self.tenant_id
        payment_method: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if store_id is not UNSET:
            field_dict["store_id"] = store_id
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        store_id = d.pop("store_id", UNSET)

        tenant_id = d.pop("tenant_id", UNSET)

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: Union[Unset, StorePaymentMethodsStoresItemPaymentMethod]
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = StorePaymentMethodsStoresItemPaymentMethod.from_dict(_payment_method)

        store_payment_methods_stores_item = cls(
            id=id,
            store_id=store_id,
            tenant_id=tenant_id,
            payment_method=payment_method,
        )

        store_payment_methods_stores_item.additional_properties = d
        return store_payment_methods_stores_item

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
