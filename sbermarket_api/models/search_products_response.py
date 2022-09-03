from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.search_products_response_facets_item import SearchProductsResponseFacetsItem
from ..models.search_products_response_meta import SearchProductsResponseMeta
from ..models.search_products_response_private_filters import SearchProductsResponsePrivateFilters
from ..models.search_products_response_products_item import SearchProductsResponseProductsItem
from ..models.search_products_response_root_categories import SearchProductsResponseRootCategories
from ..models.search_products_response_sort_item import SearchProductsResponseSortItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponse")


@attr.s(auto_attribs=True)
class SearchProductsResponse:
    """
    Attributes:
        products (Union[Unset, List[SearchProductsResponseProductsItem]]):
        meta (Union[Unset, SearchProductsResponseMeta]):
        facets (Union[Unset, List[SearchProductsResponseFacetsItem]]):
        sort (Union[Unset, List[SearchProductsResponseSortItem]]):
        root_categories (Union[Unset, SearchProductsResponseRootCategories]):
        private_filters (Union[Unset, SearchProductsResponsePrivateFilters]):
        promo_badges (Union[Unset, List[str]]):
    """

    products: Union[Unset, List[SearchProductsResponseProductsItem]] = UNSET
    meta: Union[Unset, SearchProductsResponseMeta] = UNSET
    facets: Union[Unset, List[SearchProductsResponseFacetsItem]] = UNSET
    sort: Union[Unset, List[SearchProductsResponseSortItem]] = UNSET
    root_categories: Union[Unset, SearchProductsResponseRootCategories] = UNSET
    private_filters: Union[Unset, SearchProductsResponsePrivateFilters] = UNSET
    promo_badges: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()

                products.append(products_item)

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        facets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.facets, Unset):
            facets = []
            for facets_item_data in self.facets:
                facets_item = facets_item_data.to_dict()

                facets.append(facets_item)

        sort: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = []
            for sort_item_data in self.sort:
                sort_item = sort_item_data.to_dict()

                sort.append(sort_item)

        root_categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.root_categories, Unset):
            root_categories = self.root_categories.to_dict()

        private_filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private_filters, Unset):
            private_filters = self.private_filters.to_dict()

        promo_badges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.promo_badges, Unset):
            promo_badges = self.promo_badges

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if products is not UNSET:
            field_dict["products"] = products
        if meta is not UNSET:
            field_dict["meta"] = meta
        if facets is not UNSET:
            field_dict["facets"] = facets
        if sort is not UNSET:
            field_dict["sort"] = sort
        if root_categories is not UNSET:
            field_dict["root_categories"] = root_categories
        if private_filters is not UNSET:
            field_dict["private_filters"] = private_filters
        if promo_badges is not UNSET:
            field_dict["promo_badges"] = promo_badges

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = SearchProductsResponseProductsItem.from_dict(products_item_data)

            products.append(products_item)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, SearchProductsResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SearchProductsResponseMeta.from_dict(_meta)

        facets = []
        _facets = d.pop("facets", UNSET)
        for facets_item_data in _facets or []:
            facets_item = SearchProductsResponseFacetsItem.from_dict(facets_item_data)

            facets.append(facets_item)

        sort = []
        _sort = d.pop("sort", UNSET)
        for sort_item_data in _sort or []:
            sort_item = SearchProductsResponseSortItem.from_dict(sort_item_data)

            sort.append(sort_item)

        _root_categories = d.pop("root_categories", UNSET)
        root_categories: Union[Unset, SearchProductsResponseRootCategories]
        if isinstance(_root_categories, Unset):
            root_categories = UNSET
        else:
            root_categories = SearchProductsResponseRootCategories.from_dict(_root_categories)

        _private_filters = d.pop("private_filters", UNSET)
        private_filters: Union[Unset, SearchProductsResponsePrivateFilters]
        if isinstance(_private_filters, Unset):
            private_filters = UNSET
        else:
            private_filters = SearchProductsResponsePrivateFilters.from_dict(_private_filters)

        promo_badges = cast(List[str], d.pop("promo_badges", UNSET))

        search_products_response = cls(
            products=products,
            meta=meta,
            facets=facets,
            sort=sort,
            root_categories=root_categories,
            private_filters=private_filters,
            promo_badges=promo_badges,
        )

        search_products_response.additional_properties = d
        return search_products_response

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
