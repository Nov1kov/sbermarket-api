from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import datetime

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreLicensesItem")


@attr.s(auto_attribs=True)
class StoreLicensesItem:
    """
    Attributes:
        kind (Union[Unset, str]):
        number (Union[Unset, str]):
        issue_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
    """

    kind: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    issue_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind
        number = self.number
        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if number is not UNSET:
            field_dict["number"] = number
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = d.pop("kind", UNSET)

        number = d.pop("number", UNSET)

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: Union[Unset, datetime.date]
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date).date()

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        store_licenses_item = cls(
            kind=kind,
            number=number,
            issue_date=issue_date,
            end_date=end_date,
        )

        store_licenses_item.additional_properties = d
        return store_licenses_item

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
