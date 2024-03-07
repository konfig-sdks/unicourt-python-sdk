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


class BillingCycleUsageResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "totalCasesTracked",
            "billingCycle",
            "apiCallsCredited",
            "days",
            "apiUsage",
            "apiCallsBillable",
            "apiCallsMade",
            "object",
        }
        
        class properties:
        
            @staticmethod
            def apiCallsBillable() -> typing.Type['BillingCycleUsageResponseApiCallsBillable']:
                return BillingCycleUsageResponseApiCallsBillable
        
            @staticmethod
            def apiCallsCredited() -> typing.Type['BillingCycleUsageResponseApiCallsCredited']:
                return BillingCycleUsageResponseApiCallsCredited
        
            @staticmethod
            def apiCallsMade() -> typing.Type['BillingCycleUsageResponseApiCallsMade']:
                return BillingCycleUsageResponseApiCallsMade
            apiUsage = schemas.DictSchema
        
            @staticmethod
            def billingCycle() -> typing.Type['BillingCycleUsageResponseBillingCycle']:
                return BillingCycleUsageResponseBillingCycle
            days = schemas.DictSchema
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 25
                    min_length = 25
            totalCasesTracked = schemas.IntSchema
            __annotations__ = {
                "apiCallsBillable": apiCallsBillable,
                "apiCallsCredited": apiCallsCredited,
                "apiCallsMade": apiCallsMade,
                "apiUsage": apiUsage,
                "billingCycle": billingCycle,
                "days": days,
                "object": object,
                "totalCasesTracked": totalCasesTracked,
            }
    
    totalCasesTracked: MetaOapg.properties.totalCasesTracked
    billingCycle: 'BillingCycleUsageResponseBillingCycle'
    apiCallsCredited: 'BillingCycleUsageResponseApiCallsCredited'
    days: MetaOapg.properties.days
    apiUsage: MetaOapg.properties.apiUsage
    apiCallsBillable: 'BillingCycleUsageResponseApiCallsBillable'
    apiCallsMade: 'BillingCycleUsageResponseApiCallsMade'
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiCallsBillable"]) -> 'BillingCycleUsageResponseApiCallsBillable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiCallsCredited"]) -> 'BillingCycleUsageResponseApiCallsCredited': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiCallsMade"]) -> 'BillingCycleUsageResponseApiCallsMade': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiUsage"]) -> MetaOapg.properties.apiUsage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingCycle"]) -> 'BillingCycleUsageResponseBillingCycle': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["days"]) -> MetaOapg.properties.days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCasesTracked"]) -> MetaOapg.properties.totalCasesTracked: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["apiCallsBillable", "apiCallsCredited", "apiCallsMade", "apiUsage", "billingCycle", "days", "object", "totalCasesTracked", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiCallsBillable"]) -> 'BillingCycleUsageResponseApiCallsBillable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiCallsCredited"]) -> 'BillingCycleUsageResponseApiCallsCredited': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiCallsMade"]) -> 'BillingCycleUsageResponseApiCallsMade': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiUsage"]) -> MetaOapg.properties.apiUsage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingCycle"]) -> 'BillingCycleUsageResponseBillingCycle': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["days"]) -> MetaOapg.properties.days: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCasesTracked"]) -> MetaOapg.properties.totalCasesTracked: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["apiCallsBillable", "apiCallsCredited", "apiCallsMade", "apiUsage", "billingCycle", "days", "object", "totalCasesTracked", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        totalCasesTracked: typing.Union[MetaOapg.properties.totalCasesTracked, decimal.Decimal, int, ],
        billingCycle: 'BillingCycleUsageResponseBillingCycle',
        apiCallsCredited: 'BillingCycleUsageResponseApiCallsCredited',
        days: typing.Union[MetaOapg.properties.days, dict, frozendict.frozendict, ],
        apiUsage: typing.Union[MetaOapg.properties.apiUsage, dict, frozendict.frozendict, ],
        apiCallsBillable: 'BillingCycleUsageResponseApiCallsBillable',
        apiCallsMade: 'BillingCycleUsageResponseApiCallsMade',
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BillingCycleUsageResponse':
        return super().__new__(
            cls,
            *args,
            totalCasesTracked=totalCasesTracked,
            billingCycle=billingCycle,
            apiCallsCredited=apiCallsCredited,
            days=days,
            apiUsage=apiUsage,
            apiCallsBillable=apiCallsBillable,
            apiCallsMade=apiCallsMade,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.billing_cycle_usage_response_api_calls_billable import BillingCycleUsageResponseApiCallsBillable
from unicourt_python_sdk.model.billing_cycle_usage_response_api_calls_credited import BillingCycleUsageResponseApiCallsCredited
from unicourt_python_sdk.model.billing_cycle_usage_response_api_calls_made import BillingCycleUsageResponseApiCallsMade
from unicourt_python_sdk.model.billing_cycle_usage_response_billing_cycle import BillingCycleUsageResponseBillingCycle
