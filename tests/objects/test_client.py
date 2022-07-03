"""Tests for hello function."""
import re

import pytest
import responses

from sbermarket_api.client import Client

stores = [
    {
        "id": "68dc8fd6-4c5d-471a-a305-57c3b104dab7",
        "store_id": 83,
        "name": "METRO, Санкт-Петербург, Комендантский просп.",
        "min_order_amount": 1000.0,
        "min_order_amount_pickup": 500.0,
        "min_first_order_amount": 1000.0,
        "min_first_order_amount_pickup": 500.0,
        "delivery_forecast_text": None,
        "on_demand": False,
        "express_delivery": False,
        "shipping_methods": [
            {"title": "Курьером", "type": "by_courier"},
            {"title": "Курьером для компаний", "type": "by_courier_for_companies"},
        ],
    },
    {
        "id": "db8102fa-57fd-4cb3-bdf7-f59077622985",
        "store_id": 313,
        "name": "АШАН, Санкт-Петербург, Торфяная дорога",
        "min_order_amount": 1000.0,
        "min_order_amount_pickup": 500.0,
        "min_first_order_amount": 1000.0,
        "min_first_order_amount_pickup": 500.0,
        "delivery_forecast_text": None,
        "on_demand": False,
        "express_delivery": False,
        "shipping_methods": [
            {"title": "Курьером", "type": "by_courier"},
            {"title": "Курьером для компаний", "type": "by_courier_for_companies"},
        ],
    },
    {
        "id": "2b79aa9f-4887-4b56-9b93-d8359fd181a2",
        "store_id": 1293,
        "name": "ЛЕНТА, Санкт-Петербург, Планерная ул.",
        "min_order_amount": 1000.0,
        "min_order_amount_pickup": 500.0,
        "min_first_order_amount": 1000.0,
        "min_first_order_amount_pickup": 500.0,
        "delivery_forecast_text": None,
        "on_demand": False,
        "express_delivery": False,
        "shipping_methods": [
            {"title": "Курьером", "type": "by_courier"},
            {"title": "Курьером для компаний", "type": "by_courier_for_companies"},
        ],
    },
]


@pytest.fixture()
def resp_get_stores():
    with responses.RequestsMock() as rsps:
        rsps.add(
            method=responses.GET,
            url=re.compile(
                r"https://sbermarket\.ru/api/stores\?lat=\d+\.?\d+?&lon=\d+\.?\d+?&shipping_method=delivery"
            ),
            json=stores,
            content_type="application/json",
            status=200,
        )
        yield rsps


def test_get_stores(resp_get_stores):
    client = Client()
    stores = client.stores(lat=60.003526, lon=30.253471)
    assert stores[0].id == "68dc8fd6-4c5d-471a-a305-57c3b104dab7"
    assert stores[1].name == "АШАН, Санкт-Петербург, Торфяная дорога"
    assert stores[2].store_id == 1293
