from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseRootCategoriesOptionsItem")


@attr.s(auto_attribs=True)
class SearchProductsResponseRootCategoriesOptionsItem:
    """
    Attributes:
        name (Union[Unset, str]):
        permalink (Union[Unset, str]):
        value (Union[Unset, int]):
        count (Union[Unset, int]):
        active (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    permalink: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        permalink = self.permalink
        value = self.value
        count = self.count
        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if value is not UNSET:
            field_dict["value"] = value
        if count is not UNSET:
            field_dict["count"] = count
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        permalink = d.pop("permalink", UNSET)

        value = d.pop("value", UNSET)

        count = d.pop("count", UNSET)

        active = d.pop("active", UNSET)

        search_products_response_root_categories_options_item = cls(
            name=name,
            permalink=permalink,
            value=value,
            count=count,
            active=active,
        )

        search_products_response_root_categories_options_item.additional_properties = d
        return search_products_response_root_categories_options_item

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
