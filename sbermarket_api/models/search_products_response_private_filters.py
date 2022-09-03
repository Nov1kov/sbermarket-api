from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponsePrivateFilters")


@attr.s(auto_attribs=True)
class SearchProductsResponsePrivateFilters:
    """
    Attributes:
        in_stock (Union[Unset, bool]):
        with_similar (Union[Unset, bool]):
    """

    in_stock: Union[Unset, bool] = UNSET
    with_similar: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        in_stock = self.in_stock
        with_similar = self.with_similar

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_stock is not UNSET:
            field_dict["in_stock"] = in_stock
        if with_similar is not UNSET:
            field_dict["with_similar"] = with_similar

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        in_stock = d.pop("in_stock", UNSET)

        with_similar = d.pop("with_similar", UNSET)

        search_products_response_private_filters = cls(
            in_stock=in_stock,
            with_similar=with_similar,
        )

        search_products_response_private_filters.additional_properties = d
        return search_products_response_private_filters

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
