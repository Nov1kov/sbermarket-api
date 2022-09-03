from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseMeta")


@attr.s(auto_attribs=True)
class SearchProductsResponseMeta:
    """
    Attributes:
        current_page (Union[Unset, int]):
        next_page (Union[Unset, int]):
        previous_page (Union[Unset, str]):
        total_pages (Union[Unset, int]):
        per_page (Union[Unset, int]):
        total_count (Union[Unset, int]):
    """

    current_page: Union[Unset, int] = UNSET
    next_page: Union[Unset, int] = UNSET
    previous_page: Union[Unset, str] = UNSET
    total_pages: Union[Unset, int] = UNSET
    per_page: Union[Unset, int] = UNSET
    total_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_page = self.current_page
        next_page = self.next_page
        previous_page = self.previous_page
        total_pages = self.total_pages
        per_page = self.per_page
        total_count = self.total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if next_page is not UNSET:
            field_dict["next_page"] = next_page
        if previous_page is not UNSET:
            field_dict["previous_page"] = previous_page
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_page = d.pop("current_page", UNSET)

        next_page = d.pop("next_page", UNSET)

        previous_page = d.pop("previous_page", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        per_page = d.pop("per_page", UNSET)

        total_count = d.pop("total_count", UNSET)

        search_products_response_meta = cls(
            current_page=current_page,
            next_page=next_page,
            previous_page=previous_page,
            total_pages=total_pages,
            per_page=per_page,
            total_count=total_count,
        )

        search_products_response_meta.additional_properties = d
        return search_products_response_meta

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
