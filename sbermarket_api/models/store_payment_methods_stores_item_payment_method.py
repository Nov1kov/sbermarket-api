from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorePaymentMethodsStoresItemPaymentMethod")


@attr.s(auto_attribs=True)
class StorePaymentMethodsStoresItemPaymentMethod:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        environment (Union[Unset, str]):
        key (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        environment = self.environment
        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        environment = d.pop("environment", UNSET)

        key = d.pop("key", UNSET)

        store_payment_methods_stores_item_payment_method = cls(
            id=id,
            name=name,
            environment=environment,
            key=key,
        )

        store_payment_methods_stores_item_payment_method.additional_properties = d
        return store_payment_methods_stores_item_payment_method

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
