from typing import Any, BinaryIO, Dict, List, Optional, TextIO, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreConfig")


@attr.s(auto_attribs=True)
class StoreConfig:
    """
    Attributes:
        lifepay_identifier (Union[Unset, str]):
        import_key_postfix (Union[Unset, str]):
        seconds_for_assembly_item (Union[Unset, int]):
        additional_seconds_for_assembly (Union[Unset, int]):
    """

    lifepay_identifier: Union[Unset, str] = UNSET
    import_key_postfix: Union[Unset, str] = UNSET
    seconds_for_assembly_item: Union[Unset, int] = UNSET
    additional_seconds_for_assembly: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lifepay_identifier = self.lifepay_identifier
        import_key_postfix = self.import_key_postfix
        seconds_for_assembly_item = self.seconds_for_assembly_item
        additional_seconds_for_assembly = self.additional_seconds_for_assembly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lifepay_identifier is not UNSET:
            field_dict["lifepay_identifier"] = lifepay_identifier
        if import_key_postfix is not UNSET:
            field_dict["import_key_postfix"] = import_key_postfix
        if seconds_for_assembly_item is not UNSET:
            field_dict["seconds_for_assembly_item"] = seconds_for_assembly_item
        if additional_seconds_for_assembly is not UNSET:
            field_dict["additional_seconds_for_assembly"] = additional_seconds_for_assembly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lifepay_identifier = d.pop("lifepay_identifier", UNSET)

        import_key_postfix = d.pop("import_key_postfix", UNSET)

        seconds_for_assembly_item = d.pop("seconds_for_assembly_item", UNSET)

        additional_seconds_for_assembly = d.pop("additional_seconds_for_assembly", UNSET)

        store_config = cls(
            lifepay_identifier=lifepay_identifier,
            import_key_postfix=import_key_postfix,
            seconds_for_assembly_item=seconds_for_assembly_item,
            additional_seconds_for_assembly=additional_seconds_for_assembly,
        )

        store_config.additional_properties = d
        return store_config

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
