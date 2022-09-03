from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreStoreZonesItem")


@attr.s(auto_attribs=True)
class StoreStoreZonesItem:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        area (Union[Unset, List[List[List[float]]]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    area: Union[Unset, List[List[List[float]]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        area: Union[Unset, List[List[List[float]]]] = UNSET
        if not isinstance(self.area, Unset):
            area = []
            for area_item_data in self.area:
                area_item = []
                for area_item_item_data in area_item_data:
                    area_item_item = area_item_item_data

                    area_item.append(area_item_item)

                area.append(area_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if area is not UNSET:
            field_dict["area"] = area

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        area = []
        _area = d.pop("area", UNSET)
        for area_item_data in _area or []:
            area_item = []
            _area_item = area_item_data
            for area_item_item_data in _area_item:
                area_item_item = cast(List[float], area_item_item_data)

                area_item.append(area_item_item)

            area.append(area_item)

        store_store_zones_item = cls(
            id=id,
            name=name,
            area=area,
        )

        store_store_zones_item.additional_properties = d
        return store_store_zones_item

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
