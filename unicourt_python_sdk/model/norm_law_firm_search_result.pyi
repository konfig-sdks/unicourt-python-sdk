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


class NormLawFirmSearchResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "normLawFirmDetailsAPI",
            "lastFetchDate",
            "normLawFirmId",
            "matchedObjectArray",
            "name",
            "firstFetchDate",
            "object",
        }
        
        class properties:
            
            
            class firstFetchDate(
                schemas.DateTimeSchema
            ):
                pass
            
            
            class lastFetchDate(
                schemas.DateTimeSchema
            ):
                pass
            
            
            class matchedObjectArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MatchedObject']:
                        return MatchedObject
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MatchedObject'], typing.List['MatchedObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matchedObjectArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MatchedObject':
                    return super().__getitem__(i)
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class normLawFirmDetailsAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class normLawFirmId(
                schemas.StrSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "firstFetchDate": firstFetchDate,
                "lastFetchDate": lastFetchDate,
                "matchedObjectArray": matchedObjectArray,
                "name": name,
                "normLawFirmDetailsAPI": normLawFirmDetailsAPI,
                "normLawFirmId": normLawFirmId,
                "object": object,
            }
    
    normLawFirmDetailsAPI: MetaOapg.properties.normLawFirmDetailsAPI
    lastFetchDate: MetaOapg.properties.lastFetchDate
    normLawFirmId: MetaOapg.properties.normLawFirmId
    matchedObjectArray: MetaOapg.properties.matchedObjectArray
    name: MetaOapg.properties.name
    firstFetchDate: MetaOapg.properties.firstFetchDate
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchedObjectArray"]) -> MetaOapg.properties.matchedObjectArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normLawFirmDetailsAPI"]) -> MetaOapg.properties.normLawFirmDetailsAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normLawFirmId"]) -> MetaOapg.properties.normLawFirmId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstFetchDate", "lastFetchDate", "matchedObjectArray", "name", "normLawFirmDetailsAPI", "normLawFirmId", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstFetchDate"]) -> MetaOapg.properties.firstFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastFetchDate"]) -> MetaOapg.properties.lastFetchDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchedObjectArray"]) -> MetaOapg.properties.matchedObjectArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normLawFirmDetailsAPI"]) -> MetaOapg.properties.normLawFirmDetailsAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normLawFirmId"]) -> MetaOapg.properties.normLawFirmId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstFetchDate", "lastFetchDate", "matchedObjectArray", "name", "normLawFirmDetailsAPI", "normLawFirmId", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        normLawFirmDetailsAPI: typing.Union[MetaOapg.properties.normLawFirmDetailsAPI, str, ],
        lastFetchDate: typing.Union[MetaOapg.properties.lastFetchDate, str, datetime, ],
        normLawFirmId: typing.Union[MetaOapg.properties.normLawFirmId, str, ],
        matchedObjectArray: typing.Union[MetaOapg.properties.matchedObjectArray, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        firstFetchDate: typing.Union[MetaOapg.properties.firstFetchDate, str, datetime, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NormLawFirmSearchResult':
        return super().__new__(
            cls,
            *args,
            normLawFirmDetailsAPI=normLawFirmDetailsAPI,
            lastFetchDate=lastFetchDate,
            normLawFirmId=normLawFirmId,
            matchedObjectArray=matchedObjectArray,
            name=name,
            firstFetchDate=firstFetchDate,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.matched_object import MatchedObject
