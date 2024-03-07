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


class Phone(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Phone object data schema.
    """


    class MetaOapg:
        required = {
            "lastFetchDate",
            "phoneType",
            "phoneNumber",
            "isVisible",
            "firstFetchDate",
            "object",
        }
        
        class properties:
            
            
            class firstFetchDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 35
                    min_length = 25
            isVisible = schemas.BoolSchema
            
            
            class lastFetchDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 35
                    min_length = 25
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 5
                    min_length = 5
            
            
            class phoneNumber(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 30
                    min_length = 1
            
            
            class phoneType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 250
                    min_length = 1
                    enum_value_to_name = {
                        "DEFAULT": "DEFAULT",
                        "OFFICE": "OFFICE",
                        "FAX": "FAX",
                        "PHONE": "PHONE",
                    }
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("DEFAULT")
                
                @schemas.classproperty
                def OFFICE(cls):
                    return cls("OFFICE")
                
                @schemas.classproperty
                def FAX(cls):
                    return cls("FAX")
                
                @schemas.classproperty
                def PHONE(cls):
                    return cls("PHONE")
            __annotations__ = {
                "firstFetchDate": firstFetchDate,
                "isVisible": isVisible,
                "lastFetchDate": lastFetchDate,
                "object": object,
                "phoneNumber": phoneNumber,
                "phoneType": phoneType,
            }
    
    lastFetchDate: MetaOapg.properties.lastFetchDate
    phoneType: MetaOapg.properties.phoneType
    phoneNumber: MetaOapg.properties.phoneNumber
    isVisible: MetaOapg.properties.isVisible
    firstFetchDate: MetaOapg.properties.firstFetchDate
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneType"]) -> MetaOapg.properties.phoneType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstFetchDate", "isVisible", "lastFetchDate", "object", "phoneNumber", "phoneType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneType"]) -> MetaOapg.properties.phoneType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstFetchDate", "isVisible", "lastFetchDate", "object", "phoneNumber", "phoneType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lastFetchDate: typing.Union[MetaOapg.properties.lastFetchDate, str, datetime, ],
        phoneType: typing.Union[MetaOapg.properties.phoneType, str, ],
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, ],
        isVisible: typing.Union[MetaOapg.properties.isVisible, bool, ],
        firstFetchDate: typing.Union[MetaOapg.properties.firstFetchDate, str, datetime, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Phone':
        return super().__new__(
            cls,
            *args,
            lastFetchDate=lastFetchDate,
            phoneType=phoneType,
            phoneNumber=phoneNumber,
            isVisible=isVisible,
            firstFetchDate=firstFetchDate,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
