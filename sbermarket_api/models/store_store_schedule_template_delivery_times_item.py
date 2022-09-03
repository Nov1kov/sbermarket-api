from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreStoreScheduleTemplateDeliveryTimesItem")


@attr.s(auto_attribs=True)
class StoreStoreScheduleTemplateDeliveryTimesItem:
    """
    Attributes:
        start (Union[Unset, str]):
        end (Union[Unset, str]):
        orders_limit (Union[Unset, int]):
        surge_amount (Union[Unset, str]):
        shipment_min_kilos (Union[Unset, str]):
        shipment_max_kilos (Union[Unset, str]):
        shipments_excess_kilos (Union[Unset, str]):
        shipments_excess_items_count (Union[Unset, str]):
        closing_time_gap (Union[Unset, int]):
        kind (Union[Unset, str]):
        store_zone_ids (Union[Unset, List[str]]):
    """

    start: Union[Unset, str] = UNSET
    end: Union[Unset, str] = UNSET
    orders_limit: Union[Unset, int] = UNSET
    surge_amount: Union[Unset, str] = UNSET
    shipment_min_kilos: Union[Unset, str] = UNSET
    shipment_max_kilos: Union[Unset, str] = UNSET
    shipments_excess_kilos: Union[Unset, str] = UNSET
    shipments_excess_items_count: Union[Unset, str] = UNSET
    closing_time_gap: Union[Unset, int] = UNSET
    kind: Union[Unset, str] = UNSET
    store_zone_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start
        end = self.end
        orders_limit = self.orders_limit
        surge_amount = self.surge_amount
        shipment_min_kilos = self.shipment_min_kilos
        shipment_max_kilos = self.shipment_max_kilos
        shipments_excess_kilos = self.shipments_excess_kilos
        shipments_excess_items_count = self.shipments_excess_items_count
        closing_time_gap = self.closing_time_gap
        kind = self.kind
        store_zone_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.store_zone_ids, Unset):
            store_zone_ids = self.store_zone_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if orders_limit is not UNSET:
            field_dict["orders_limit"] = orders_limit
        if surge_amount is not UNSET:
            field_dict["surge_amount"] = surge_amount
        if shipment_min_kilos is not UNSET:
            field_dict["shipment_min_kilos"] = shipment_min_kilos
        if shipment_max_kilos is not UNSET:
            field_dict["shipment_max_kilos"] = shipment_max_kilos
        if shipments_excess_kilos is not UNSET:
            field_dict["shipments_excess_kilos"] = shipments_excess_kilos
        if shipments_excess_items_count is not UNSET:
            field_dict["shipments_excess_items_count"] = shipments_excess_items_count
        if closing_time_gap is not UNSET:
            field_dict["closing_time_gap"] = closing_time_gap
        if kind is not UNSET:
            field_dict["kind"] = kind
        if store_zone_ids is not UNSET:
            field_dict["store_zone_ids"] = store_zone_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        orders_limit = d.pop("orders_limit", UNSET)

        surge_amount = d.pop("surge_amount", UNSET)

        shipment_min_kilos = d.pop("shipment_min_kilos", UNSET)

        shipment_max_kilos = d.pop("shipment_max_kilos", UNSET)

        shipments_excess_kilos = d.pop("shipments_excess_kilos", UNSET)

        shipments_excess_items_count = d.pop("shipments_excess_items_count", UNSET)

        closing_time_gap = d.pop("closing_time_gap", UNSET)

        kind = d.pop("kind", UNSET)

        store_zone_ids = cast(List[str], d.pop("store_zone_ids", UNSET))

        store_store_schedule_template_delivery_times_item = cls(
            start=start,
            end=end,
            orders_limit=orders_limit,
            surge_amount=surge_amount,
            shipment_min_kilos=shipment_min_kilos,
            shipment_max_kilos=shipment_max_kilos,
            shipments_excess_kilos=shipments_excess_kilos,
            shipments_excess_items_count=shipments_excess_items_count,
            closing_time_gap=closing_time_gap,
            kind=kind,
            store_zone_ids=store_zone_ids,
        )

        store_store_schedule_template_delivery_times_item.additional_properties = d
        return store_store_schedule_template_delivery_times_item

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
