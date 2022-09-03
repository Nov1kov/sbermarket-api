from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseSortItem")


@attr.s(auto_attribs=True)
class SearchProductsResponseSortItem:
    """
    Attributes:
        key (Union[Unset, str]):
        name (Union[Unset, str]):
        order (Union[Unset, str]):
        active (Union[Unset, bool]):
    """

    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        name = self.name
        order = self.order
        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if order is not UNSET:
            field_dict["order"] = order
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        order = d.pop("order", UNSET)

        active = d.pop("active", UNSET)

        search_products_response_sort_item = cls(
            key=key,
            name=name,
            order=order,
            active=active,
        )

        search_products_response_sort_item.additional_properties = d
        return search_products_response_sort_item

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
