from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.store_retailer_appearance import StoreRetailerAppearance
from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreRetailer")


@attr.s(auto_attribs=True)
class StoreRetailer:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        color (Union[Unset, str]):
        secondary_color (Union[Unset, str]):
        logo (Union[Unset, str]):
        logo_background_color (Union[Unset, str]):
        slug (Union[Unset, str]):
        description (Union[Unset, str]):
        icon (Union[Unset, str]):
        is_alcohol (Union[Unset, bool]):
        is_agent_contract_types (Union[Unset, bool]):
        home_page_departments_depth (Union[Unset, int]):
        appearance (Union[Unset, StoreRetailerAppearance]):
        services (Union[Unset, List[str]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    secondary_color: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    logo_background_color: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    is_alcohol: Union[Unset, bool] = UNSET
    is_agent_contract_types: Union[Unset, bool] = UNSET
    home_page_departments_depth: Union[Unset, int] = UNSET
    appearance: Union[Unset, StoreRetailerAppearance] = UNSET
    services: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        color = self.color
        secondary_color = self.secondary_color
        logo = self.logo
        logo_background_color = self.logo_background_color
        slug = self.slug
        description = self.description
        icon = self.icon
        is_alcohol = self.is_alcohol
        is_agent_contract_types = self.is_agent_contract_types
        home_page_departments_depth = self.home_page_departments_depth
        appearance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        services: Union[Unset, List[str]] = UNSET
        if not isinstance(self.services, Unset):
            services = self.services

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if color is not UNSET:
            field_dict["color"] = color
        if secondary_color is not UNSET:
            field_dict["secondary_color"] = secondary_color
        if logo is not UNSET:
            field_dict["logo"] = logo
        if logo_background_color is not UNSET:
            field_dict["logo_background_color"] = logo_background_color
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if is_alcohol is not UNSET:
            field_dict["is_alcohol"] = is_alcohol
        if is_agent_contract_types is not UNSET:
            field_dict["is_agent_contract_types"] = is_agent_contract_types
        if home_page_departments_depth is not UNSET:
            field_dict["home_page_departments_depth"] = home_page_departments_depth
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        color = d.pop("color", UNSET)

        secondary_color = d.pop("secondary_color", UNSET)

        logo = d.pop("logo", UNSET)

        logo_background_color = d.pop("logo_background_color", UNSET)

        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        is_alcohol = d.pop("is_alcohol", UNSET)

        is_agent_contract_types = d.pop("is_agent_contract_types", UNSET)

        home_page_departments_depth = d.pop("home_page_departments_depth", UNSET)

        _appearance = d.pop("appearance", UNSET)
        appearance: Union[Unset, StoreRetailerAppearance]
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = StoreRetailerAppearance.from_dict(_appearance)

        services = cast(List[str], d.pop("services", UNSET))

        store_retailer = cls(
            id=id,
            name=name,
            color=color,
            secondary_color=secondary_color,
            logo=logo,
            logo_background_color=logo_background_color,
            slug=slug,
            description=description,
            icon=icon,
            is_alcohol=is_alcohol,
            is_agent_contract_types=is_agent_contract_types,
            home_page_departments_depth=home_page_departments_depth,
            appearance=appearance,
            services=services,
        )

        store_retailer.additional_properties = d
        return store_retailer

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
