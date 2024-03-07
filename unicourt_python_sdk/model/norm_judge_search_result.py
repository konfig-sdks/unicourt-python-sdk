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


class NormJudgeSearchResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "lastFetchDate",
            "matchedObjectArray",
            "name",
            "normJudgeId",
            "firstFetchDate",
            "normJudgeDetailsAPI",
            "object",
        }
        
        class properties:
            
            
            class firstFetchDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
                    min_length = 25
            
            
            class lastFetchDate(
                schemas.DateTimeSchema
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
                    max_length = 25
                    min_length = 25
            
            
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
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 1
            
            
            class normJudgeDetailsAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
                    min_length = 1
            
            
            class normJudgeId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 17
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 21
                    min_length = 21
            __annotations__ = {
                "firstFetchDate": firstFetchDate,
                "lastFetchDate": lastFetchDate,
                "matchedObjectArray": matchedObjectArray,
                "name": name,
                "normJudgeDetailsAPI": normJudgeDetailsAPI,
                "normJudgeId": normJudgeId,
                "object": object,
            }
    
    lastFetchDate: MetaOapg.properties.lastFetchDate
    matchedObjectArray: MetaOapg.properties.matchedObjectArray
    name: MetaOapg.properties.name
    normJudgeId: MetaOapg.properties.normJudgeId
    firstFetchDate: MetaOapg.properties.firstFetchDate
    normJudgeDetailsAPI: MetaOapg.properties.normJudgeDetailsAPI
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
    def __getitem__(self, name: typing_extensions.Literal["normJudgeDetailsAPI"]) -> MetaOapg.properties.normJudgeDetailsAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normJudgeId"]) -> MetaOapg.properties.normJudgeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstFetchDate", "lastFetchDate", "matchedObjectArray", "name", "normJudgeDetailsAPI", "normJudgeId", "object", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["normJudgeDetailsAPI"]) -> MetaOapg.properties.normJudgeDetailsAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normJudgeId"]) -> MetaOapg.properties.normJudgeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstFetchDate", "lastFetchDate", "matchedObjectArray", "name", "normJudgeDetailsAPI", "normJudgeId", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lastFetchDate: typing.Union[MetaOapg.properties.lastFetchDate, str, datetime, ],
        matchedObjectArray: typing.Union[MetaOapg.properties.matchedObjectArray, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        normJudgeId: typing.Union[MetaOapg.properties.normJudgeId, str, ],
        firstFetchDate: typing.Union[MetaOapg.properties.firstFetchDate, str, datetime, ],
        normJudgeDetailsAPI: typing.Union[MetaOapg.properties.normJudgeDetailsAPI, str, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NormJudgeSearchResult':
        return super().__new__(
            cls,
            *args,
            lastFetchDate=lastFetchDate,
            matchedObjectArray=matchedObjectArray,
            name=name,
            normJudgeId=normJudgeId,
            firstFetchDate=firstFetchDate,
            normJudgeDetailsAPI=normJudgeDetailsAPI,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.matched_object import MatchedObject
