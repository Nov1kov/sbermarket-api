from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreStoreShippingMethodsItemShippingMethod")


@attr.s(auto_attribs=True)
class StoreStoreShippingMethodsItemShippingMethod:
    """
    Attributes:
        name (Union[Unset, str]):
        kind (Union[Unset, str]):
        id (Union[Unset, int]):
    """

    name: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        kind = self.kind
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        kind = d.pop("kind", UNSET)

        id = d.pop("id", UNSET)

        store_store_shipping_methods_item_shipping_method = cls(
            name=name,
            kind=kind,
            id=id,
        )

        store_store_shipping_methods_item_shipping_method.additional_properties = d
        return store_store_shipping_methods_item_shipping_method

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
