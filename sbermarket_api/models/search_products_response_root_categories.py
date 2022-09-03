from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.search_products_response_root_categories_options_item import (
    SearchProductsResponseRootCategoriesOptionsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseRootCategories")


@attr.s(auto_attribs=True)
class SearchProductsResponseRootCategories:
    """
    Attributes:
        key (Union[Unset, str]):
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        options (Union[Unset, List[SearchProductsResponseRootCategoriesOptionsItem]]):
    """

    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    options: Union[Unset, List[SearchProductsResponseRootCategoriesOptionsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        name = self.name
        type = self.type
        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = SearchProductsResponseRootCategoriesOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        search_products_response_root_categories = cls(
            key=key,
            name=name,
            type=type,
            options=options,
        )

        search_products_response_root_categories.additional_properties = d
        return search_products_response_root_categories

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
