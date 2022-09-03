from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.store import Store
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: int,
    *,
    client: Client,
    api_version: Union[Unset, str] = "3.0",
) -> Dict[str, Any]:
    url = f"{client.base_url}/stores/{store_id}"

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(api_version, Unset):
        headers["api-version"] = api_version

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Store]]:
    if response.status_code == 200:
        response_200 = Store.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Store]]:
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
    api_version: Union[Unset, str] = "3.0",
) -> Response[Union[Any, Store]]:
    """Find store by ID

     Returns a single store

    Args:
        store_id (int):
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, Store]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        client=client,
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
    api_version: Union[Unset, str] = "3.0",
) -> Optional[Union[Any, Store]]:
    """Find store by ID

     Returns a single store

    Args:
        store_id (int):
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, Store]]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        api_version=api_version,
    ).parsed


async def asyncio_detailed(
    store_id: int,
    *,
    client: Client,
    api_version: Union[Unset, str] = "3.0",
) -> Response[Union[Any, Store]]:
    """Find store by ID

     Returns a single store

    Args:
        store_id (int):
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, Store]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        client=client,
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
    api_version: Union[Unset, str] = "3.0",
) -> Optional[Union[Any, Store]]:
    """Find store by ID

     Returns a single store

    Args:
        store_id (int):
        api_version (Union[Unset, str]):  Default: '3.0'.

    Returns:
        Response[Union[Any, Store]]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            api_version=api_version,
        )
    ).parsed
