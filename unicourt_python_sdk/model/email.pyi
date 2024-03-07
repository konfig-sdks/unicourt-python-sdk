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


class Email(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Email object data schema.
    """


    class MetaOapg:
        required = {
            "lastFetchDate",
            "emailId",
            "isVisible",
            "firstFetchDate",
            "object",
        }
        
        class properties:
            
            
            class emailId(
                schemas.StrSchema
            ):
                pass
            
            
            class firstFetchDate(
                schemas.DateTimeSchema
            ):
                pass
            isVisible = schemas.BoolSchema
            
            
            class lastFetchDate(
                schemas.DateTimeSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "emailId": emailId,
                "firstFetchDate": firstFetchDate,
                "isVisible": isVisible,
                "lastFetchDate": lastFetchDate,
                "object": object,
            }
    
    lastFetchDate: MetaOapg.properties.lastFetchDate
    emailId: MetaOapg.properties.emailId
    isVisible: MetaOapg.properties.isVisible
    firstFetchDate: MetaOapg.properties.firstFetchDate
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailId"]) -> MetaOapg.properties.emailId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["emailId", "firstFetchDate", "isVisible", "lastFetchDate", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailId"]) -> MetaOapg.properties.emailId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isVisible"]) -> MetaOapg.properties.isVisible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["emailId", "firstFetchDate", "isVisible", "lastFetchDate", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lastFetchDate: typing.Union[MetaOapg.properties.lastFetchDate, str, datetime, ],
        emailId: typing.Union[MetaOapg.properties.emailId, str, ],
        isVisible: typing.Union[MetaOapg.properties.isVisible, bool, ],
        firstFetchDate: typing.Union[MetaOapg.properties.firstFetchDate, str, datetime, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Email':
        return super().__new__(
            cls,
            *args,
            lastFetchDate=lastFetchDate,
            emailId=emailId,
            isVisible=isVisible,
            firstFetchDate=firstFetchDate,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
