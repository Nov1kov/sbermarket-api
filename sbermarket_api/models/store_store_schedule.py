from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.store_store_schedule_template import StoreStoreScheduleTemplate
from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreStoreSchedule")


@attr.s(auto_attribs=True)
class StoreStoreSchedule:
    """
    Attributes:
        id (Union[Unset, int]):
        store_id (Union[Unset, int]):
        template (Union[Unset, StoreStoreScheduleTemplate]):
    """

    id: Union[Unset, int] = UNSET
    store_id: Union[Unset, int] = UNSET
    template: Union[Unset, StoreStoreScheduleTemplate] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        store_id = self.store_id
        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if store_id is not UNSET:
            field_dict["store_id"] = store_id
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        store_id = d.pop("store_id", UNSET)

        _template = d.pop("template", UNSET)
        template: Union[Unset, StoreStoreScheduleTemplate]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = StoreStoreScheduleTemplate.from_dict(_template)

        store_store_schedule = cls(
            id=id,
            store_id=store_id,
            template=template,
        )

        store_store_schedule.additional_properties = d
        return store_store_schedule

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
