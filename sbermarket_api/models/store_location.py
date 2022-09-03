from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreLocation")


@attr.s(auto_attribs=True)
class StoreLocation:
    """
    Attributes:
        id (Union[Unset, int]):
        full_address (Union[Unset, str]):
        city (Union[Unset, str]):
        street (Union[Unset, str]):
        building (Union[Unset, str]):
        block (Union[Unset, str]):
        floor (Union[Unset, str]):
        apartment (Union[Unset, str]):
        entrance (Union[Unset, str]):
        elevator (Union[Unset, str]):
        region (Union[Unset, str]):
        comments (Union[Unset, str]):
        phone (Union[Unset, str]):
        area (Union[Unset, str]):
        settlement (Union[Unset, str]):
        lat (Union[Unset, float]):
        lon (Union[Unset, float]):
        city_kladr_id (Union[Unset, str]):
        street_kladr_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        door_phone (Union[Unset, str]):
        kind (Union[Unset, str]):
        delivery_to_door (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    full_address: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    building: Union[Unset, str] = UNSET
    block: Union[Unset, str] = UNSET
    floor: Union[Unset, str] = UNSET
    apartment: Union[Unset, str] = UNSET
    entrance: Union[Unset, str] = UNSET
    elevator: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    area: Union[Unset, str] = UNSET
    settlement: Union[Unset, str] = UNSET
    lat: Union[Unset, float] = UNSET
    lon: Union[Unset, float] = UNSET
    city_kladr_id: Union[Unset, str] = UNSET
    street_kladr_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    door_phone: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    delivery_to_door: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        full_address = self.full_address
        city = self.city
        street = self.street
        building = self.building
        block = self.block
        floor = self.floor
        apartment = self.apartment
        entrance = self.entrance
        elevator = self.elevator
        region = self.region
        comments = self.comments
        phone = self.phone
        area = self.area
        settlement = self.settlement
        lat = self.lat
        lon = self.lon
        city_kladr_id = self.city_kladr_id
        street_kladr_id = self.street_kladr_id
        user_id = self.user_id
        door_phone = self.door_phone
        kind = self.kind
        delivery_to_door = self.delivery_to_door

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if full_address is not UNSET:
            field_dict["full_address"] = full_address
        if city is not UNSET:
            field_dict["city"] = city
        if street is not UNSET:
            field_dict["street"] = street
        if building is not UNSET:
            field_dict["building"] = building
        if block is not UNSET:
            field_dict["block"] = block
        if floor is not UNSET:
            field_dict["floor"] = floor
        if apartment is not UNSET:
            field_dict["apartment"] = apartment
        if entrance is not UNSET:
            field_dict["entrance"] = entrance
        if elevator is not UNSET:
            field_dict["elevator"] = elevator
        if region is not UNSET:
            field_dict["region"] = region
        if comments is not UNSET:
            field_dict["comments"] = comments
        if phone is not UNSET:
            field_dict["phone"] = phone
        if area is not UNSET:
            field_dict["area"] = area
        if settlement is not UNSET:
            field_dict["settlement"] = settlement
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon
        if city_kladr_id is not UNSET:
            field_dict["city_kladr_id"] = city_kladr_id
        if street_kladr_id is not UNSET:
            field_dict["street_kladr_id"] = street_kladr_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if door_phone is not UNSET:
            field_dict["door_phone"] = door_phone
        if kind is not UNSET:
            field_dict["kind"] = kind
        if delivery_to_door is not UNSET:
            field_dict["delivery_to_door"] = delivery_to_door

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        full_address = d.pop("full_address", UNSET)

        city = d.pop("city", UNSET)

        street = d.pop("street", UNSET)

        building = d.pop("building", UNSET)

        block = d.pop("block", UNSET)

        floor = d.pop("floor", UNSET)

        apartment = d.pop("apartment", UNSET)

        entrance = d.pop("entrance", UNSET)

        elevator = d.pop("elevator", UNSET)

        region = d.pop("region", UNSET)

        comments = d.pop("comments", UNSET)

        phone = d.pop("phone", UNSET)

        area = d.pop("area", UNSET)

        settlement = d.pop("settlement", UNSET)

        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        city_kladr_id = d.pop("city_kladr_id", UNSET)

        street_kladr_id = d.pop("street_kladr_id", UNSET)

        user_id = d.pop("user_id", UNSET)

        door_phone = d.pop("door_phone", UNSET)

        kind = d.pop("kind", UNSET)

        delivery_to_door = d.pop("delivery_to_door", UNSET)

        store_location = cls(
            id=id,
            full_address=full_address,
            city=city,
            street=street,
            building=building,
            block=block,
            floor=floor,
            apartment=apartment,
            entrance=entrance,
            elevator=elevator,
            region=region,
            comments=comments,
            phone=phone,
            area=area,
            settlement=settlement,
            lat=lat,
            lon=lon,
            city_kladr_id=city_kladr_id,
            street_kladr_id=street_kladr_id,
            user_id=user_id,
            door_phone=door_phone,
            kind=kind,
            delivery_to_door=delivery_to_door,
        )

        store_location.additional_properties = d
        return store_location

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
