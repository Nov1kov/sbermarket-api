from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.search_products_response import SearchProductsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: int,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    per_page: Union[Unset, None, int] = 24,
    page: Union[Unset, None, int] = 1,
    api_version: Union[Unset, str] = "3.0",
) -> Dict[str, Any]:
    url = f"{client.base_url}/stores/{store_id}/products"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(api_version, Unset):
        headers["api-version"] = api_version

    params: Dict[str, Any] = {}
    params["q"] = q

    params["per_page"] = per_page

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, SearchProductsResponse]]:
    if response.status_code == 200:
        response_200 = SearchProductsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 301:
        response_301 = cast(Any, None)
        return response_301
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, SearchProductsResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    store_id: int,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    per_page: Union[Unset, None, int] = 24,
    page: Union[Unset, None, int] = 1,
    api_version: Union[Unset, str] = "3.0",
) -> Response[Union[Any, SearchProductsResponse]]:
    """Поиск товаров в магазине

    Args:
        store_id (int):
        q (Union[Unset, None, str]):
        per_page (Union[Unset, None, int]):  Default: 24.
        page (Union[Unset, None, int]):  Default: 1.
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, SearchProductsResponse]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        client=client,
        q=q,
        per_page=per_page,
        page=page,
        api_version=api_version,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    client.set_cookies(dict(response.cookies))
    return _build_response(response=response)


def sync(
    store_id: int,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    per_page: Union[Unset, None, int] = 24,
    page: Union[Unset, None, int] = 1,
    api_version: Union[Unset, str] = "3.0",
) -> Optional[Union[Any, SearchProductsResponse]]:
    """Поиск товаров в магазине

    Args:
        store_id (int):
        q (Union[Unset, None, str]):
        per_page (Union[Unset, None, int]):  Default: 24.
        page (Union[Unset, None, int]):  Default: 1.
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, SearchProductsResponse]]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        q=q,
        per_page=per_page,
        page=page,
        api_version=api_version,
    ).parsed


async def asyncio_detailed(
    store_id: int,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    per_page: Union[Unset, None, int] = 24,
    page: Union[Unset, None, int] = 1,
    api_version: Union[Unset, str] = "3.0",
) -> Response[Union[Any, SearchProductsResponse]]:
    """Поиск товаров в магазине

    Args:
        store_id (int):
        q (Union[Unset, None, str]):
        per_page (Union[Unset, None, int]):  Default: 24.
        page (Union[Unset, None, int]):  Default: 1.
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, SearchProductsResponse]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        client=client,
        q=q,
        per_page=per_page,
        page=page,
        api_version=api_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    client.set_cookies(dict(response.cookies))
    return _build_response(response=response)


async def asyncio(
    store_id: int,
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    per_page: Union[Unset, None, int] = 24,
    page: Union[Unset, None, int] = 1,
    api_version: Union[Unset, str] = "3.0",
) -> Optional[Union[Any, SearchProductsResponse]]:
    """Поиск товаров в магазине

    Args:
        store_id (int):
        q (Union[Unset, None, str]):
        per_page (Union[Unset, None, int]):  Default: 24.
        page (Union[Unset, None, int]):  Default: 1.
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, SearchProductsResponse]]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            q=q,
            per_page=per_page,
            page=page,
            api_version=api_version,
        )
    ).parsed
