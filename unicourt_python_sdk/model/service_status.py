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


class ServiceStatus(
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
            "serviceStatusDownDetails",
            "serviceDetails",
            "serviceUp",
            "object",
        }
        
        class properties:
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 13
                    min_length = 13
            
            
            class serviceDetails(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "acceptingCaseUpdates": "ACCEPTING_CASE_UPDATES",
                        "notAcceptingCaseUpdates": "NOT_ACCEPTING_CASE_UPDATES",
                        "acceptingCaseTrack": "ACCEPTING_CASE_TRACK",
                        "notAcceptingCaseTrack": "NOT_ACCEPTING_CASE_TRACK",
                        "acceptingAutoDocOrders": "ACCEPTING_AUTO_DOC_ORDERS",
                        "acceptingManualDocOrders": "ACCEPTING_MANUAL_DOC_ORDERS",
                        "notAcceptingAutoDocOrdersLimitExceeded": "NOT_ACCEPTING_AUTO_DOC_ORDERS_LIMIT_EXCEEDED",
                        "notAcceptingManualDocOrdersLimitExceeded": "NOT_ACCEPTING_MANUAL_DOC_ORDERS_LIMIT_EXCEEDED",
                        "notAcceptingDocOrders": "NOT_ACCEPTING_DOC_ORDERS",
                    }
                
                @schemas.classproperty
                def ACCEPTING_CASE_UPDATES(cls):
                    return cls("acceptingCaseUpdates")
                
                @schemas.classproperty
                def NOT_ACCEPTING_CASE_UPDATES(cls):
                    return cls("notAcceptingCaseUpdates")
                
                @schemas.classproperty
                def ACCEPTING_CASE_TRACK(cls):
                    return cls("acceptingCaseTrack")
                
                @schemas.classproperty
                def NOT_ACCEPTING_CASE_TRACK(cls):
                    return cls("notAcceptingCaseTrack")
                
                @schemas.classproperty
                def ACCEPTING_AUTO_DOC_ORDERS(cls):
                    return cls("acceptingAutoDocOrders")
                
                @schemas.classproperty
                def ACCEPTING_MANUAL_DOC_ORDERS(cls):
                    return cls("acceptingManualDocOrders")
                
                @schemas.classproperty
                def NOT_ACCEPTING_AUTO_DOC_ORDERS_LIMIT_EXCEEDED(cls):
                    return cls("notAcceptingAutoDocOrdersLimitExceeded")
                
                @schemas.classproperty
                def NOT_ACCEPTING_MANUAL_DOC_ORDERS_LIMIT_EXCEEDED(cls):
                    return cls("notAcceptingManualDocOrdersLimitExceeded")
                
                @schemas.classproperty
                def NOT_ACCEPTING_DOC_ORDERS(cls):
                    return cls("notAcceptingDocOrders")
        
            @staticmethod
            def serviceStatusDownDetails() -> typing.Type['ServiceStatusDownDetails']:
                return ServiceStatusDownDetails
            serviceUp = schemas.BoolSchema
            __annotations__ = {
                "object": object,
                "serviceDetails": serviceDetails,
                "serviceStatusDownDetails": serviceStatusDownDetails,
                "serviceUp": serviceUp,
            }

    
    serviceStatusDownDetails: 'ServiceStatusDownDetails'
    serviceDetails: MetaOapg.properties.serviceDetails
    serviceUp: MetaOapg.properties.serviceUp
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceDetails"]) -> MetaOapg.properties.serviceDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceStatusDownDetails"]) -> 'ServiceStatusDownDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceUp"]) -> MetaOapg.properties.serviceUp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["object", "serviceDetails", "serviceStatusDownDetails", "serviceUp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceDetails"]) -> MetaOapg.properties.serviceDetails: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceStatusDownDetails"]) -> 'ServiceStatusDownDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceUp"]) -> MetaOapg.properties.serviceUp: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["object", "serviceDetails", "serviceStatusDownDetails", "serviceUp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServiceStatus':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.service_status_down_details import ServiceStatusDownDetails
