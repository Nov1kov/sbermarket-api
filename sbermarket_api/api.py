from typing import Any, Dict, List, Union

from urllib.parse import urljoin

import requests
from requests import JSONDecodeError


class ApiError(Exception):
    pass


class API:
    def __init__(self, base_url: str, client_token: str):
        self.__client_token = client_token
        self.base_url = base_url

    def request(self, url, auth=True, query: Dict[str, Any] = None):  # type: ignore
        full_url = urljoin(self.base_url, url)
        headers = {"accept": "application/json, text/plain, */*", "api-version": "3.0"}
        if auth:
            headers["client-token"] = self.__client_token
        resp = requests.get(full_url, headers=headers, params=query)
        try:
            result = resp.json()
            if "error" in result:
                raise ApiError(result["error"])
            return result
        except JSONDecodeError as e:
            raise ApiError("Unexpected not json response. Can't parse.")
        except Exception as e:
            raise e


# ToDo research
# "https://sbermarket.ru/api/auth_providers/sberbank/auth_params"
# "https://sbermarket.ru/api/next/page/browser_head"
# "https://sbermarket.ru/api/phone_confirmations"
# "https://sbermarket.ru/api/stores/1/next_deliveries?cargo=false"
# "https://sbermarket.ru/_next/static/chunks/pages/_app-b824ce51c817753c.js"
