from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_stores_shipping_method import GetStoresShippingMethod
from ...models.store_list_item import StoreListItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    shipping_method: Union[Unset, None, GetStoresShippingMethod] = GetStoresShippingMethod.DELIVERY,
    lat: Union[Unset, None, str] = UNSET,
    lon: Union[Unset, None, str] = UNSET,
    api_version: Union[Unset, str] = "3.0",
) -> Dict[str, Any]:
    url = f"{client.base_url}/stores"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(api_version, Unset):
        headers["api-version"] = api_version

    params: Dict[str, Any] = {}
    json_shipping_method: Union[Unset, None, str] = UNSET
    if not isinstance(shipping_method, Unset):
        json_shipping_method = shipping_method.value if shipping_method else None

    params["shipping_method"] = json_shipping_method

    params["lat"] = lat

    params["lon"] = lon

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[StoreListItem]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StoreListItem.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[StoreListItem]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    shipping_method: Union[Unset, None, GetStoresShippingMethod] = GetStoresShippingMethod.DELIVERY,
    lat: Union[Unset, None, str] = UNSET,
    lon: Union[Unset, None, str] = UNSET,
    api_version: Union[Unset, str] = "3.0",
) -> Response[Union[Any, List[StoreListItem]]]:
    """Получить все магазины вокруг данной точки

    Args:
        shipping_method (Union[Unset, None, GetStoresShippingMethod]):  Default:
            GetStoresShippingMethod.DELIVERY.
        lat (Union[Unset, None, str]):
        lon (Union[Unset, None, str]):
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, List[StoreListItem]]]
    """

    kwargs = _get_kwargs(
        client=client,
        shipping_method=shipping_method,
        lat=lat,
        lon=lon,
        api_version=api_version,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    client.set_cookies(dict(response.cookies))
    return _build_response(response=response)


def sync(
    *,
    client: Client,
    shipping_method: Union[Unset, None, GetStoresShippingMethod] = GetStoresShippingMethod.DELIVERY,
    lat: Union[Unset, None, str] = UNSET,
    lon: Union[Unset, None, str] = UNSET,
    api_version: Union[Unset, str] = "3.0",
) -> Optional[Union[Any, List[StoreListItem]]]:
    """Получить все магазины вокруг данной точки

    Args:
        shipping_method (Union[Unset, None, GetStoresShippingMethod]):  Default:
            GetStoresShippingMethod.DELIVERY.
        lat (Union[Unset, None, str]):
        lon (Union[Unset, None, str]):
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, List[StoreListItem]]]
    """

    return sync_detailed(
        client=client,
        shipping_method=shipping_method,
        lat=lat,
        lon=lon,
        api_version=api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    shipping_method: Union[Unset, None, GetStoresShippingMethod] = GetStoresShippingMethod.DELIVERY,
    lat: Union[Unset, None, str] = UNSET,
    lon: Union[Unset, None, str] = UNSET,
    api_version: Union[Unset, str] = "3.0",
) -> Response[Union[Any, List[StoreListItem]]]:
    """Получить все магазины вокруг данной точки

    Args:
        shipping_method (Union[Unset, None, GetStoresShippingMethod]):  Default:
            GetStoresShippingMethod.DELIVERY.
        lat (Union[Unset, None, str]):
        lon (Union[Unset, None, str]):
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, List[StoreListItem]]]
    """

    kwargs = _get_kwargs(
        client=client,
        shipping_method=shipping_method,
        lat=lat,
        lon=lon,
        api_version=api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    client.set_cookies(dict(response.cookies))
    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    shipping_method: Union[Unset, None, GetStoresShippingMethod] = GetStoresShippingMethod.DELIVERY,
    lat: Union[Unset, None, str] = UNSET,
    lon: Union[Unset, None, str] = UNSET,
    api_version: Union[Unset, str] = "3.0",
) -> Optional[Union[Any, List[StoreListItem]]]:
    """Получить все магазины вокруг данной точки

    Args:
        shipping_method (Union[Unset, None, GetStoresShippingMethod]):  Default:
            GetStoresShippingMethod.DELIVERY.
        lat (Union[Unset, None, str]):
        lon (Union[Unset, None, str]):
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, List[StoreListItem]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            shipping_method=shipping_method,
            lat=lat,
            lon=lon,
            api_version=api_version,
        )
    ).parsed
