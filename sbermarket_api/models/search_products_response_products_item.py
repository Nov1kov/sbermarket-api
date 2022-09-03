from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseProductsItem")


@attr.s(auto_attribs=True)
class SearchProductsResponseProductsItem:
    """
    Attributes:
        id (Union[Unset, str]):
        legacy_offer_id (Union[Unset, int]):
        legacy_product_id (Union[Unset, int]):
        sku (Union[Unset, str]):
        retailer_sku (Union[Unset, str]):
        name (Union[Unset, str]):
        price (Union[Unset, int]):
        original_price (Union[Unset, int]):
        discount (Union[Unset, int]):
        human_volume (Union[Unset, str]):
        volume (Union[Unset, int]):
        volume_type (Union[Unset, str]):
        items_per_pack (Union[Unset, int]):
        discount_ends_at (Union[Unset, str]):
        price_type (Union[Unset, str]):
        grams_per_unit (Union[Unset, int]):
        unit_price (Union[Unset, int]):
        original_unit_price (Union[Unset, int]):
        slug (Union[Unset, str]):
        max_select_quantity (Union[Unset, int]):
        canonical_url (Union[Unset, str]):
        available (Union[Unset, bool]):
        vat_info (Union[Unset, str]):
        bmpl_info (Union[Unset, str]):
        promo_badge_ids (Union[Unset, List[str]]):
        requirements (Union[Unset, List[str]]):
        image_urls (Union[Unset, List[str]]):
    """

    id: Union[Unset, str] = UNSET
    legacy_offer_id: Union[Unset, int] = UNSET
    legacy_product_id: Union[Unset, int] = UNSET
    sku: Union[Unset, str] = UNSET
    retailer_sku: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    price: Union[Unset, int] = UNSET
    original_price: Union[Unset, int] = UNSET
    discount: Union[Unset, int] = UNSET
    human_volume: Union[Unset, str] = UNSET
    volume: Union[Unset, int] = UNSET
    volume_type: Union[Unset, str] = UNSET
    items_per_pack: Union[Unset, int] = UNSET
    discount_ends_at: Union[Unset, str] = UNSET
    price_type: Union[Unset, str] = UNSET
    grams_per_unit: Union[Unset, int] = UNSET
    unit_price: Union[Unset, int] = UNSET
    original_unit_price: Union[Unset, int] = UNSET
    slug: Union[Unset, str] = UNSET
    max_select_quantity: Union[Unset, int] = UNSET
    canonical_url: Union[Unset, str] = UNSET
    available: Union[Unset, bool] = UNSET
    vat_info: Union[Unset, str] = UNSET
    bmpl_info: Union[Unset, str] = UNSET
    promo_badge_ids: Union[Unset, List[str]] = UNSET
    requirements: Union[Unset, List[str]] = UNSET
    image_urls: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        legacy_offer_id = self.legacy_offer_id
        legacy_product_id = self.legacy_product_id
        sku = self.sku
        retailer_sku = self.retailer_sku
        name = self.name
        price = self.price
        original_price = self.original_price
        discount = self.discount
        human_volume = self.human_volume
        volume = self.volume
        volume_type = self.volume_type
        items_per_pack = self.items_per_pack
        discount_ends_at = self.discount_ends_at
        price_type = self.price_type
        grams_per_unit = self.grams_per_unit
        unit_price = self.unit_price
        original_unit_price = self.original_unit_price
        slug = self.slug
        max_select_quantity = self.max_select_quantity
        canonical_url = self.canonical_url
        available = self.available
        vat_info = self.vat_info
        bmpl_info = self.bmpl_info
        promo_badge_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.promo_badge_ids, Unset):
            promo_badge_ids = self.promo_badge_ids

        requirements: Union[Unset, List[str]] = UNSET
        if not isinstance(self.requirements, Unset):
            requirements = self.requirements

        image_urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.image_urls, Unset):
            image_urls = self.image_urls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if legacy_offer_id is not UNSET:
            field_dict["legacy_offer_id"] = legacy_offer_id
        if legacy_product_id is not UNSET:
            field_dict["legacy_product_id"] = legacy_product_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if retailer_sku is not UNSET:
            field_dict["retailer_sku"] = retailer_sku
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if original_price is not UNSET:
            field_dict["original_price"] = original_price
        if discount is not UNSET:
            field_dict["discount"] = discount
        if human_volume is not UNSET:
            field_dict["human_volume"] = human_volume
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_type is not UNSET:
            field_dict["volume_type"] = volume_type
        if items_per_pack is not UNSET:
            field_dict["items_per_pack"] = items_per_pack
        if discount_ends_at is not UNSET:
            field_dict["discount_ends_at"] = discount_ends_at
        if price_type is not UNSET:
            field_dict["price_type"] = price_type
        if grams_per_unit is not UNSET:
            field_dict["grams_per_unit"] = grams_per_unit
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if original_unit_price is not UNSET:
            field_dict["original_unit_price"] = original_unit_price
        if slug is not UNSET:
            field_dict["slug"] = slug
        if max_select_quantity is not UNSET:
            field_dict["max_select_quantity"] = max_select_quantity
        if canonical_url is not UNSET:
            field_dict["canonical_url"] = canonical_url
        if available is not UNSET:
            field_dict["available"] = available
        if vat_info is not UNSET:
            field_dict["vat_info"] = vat_info
        if bmpl_info is not UNSET:
            field_dict["bmpl_info"] = bmpl_info
        if promo_badge_ids is not UNSET:
            field_dict["promo_badge_ids"] = promo_badge_ids
        if requirements is not UNSET:
            field_dict["requirements"] = requirements
        if image_urls is not UNSET:
            field_dict["image_urls"] = image_urls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        legacy_offer_id = d.pop("legacy_offer_id", UNSET)

        legacy_product_id = d.pop("legacy_product_id", UNSET)

        sku = d.pop("sku", UNSET)

        retailer_sku = d.pop("retailer_sku", UNSET)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        original_price = d.pop("original_price", UNSET)

        discount = d.pop("discount", UNSET)

        human_volume = d.pop("human_volume", UNSET)

        volume = d.pop("volume", UNSET)

        volume_type = d.pop("volume_type", UNSET)

        items_per_pack = d.pop("items_per_pack", UNSET)

        discount_ends_at = d.pop("discount_ends_at", UNSET)

        price_type = d.pop("price_type", UNSET)

        grams_per_unit = d.pop("grams_per_unit", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        original_unit_price = d.pop("original_unit_price", UNSET)

        slug = d.pop("slug", UNSET)

        max_select_quantity = d.pop("max_select_quantity", UNSET)

        canonical_url = d.pop("canonical_url", UNSET)

        available = d.pop("available", UNSET)

        vat_info = d.pop("vat_info", UNSET)

        bmpl_info = d.pop("bmpl_info", UNSET)

        promo_badge_ids = cast(List[str], d.pop("promo_badge_ids", UNSET))

        requirements = cast(List[str], d.pop("requirements", UNSET))

        image_urls = cast(List[str], d.pop("image_urls", UNSET))

        search_products_response_products_item = cls(
            id=id,
            legacy_offer_id=legacy_offer_id,
            legacy_product_id=legacy_product_id,
            sku=sku,
            retailer_sku=retailer_sku,
            name=name,
            price=price,
            original_price=original_price,
            discount=discount,
            human_volume=human_volume,
            volume=volume,
            volume_type=volume_type,
            items_per_pack=items_per_pack,
            discount_ends_at=discount_ends_at,
            price_type=price_type,
            grams_per_unit=grams_per_unit,
            unit_price=unit_price,
            original_unit_price=original_unit_price,
            slug=slug,
            max_select_quantity=max_select_quantity,
            canonical_url=canonical_url,
            available=available,
            vat_info=vat_info,
            bmpl_info=bmpl_info,
            promo_badge_ids=promo_badge_ids,
            requirements=requirements,
            image_urls=image_urls,
        )

        search_products_response_products_item.additional_properties = d
        return search_products_response_products_item

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
