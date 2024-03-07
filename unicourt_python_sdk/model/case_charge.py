# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unicourt_python_sdk import schemas  # noqa: F401


class CaseCharge(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "chargeDegree",
            "charge",
            "chargeSeverity",
            "chargeAdditionalDataArray",
            "object",
        }
        
        class properties:
        
            @staticmethod
            def charge() -> typing.Type['Charge']:
                return Charge
            
            
            class chargeAdditionalDataArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ChargeAdditionalData']:
                        return ChargeAdditionalData
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ChargeAdditionalData'], typing.List['ChargeAdditionalData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'chargeAdditionalDataArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChargeAdditionalData':
                    return super().__getitem__(i)
        
            @staticmethod
            def chargeDegree() -> typing.Type['ChargeDegree']:
                return ChargeDegree
        
            @staticmethod
            def chargeSeverity() -> typing.Type['ChargeSeverity']:
                return ChargeSeverity
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 10
                    min_length = 10
            __annotations__ = {
                "charge": charge,
                "chargeAdditionalDataArray": chargeAdditionalDataArray,
                "chargeDegree": chargeDegree,
                "chargeSeverity": chargeSeverity,
                "object": object,
            }

    
    chargeDegree: 'ChargeDegree'
    charge: 'Charge'
    chargeSeverity: 'ChargeSeverity'
    chargeAdditionalDataArray: MetaOapg.properties.chargeAdditionalDataArray
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["charge"]) -> 'Charge': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeAdditionalDataArray"]) -> MetaOapg.properties.chargeAdditionalDataArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeDegree"]) -> 'ChargeDegree': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeSeverity"]) -> 'ChargeSeverity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["charge", "chargeAdditionalDataArray", "chargeDegree", "chargeSeverity", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["charge"]) -> 'Charge': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeAdditionalDataArray"]) -> MetaOapg.properties.chargeAdditionalDataArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeDegree"]) -> 'ChargeDegree': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeSeverity"]) -> 'ChargeSeverity': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["charge", "chargeAdditionalDataArray", "chargeDegree", "chargeSeverity", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseCharge':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.charge import Charge
from unicourt_python_sdk.model.charge_additional_data import ChargeAdditionalData
from unicourt_python_sdk.model.charge_degree import ChargeDegree
from unicourt_python_sdk.model.charge_severity import ChargeSeverity
