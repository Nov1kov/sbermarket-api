from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.store_store_schedule_template_delivery_times_item import StoreStoreScheduleTemplateDeliveryTimesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreStoreScheduleTemplate")


@attr.s(auto_attribs=True)
class StoreStoreScheduleTemplate:
    """
    Attributes:
        delivery_times (Union[Unset, List[StoreStoreScheduleTemplateDeliveryTimesItem]]):
    """

    delivery_times: Union[Unset, List[StoreStoreScheduleTemplateDeliveryTimesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delivery_times: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.delivery_times, Unset):
            delivery_times = []
            for delivery_times_item_data in self.delivery_times:
                delivery_times_item = delivery_times_item_data.to_dict()

                delivery_times.append(delivery_times_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_times is not UNSET:
            field_dict["delivery_times"] = delivery_times

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delivery_times = []
        _delivery_times = d.pop("delivery_times", UNSET)
        for delivery_times_item_data in _delivery_times or []:
            delivery_times_item = StoreStoreScheduleTemplateDeliveryTimesItem.from_dict(delivery_times_item_data)

            delivery_times.append(delivery_times_item)

        store_store_schedule_template = cls(
            delivery_times=delivery_times,
        )

        store_store_schedule_template.additional_properties = d
        return store_store_schedule_template

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
