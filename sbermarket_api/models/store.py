from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.store_city import StoreCity
from ..models.store_config import StoreConfig
from ..models.store_licenses_item import StoreLicensesItem
from ..models.store_location import StoreLocation
from ..models.store_operational_zone import StoreOperationalZone
from ..models.store_payment_methods_stores_item import StorePaymentMethodsStoresItem
from ..models.store_retailer import StoreRetailer
from ..models.store_store_schedule import StoreStoreSchedule
from ..models.store_store_shipping_methods_item import StoreStoreShippingMethodsItem
from ..models.store_store_zones_item import StoreStoreZonesItem
from ..models.store_tenants_item import StoreTenantsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Store")


@attr.s(auto_attribs=True)
class Store:
    """
    Attributes:
        id (Union[Unset, int]):
        uuid (Union[Unset, str]):
        name (Union[Unset, str]):
        city_id (Union[Unset, int]):
        on_demand (Union[Unset, bool]):
        on_demand_raw (Union[Unset, bool]):
        time_zone (Union[Unset, str]):
        available_on (Union[Unset, str]):
        has_conveyor (Union[Unset, bool]):
        auto_routing (Union[Unset, bool]):
        express_delivery (Union[Unset, bool]):
        pickup_instruction (Union[Unset, str]):
        import_key_postfix (Union[Unset, str]):
        active (Union[Unset, bool]):
        box_scanning (Union[Unset, bool]):
        seconds_for_assembly_item (Union[Unset, int]):
        additional_seconds_for_assembly (Union[Unset, int]):
        retailer_store_id (Union[Unset, str]):
        external_assembly (Union[Unset, bool]):
        training (Union[Unset, bool]):
        delivery_forecast_text (Union[Unset, str]):
        pharmacy_legal_info (Union[Unset, str]):
        phone (Union[Unset, str]):
        orders_api_integration_type (Union[Unset, str]):
        opening_time (Union[Unset, str]):
        closing_time (Union[Unset, str]):
        parallel_assembly (Union[Unset, bool]):
        assembly_dispatch (Union[Unset, bool]):
        retailer (Union[Unset, StoreRetailer]):
        location (Union[Unset, StoreLocation]):
        store_zones (Union[Unset, List[StoreStoreZonesItem]]):
        config (Union[Unset, StoreConfig]):
        store_schedule (Union[Unset, StoreStoreSchedule]):
        operational_zone (Union[Unset, StoreOperationalZone]):
        city (Union[Unset, StoreCity]):
        tenants (Union[Unset, List[StoreTenantsItem]]):
        store_shipping_methods (Union[Unset, List[StoreStoreShippingMethodsItem]]):
        payment_methods_stores (Union[Unset, List[StorePaymentMethodsStoresItem]]):
        licenses (Union[Unset, List[StoreLicensesItem]]):
    """

    id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    city_id: Union[Unset, int] = UNSET
    on_demand: Union[Unset, bool] = UNSET
    on_demand_raw: Union[Unset, bool] = UNSET
    time_zone: Union[Unset, str] = UNSET
    available_on: Union[Unset, str] = UNSET
    has_conveyor: Union[Unset, bool] = UNSET
    auto_routing: Union[Unset, bool] = UNSET
    express_delivery: Union[Unset, bool] = UNSET
    pickup_instruction: Union[Unset, str] = UNSET
    import_key_postfix: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    box_scanning: Union[Unset, bool] = UNSET
    seconds_for_assembly_item: Union[Unset, int] = UNSET
    additional_seconds_for_assembly: Union[Unset, int] = UNSET
    retailer_store_id: Union[Unset, str] = UNSET
    external_assembly: Union[Unset, bool] = UNSET
    training: Union[Unset, bool] = UNSET
    delivery_forecast_text: Union[Unset, str] = UNSET
    pharmacy_legal_info: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    orders_api_integration_type: Union[Unset, str] = UNSET
    opening_time: Union[Unset, str] = UNSET
    closing_time: Union[Unset, str] = UNSET
    parallel_assembly: Union[Unset, bool] = UNSET
    assembly_dispatch: Union[Unset, bool] = UNSET
    retailer: Union[Unset, StoreRetailer] = UNSET
    location: Union[Unset, StoreLocation] = UNSET
    store_zones: Union[Unset, List[StoreStoreZonesItem]] = UNSET
    config: Union[Unset, StoreConfig] = UNSET
    store_schedule: Union[Unset, StoreStoreSchedule] = UNSET
    operational_zone: Union[Unset, StoreOperationalZone] = UNSET
    city: Union[Unset, StoreCity] = UNSET
    tenants: Union[Unset, List[StoreTenantsItem]] = UNSET
    store_shipping_methods: Union[Unset, List[StoreStoreShippingMethodsItem]] = UNSET
    payment_methods_stores: Union[Unset, List[StorePaymentMethodsStoresItem]] = UNSET
    licenses: Union[Unset, List[StoreLicensesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uuid = self.uuid
        name = self.name
        city_id = self.city_id
        on_demand = self.on_demand
        on_demand_raw = self.on_demand_raw
        time_zone = self.time_zone
        available_on = self.available_on
        has_conveyor = self.has_conveyor
        auto_routing = self.auto_routing
        express_delivery = self.express_delivery
        pickup_instruction = self.pickup_instruction
        import_key_postfix = self.import_key_postfix
        active = self.active
        box_scanning = self.box_scanning
        seconds_for_assembly_item = self.seconds_for_assembly_item
        additional_seconds_for_assembly = self.additional_seconds_for_assembly
        retailer_store_id = self.retailer_store_id
        external_assembly = self.external_assembly
        training = self.training
        delivery_forecast_text = self.delivery_forecast_text
        pharmacy_legal_info = self.pharmacy_legal_info
        phone = self.phone
        orders_api_integration_type = self.orders_api_integration_type
        opening_time = self.opening_time
        closing_time = self.closing_time
        parallel_assembly = self.parallel_assembly
        assembly_dispatch = self.assembly_dispatch
        retailer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retailer, Unset):
            retailer = self.retailer.to_dict()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        store_zones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.store_zones, Unset):
            store_zones = []
            for store_zones_item_data in self.store_zones:
                store_zones_item = store_zones_item_data.to_dict()

                store_zones.append(store_zones_item)

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        store_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.store_schedule, Unset):
            store_schedule = self.store_schedule.to_dict()

        operational_zone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.operational_zone, Unset):
            operational_zone = self.operational_zone.to_dict()

        city: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.city, Unset):
            city = self.city.to_dict()

        tenants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tenants, Unset):
            tenants = []
            for tenants_item_data in self.tenants:
                tenants_item = tenants_item_data.to_dict()

                tenants.append(tenants_item)

        store_shipping_methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.store_shipping_methods, Unset):
            store_shipping_methods = []
            for store_shipping_methods_item_data in self.store_shipping_methods:
                store_shipping_methods_item = store_shipping_methods_item_data.to_dict()

                store_shipping_methods.append(store_shipping_methods_item)

        payment_methods_stores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payment_methods_stores, Unset):
            payment_methods_stores = []
            for payment_methods_stores_item_data in self.payment_methods_stores:
                payment_methods_stores_item = payment_methods_stores_item_data.to_dict()

                payment_methods_stores.append(payment_methods_stores_item)

        licenses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = []
            for licenses_item_data in self.licenses:
                licenses_item = licenses_item_data.to_dict()

                licenses.append(licenses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if city_id is not UNSET:
            field_dict["city_id"] = city_id
        if on_demand is not UNSET:
            field_dict["on_demand"] = on_demand
        if on_demand_raw is not UNSET:
            field_dict["on_demand_raw"] = on_demand_raw
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if available_on is not UNSET:
            field_dict["available_on"] = available_on
        if has_conveyor is not UNSET:
            field_dict["has_conveyor"] = has_conveyor
        if auto_routing is not UNSET:
            field_dict["auto_routing"] = auto_routing
        if express_delivery is not UNSET:
            field_dict["express_delivery"] = express_delivery
        if pickup_instruction is not UNSET:
            field_dict["pickup_instruction"] = pickup_instruction
        if import_key_postfix is not UNSET:
            field_dict["import_key_postfix"] = import_key_postfix
        if active is not UNSET:
            field_dict["active"] = active
        if box_scanning is not UNSET:
            field_dict["box_scanning"] = box_scanning
        if seconds_for_assembly_item is not UNSET:
            field_dict["seconds_for_assembly_item"] = seconds_for_assembly_item
        if additional_seconds_for_assembly is not UNSET:
            field_dict["additional_seconds_for_assembly"] = additional_seconds_for_assembly
        if retailer_store_id is not UNSET:
            field_dict["retailer_store_id"] = retailer_store_id
        if external_assembly is not UNSET:
            field_dict["external_assembly"] = external_assembly
        if training is not UNSET:
            field_dict["training"] = training
        if delivery_forecast_text is not UNSET:
            field_dict["delivery_forecast_text"] = delivery_forecast_text
        if pharmacy_legal_info is not UNSET:
            field_dict["pharmacy_legal_info"] = pharmacy_legal_info
        if phone is not UNSET:
            field_dict["phone"] = phone
        if orders_api_integration_type is not UNSET:
            field_dict["orders_api_integration_type"] = orders_api_integration_type
        if opening_time is not UNSET:
            field_dict["opening_time"] = opening_time
        if closing_time is not UNSET:
            field_dict["closing_time"] = closing_time
        if parallel_assembly is not UNSET:
            field_dict["parallel_assembly"] = parallel_assembly
        if assembly_dispatch is not UNSET:
            field_dict["assembly_dispatch"] = assembly_dispatch
        if retailer is not UNSET:
            field_dict["retailer"] = retailer
        if location is not UNSET:
            field_dict["location"] = location
        if store_zones is not UNSET:
            field_dict["store_zones"] = store_zones
        if config is not UNSET:
            field_dict["config"] = config
        if store_schedule is not UNSET:
            field_dict["store_schedule"] = store_schedule
        if operational_zone is not UNSET:
            field_dict["operational_zone"] = operational_zone
        if city is not UNSET:
            field_dict["city"] = city
        if tenants is not UNSET:
            field_dict["tenants"] = tenants
        if store_shipping_methods is not UNSET:
            field_dict["store_shipping_methods"] = store_shipping_methods
        if payment_methods_stores is not UNSET:
            field_dict["payment_methods_stores"] = payment_methods_stores
        if licenses is not UNSET:
            field_dict["licenses"] = licenses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        city_id = d.pop("city_id", UNSET)

        on_demand = d.pop("on_demand", UNSET)

        on_demand_raw = d.pop("on_demand_raw", UNSET)

        time_zone = d.pop("time_zone", UNSET)

        available_on = d.pop("available_on", UNSET)

        has_conveyor = d.pop("has_conveyor", UNSET)

        auto_routing = d.pop("auto_routing", UNSET)

        express_delivery = d.pop("express_delivery", UNSET)

        pickup_instruction = d.pop("pickup_instruction", UNSET)

        import_key_postfix = d.pop("import_key_postfix", UNSET)

        active = d.pop("active", UNSET)

        box_scanning = d.pop("box_scanning", UNSET)

        seconds_for_assembly_item = d.pop("seconds_for_assembly_item", UNSET)

        additional_seconds_for_assembly = d.pop("additional_seconds_for_assembly", UNSET)

        retailer_store_id = d.pop("retailer_store_id", UNSET)

        external_assembly = d.pop("external_assembly", UNSET)

        training = d.pop("training", UNSET)

        delivery_forecast_text = d.pop("delivery_forecast_text", UNSET)

        pharmacy_legal_info = d.pop("pharmacy_legal_info", UNSET)

        phone = d.pop("phone", UNSET)

        orders_api_integration_type = d.pop("orders_api_integration_type", UNSET)

        opening_time = d.pop("opening_time", UNSET)

        closing_time = d.pop("closing_time", UNSET)

        parallel_assembly = d.pop("parallel_assembly", UNSET)

        assembly_dispatch = d.pop("assembly_dispatch", UNSET)

        _retailer = d.pop("retailer", UNSET)
        retailer: Union[Unset, StoreRetailer]
        if isinstance(_retailer, Unset):
            retailer = UNSET
        else:
            retailer = StoreRetailer.from_dict(_retailer)

        _location = d.pop("location", UNSET)
        location: Union[Unset, StoreLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = StoreLocation.from_dict(_location)

        store_zones = []
        _store_zones = d.pop("store_zones", UNSET)
        for store_zones_item_data in _store_zones or []:
            store_zones_item = StoreStoreZonesItem.from_dict(store_zones_item_data)

            store_zones.append(store_zones_item)

        _config = d.pop("config", UNSET)
        config: Union[Unset, StoreConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = StoreConfig.from_dict(_config)

        _store_schedule = d.pop("store_schedule", UNSET)
        store_schedule: Union[Unset, StoreStoreSchedule]
        if isinstance(_store_schedule, Unset):
            store_schedule = UNSET
        else:
            store_schedule = StoreStoreSchedule.from_dict(_store_schedule)

        _operational_zone = d.pop("operational_zone", UNSET)
        operational_zone: Union[Unset, StoreOperationalZone]
        if isinstance(_operational_zone, Unset):
            operational_zone = UNSET
        else:
            operational_zone = StoreOperationalZone.from_dict(_operational_zone)

        _city = d.pop("city", UNSET)
        city: Union[Unset, StoreCity]
        if isinstance(_city, Unset):
            city = UNSET
        else:
            city = StoreCity.from_dict(_city)

        tenants = []
        _tenants = d.pop("tenants", UNSET)
        for tenants_item_data in _tenants or []:
            tenants_item = StoreTenantsItem.from_dict(tenants_item_data)

            tenants.append(tenants_item)

        store_shipping_methods = []
        _store_shipping_methods = d.pop("store_shipping_methods", UNSET)
        for store_shipping_methods_item_data in _store_shipping_methods or []:
            store_shipping_methods_item = StoreStoreShippingMethodsItem.from_dict(store_shipping_methods_item_data)

            store_shipping_methods.append(store_shipping_methods_item)

        payment_methods_stores = []
        _payment_methods_stores = d.pop("payment_methods_stores", UNSET)
        for payment_methods_stores_item_data in _payment_methods_stores or []:
            payment_methods_stores_item = StorePaymentMethodsStoresItem.from_dict(payment_methods_stores_item_data)

            payment_methods_stores.append(payment_methods_stores_item)

        licenses = []
        _licenses = d.pop("licenses", UNSET)
        for licenses_item_data in _licenses or []:
            licenses_item = StoreLicensesItem.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        store = cls(
            id=id,
            uuid=uuid,
            name=name,
            city_id=city_id,
            on_demand=on_demand,
            on_demand_raw=on_demand_raw,
            time_zone=time_zone,
            available_on=available_on,
            has_conveyor=has_conveyor,
            auto_routing=auto_routing,
            express_delivery=express_delivery,
            pickup_instruction=pickup_instruction,
            import_key_postfix=import_key_postfix,
            active=active,
            box_scanning=box_scanning,
            seconds_for_assembly_item=seconds_for_assembly_item,
            additional_seconds_for_assembly=additional_seconds_for_assembly,
            retailer_store_id=retailer_store_id,
            external_assembly=external_assembly,
            training=training,
            delivery_forecast_text=delivery_forecast_text,
            pharmacy_legal_info=pharmacy_legal_info,
            phone=phone,
            orders_api_integration_type=orders_api_integration_type,
            opening_time=opening_time,
            closing_time=closing_time,
            parallel_assembly=parallel_assembly,
            assembly_dispatch=assembly_dispatch,
            retailer=retailer,
            location=location,
            store_zones=store_zones,
            config=config,
            store_schedule=store_schedule,
            operational_zone=operational_zone,
            city=city,
            tenants=tenants,
            store_shipping_methods=store_shipping_methods,
            payment_methods_stores=payment_methods_stores,
            licenses=licenses,
        )

        store.additional_properties = d
        return store

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
