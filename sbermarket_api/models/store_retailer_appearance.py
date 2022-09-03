from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreRetailerAppearance")


@attr.s(auto_attribs=True)
class StoreRetailerAppearance:
    """
    Attributes:
        background_color (Union[Unset, str]):
        image_color (Union[Unset, str]):
        black_theme (Union[Unset, bool]):
        logo_image (Union[Unset, str]):
        side_image (Union[Unset, str]):
        mini_logo_image (Union[Unset, str]):
    """

    background_color: Union[Unset, str] = UNSET
    image_color: Union[Unset, str] = UNSET
    black_theme: Union[Unset, bool] = UNSET
    logo_image: Union[Unset, str] = UNSET
    side_image: Union[Unset, str] = UNSET
    mini_logo_image: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        background_color = self.background_color
        image_color = self.image_color
        black_theme = self.black_theme
        logo_image = self.logo_image
        side_image = self.side_image
        mini_logo_image = self.mini_logo_image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background_color is not UNSET:
            field_dict["background_color"] = background_color
        if image_color is not UNSET:
            field_dict["image_color"] = image_color
        if black_theme is not UNSET:
            field_dict["black_theme"] = black_theme
        if logo_image is not UNSET:
            field_dict["logo_image"] = logo_image
        if side_image is not UNSET:
            field_dict["side_image"] = side_image
        if mini_logo_image is not UNSET:
            field_dict["mini_logo_image"] = mini_logo_image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        background_color = d.pop("background_color", UNSET)

        image_color = d.pop("image_color", UNSET)

        black_theme = d.pop("black_theme", UNSET)

        logo_image = d.pop("logo_image", UNSET)

        side_image = d.pop("side_image", UNSET)

        mini_logo_image = d.pop("mini_logo_image", UNSET)

        store_retailer_appearance = cls(
            background_color=background_color,
            image_color=image_color,
            black_theme=black_theme,
            logo_image=logo_image,
            side_image=side_image,
            mini_logo_image=mini_logo_image,
        )

        store_retailer_appearance.additional_properties = d
        return store_retailer_appearance

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
