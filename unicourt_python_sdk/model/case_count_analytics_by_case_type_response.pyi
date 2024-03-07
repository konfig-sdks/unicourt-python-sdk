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


class CaseCountAnalyticsByCaseTypeResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Case Counts by Case Types Response.
    """


    class MetaOapg:
        required = {
            "nextPageAPI",
            "previousPageAPI",
            "totalCaseTypeCount",
            "totalPages",
            "totalCaseCount",
            "results",
            "object",
        }
        
        class properties:
            
            
            class nextPageAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nextPageAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            
            
            class previousPageAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'previousPageAPI':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CaseCountAnalyticsByCaseType']:
                        return CaseCountAnalyticsByCaseType
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CaseCountAnalyticsByCaseType'], typing.List['CaseCountAnalyticsByCaseType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'results':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CaseCountAnalyticsByCaseType':
                    return super().__getitem__(i)
            totalCaseCount = schemas.IntSchema
            totalCaseTypeCount = schemas.IntSchema
            totalPages = schemas.IntSchema
            __annotations__ = {
                "nextPageAPI": nextPageAPI,
                "object": object,
                "previousPageAPI": previousPageAPI,
                "results": results,
                "totalCaseCount": totalCaseCount,
                "totalCaseTypeCount": totalCaseTypeCount,
                "totalPages": totalPages,
            }
    
    nextPageAPI: MetaOapg.properties.nextPageAPI
    previousPageAPI: MetaOapg.properties.previousPageAPI
    totalCaseTypeCount: MetaOapg.properties.totalCaseTypeCount
    totalPages: MetaOapg.properties.totalPages
    totalCaseCount: MetaOapg.properties.totalCaseCount
    results: MetaOapg.properties.results
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previousPageAPI"]) -> MetaOapg.properties.previousPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> MetaOapg.properties.results: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCaseCount"]) -> MetaOapg.properties.totalCaseCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCaseTypeCount"]) -> MetaOapg.properties.totalCaseTypeCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "object", "previousPageAPI", "results", "totalCaseCount", "totalCaseTypeCount", "totalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previousPageAPI"]) -> MetaOapg.properties.previousPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> MetaOapg.properties.results: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCaseCount"]) -> MetaOapg.properties.totalCaseCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCaseTypeCount"]) -> MetaOapg.properties.totalCaseTypeCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "object", "previousPageAPI", "results", "totalCaseCount", "totalCaseTypeCount", "totalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        nextPageAPI: typing.Union[MetaOapg.properties.nextPageAPI, None, str, ],
        previousPageAPI: typing.Union[MetaOapg.properties.previousPageAPI, None, str, ],
        totalCaseTypeCount: typing.Union[MetaOapg.properties.totalCaseTypeCount, decimal.Decimal, int, ],
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, ],
        totalCaseCount: typing.Union[MetaOapg.properties.totalCaseCount, decimal.Decimal, int, ],
        results: typing.Union[MetaOapg.properties.results, list, tuple, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseCountAnalyticsByCaseTypeResponse':
        return super().__new__(
            cls,
            *args,
            nextPageAPI=nextPageAPI,
            previousPageAPI=previousPageAPI,
            totalCaseTypeCount=totalCaseTypeCount,
            totalPages=totalPages,
            totalCaseCount=totalCaseCount,
            results=results,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_count_analytics_by_case_type import CaseCountAnalyticsByCaseType
