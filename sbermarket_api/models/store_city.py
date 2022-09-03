from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreCity")


@attr.s(auto_attribs=True)
class StoreCity:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        name_in (Union[Unset, str]):
        name_from (Union[Unset, str]):
        name_to (Union[Unset, str]):
        slug (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    name_in: Union[Unset, str] = UNSET
    name_from: Union[Unset, str] = UNSET
    name_to: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        name_in = self.name_in
        name_from = self.name_from
        name_to = self.name_to
        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if name_in is not UNSET:
            field_dict["name_in"] = name_in
        if name_from is not UNSET:
            field_dict["name_from"] = name_from
        if name_to is not UNSET:
            field_dict["name_to"] = name_to
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        name_in = d.pop("name_in", UNSET)

        name_from = d.pop("name_from", UNSET)

        name_to = d.pop("name_to", UNSET)

        slug = d.pop("slug", UNSET)

        store_city = cls(
            id=id,
            name=name,
            name_in=name_in,
            name_from=name_from,
            name_to=name_to,
            slug=slug,
        )

        store_city.additional_properties = d
        return store_city

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
