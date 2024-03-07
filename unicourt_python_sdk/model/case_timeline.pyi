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


class CaseTimeline(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "firstCaseFiledDate",
            "lastCaseFiledDate",
            "object",
        }
        
        class properties:
            
            
            class firstCaseFiledDate(
                schemas.DateTimeSchema
            ):
                pass
            
            
            class lastCaseFiledDate(
                schemas.DateTimeSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "firstCaseFiledDate": firstCaseFiledDate,
                "lastCaseFiledDate": lastCaseFiledDate,
                "object": object,
            }
    
    firstCaseFiledDate: MetaOapg.properties.firstCaseFiledDate
    lastCaseFiledDate: MetaOapg.properties.lastCaseFiledDate
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstCaseFiledDate"]) -> MetaOapg.properties.firstCaseFiledDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastCaseFiledDate"]) -> MetaOapg.properties.lastCaseFiledDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstCaseFiledDate", "lastCaseFiledDate", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstCaseFiledDate"]) -> MetaOapg.properties.firstCaseFiledDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastCaseFiledDate"]) -> MetaOapg.properties.lastCaseFiledDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstCaseFiledDate", "lastCaseFiledDate", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        firstCaseFiledDate: typing.Union[MetaOapg.properties.firstCaseFiledDate, str, datetime, ],
        lastCaseFiledDate: typing.Union[MetaOapg.properties.lastCaseFiledDate, str, datetime, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseTimeline':
        return super().__new__(
            cls,
            *args,
            firstCaseFiledDate=firstCaseFiledDate,
            lastCaseFiledDate=lastCaseFiledDate,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
