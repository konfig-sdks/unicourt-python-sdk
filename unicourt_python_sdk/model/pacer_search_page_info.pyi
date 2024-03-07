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


class PACERSearchPageInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "number",
            "last",
            "numberOfElements",
            "size",
            "totalPages",
            "first",
            "object",
            "totalElements",
        }
        
        class properties:
            first = schemas.BoolSchema
            last = schemas.BoolSchema
            number = schemas.IntSchema
            numberOfElements = schemas.IntSchema
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            size = schemas.IntSchema
            totalElements = schemas.IntSchema
            totalPages = schemas.IntSchema
            __annotations__ = {
                "first": first,
                "last": last,
                "number": number,
                "numberOfElements": numberOfElements,
                "object": object,
                "size": size,
                "totalElements": totalElements,
                "totalPages": totalPages,
            }
    
    number: MetaOapg.properties.number
    last: MetaOapg.properties.last
    numberOfElements: MetaOapg.properties.numberOfElements
    size: MetaOapg.properties.size
    totalPages: MetaOapg.properties.totalPages
    first: MetaOapg.properties.first
    object: MetaOapg.properties.object
    totalElements: MetaOapg.properties.totalElements
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfElements"]) -> MetaOapg.properties.numberOfElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalElements"]) -> MetaOapg.properties.totalElements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first", "last", "number", "numberOfElements", "object", "size", "totalElements", "totalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfElements"]) -> MetaOapg.properties.numberOfElements: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalElements"]) -> MetaOapg.properties.totalElements: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first", "last", "number", "numberOfElements", "object", "size", "totalElements", "totalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, ],
        last: typing.Union[MetaOapg.properties.last, bool, ],
        numberOfElements: typing.Union[MetaOapg.properties.numberOfElements, decimal.Decimal, int, ],
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, ],
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, ],
        first: typing.Union[MetaOapg.properties.first, bool, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        totalElements: typing.Union[MetaOapg.properties.totalElements, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PACERSearchPageInfo':
        return super().__new__(
            cls,
            *args,
            number=number,
            last=last,
            numberOfElements=numberOfElements,
            size=size,
            totalPages=totalPages,
            first=first,
            object=object,
            totalElements=totalElements,
            _configuration=_configuration,
            **kwargs,
        )
