from typing import Dict

import json
import logging
from urllib.parse import urljoin

import requests


class API:
    def __init__(self, base_url: str, client_token: str):
        self.__client_token = client_token
        self.base_url = base_url

    def authorize(self):
        """ToDo авторизация."""
        pass

    def request(self, url, auth=True, query: Dict = None):
        full_url = urljoin(self.base_url, url)
        headers = {"accept": "application/json, text/plain, */*", "api-version": "3.0"}
        if auth:
            headers["client-token"] = self.__client_token
        resp = requests.get(full_url, headers=headers, params=query)
        try:
            result = resp.json()
            return result
        except Exception as e:
            logging.exception(e)


def try_get(url):
    resp = requests.get(
        url,
        headers={
            "accept": "application/json, text/plain, */*",
            "client-token": "7ba97b6f4049436dab90c789f946ee2f",
            "api-version": "3.0",
        },
    )
    try:
        print(json.dumps(resp.json(), indent=2))
    except:
        print(resp)


def test():
    # GET
    # В ответ пустота (на анонимной сесиии) aggregating_categories: []
    try_get("https://sbermarket.ru/api/stores/83/aggregating_categories")
    # POST -
    # response
    # {"authorize_url":"https://online.sberbank.ru/CSAFront/oidc/sberbank_id/authorize.do",
    # "state":"3dd14bd16f408fb1d326412e7ba41bf813da3f52b5dd2da4",
    # "scope":"openid+name+mobile+email+birthdate+gender+address_of_actual_residence+delivery_address",
    # "client_type":"PRIVATE",
    # "response_type":"code",
    # "client_id":"09a6f842-ed4d-4b42-a925-3bc75e77335e",
    # "nonce":"3345f4d1a1fa345fc44afce6e45eb581a440b0f7e7daf266ba3ae30d042306c5"}
    try_get("https://sbermarket.ru/api/auth_providers/sberbank/auth_params")
    # GET - непонятно пока зачем
    try_get("https://sbermarket.ru/api/multiretailer_order")
    # Получить свои текущие адреса.
    # запрос без токена, но в куках есть remember_user_token -ни на что не похожий
    # в ответ на
    try_get("https://sbermarket.ru/api/addresses")
    # Отправляется без токена а в ответа получаем
    # {"csrf_param":"authenticity_token","csrf_token":"Jbdkmim0THL6WdLkI5+12mCFI1mMrWDMQIu2OzLEJwOG7Qh6PJSH3HYTA3om9n1yk1YQh4FC/BOehA6K2tZMcg=="}
    # В ответ также получаем cookie: _Instamart_session
    try_get("https://sbermarket.ru/api/next/page/browser_head")
    # POST phone: "tfRoupxZfXaStCfaprZh75Le1bbzxGMa3Wv9Zxt2PFo=" - динамический каждый раз понять из js не получилось как воссоздать это
    #
    try_get("https://sbermarket.ru/api/phone_confirmations")

    try_get("https://sbermarket.ru/api/stores/1/next_deliveries?cargo=false")
    # PUT method, положить адрес
    # {
    #     "validity": 0,
    #     "lat": 59.962246,
    #     "lon": 30.319758,
    #     "street": "Большая Монетная улица",
    #     "building": "16",
    #     "full_address": "Большая Монетная улица, 16",
    #     "city": "Санкт-Петербург",
    #     "city_in": ""
    # }
    try_get("https://sbermarket.ru/api/shopping_context")
    # Последние магазины на основе адреса?
    # response:
    # {"pickup":[],"by_courier":[]}
    try_get("https://sbermarket.ru/api/recent_stores?lat=59.962246&lon=30.319758")
    # Это возвращает client-token вида: {"api-version":"3.0","client-token":"TOKEN","is-storefront-ssr":l.sk}
    try_get("https://sbermarket.ru/_next/static/chunks/pages/_app-b824ce51c817753c.js")
