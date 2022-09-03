from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreTenantsItem")


@attr.s(auto_attribs=True)
class StoreTenantsItem:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        hostname (Union[Unset, str]):
        preferred_card_payment_method (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    preferred_card_payment_method: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        hostname = self.hostname
        preferred_card_payment_method = self.preferred_card_payment_method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if preferred_card_payment_method is not UNSET:
            field_dict["preferred_card_payment_method"] = preferred_card_payment_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        hostname = d.pop("hostname", UNSET)

        preferred_card_payment_method = d.pop("preferred_card_payment_method", UNSET)

        store_tenants_item = cls(
            id=id,
            name=name,
            hostname=hostname,
            preferred_card_payment_method=preferred_card_payment_method,
        )

        store_tenants_item.additional_properties = d
        return store_tenants_item

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
