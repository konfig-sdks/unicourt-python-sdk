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


class CaseCountAnalyticsByPartyRoleResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Case Count by Party Type Response.
    """


    class MetaOapg:
        required = {
            "nextPageAPI",
            "previousPageAPI",
            "totalPages",
            "totalCaseCount",
            "results",
            "object",
            "totalPartyRoleCount",
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
                    max_length = 2173
            
            
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
            
            
                class MetaOapg:
                    max_length = 37
            
            
            class previousPageAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 2172
            
            
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
                    def items() -> typing.Type['CaseCountAnalyticsByPartyRole']:
                        return CaseCountAnalyticsByPartyRole
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CaseCountAnalyticsByPartyRole'], typing.List['CaseCountAnalyticsByPartyRole']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'results':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CaseCountAnalyticsByPartyRole':
                    return super().__getitem__(i)
            totalCaseCount = schemas.IntSchema
            totalPages = schemas.IntSchema
            totalPartyRoleCount = schemas.IntSchema
            __annotations__ = {
                "nextPageAPI": nextPageAPI,
                "object": object,
                "previousPageAPI": previousPageAPI,
                "results": results,
                "totalCaseCount": totalCaseCount,
                "totalPages": totalPages,
                "totalPartyRoleCount": totalPartyRoleCount,
            }
    
    nextPageAPI: MetaOapg.properties.nextPageAPI
    previousPageAPI: MetaOapg.properties.previousPageAPI
    totalPages: MetaOapg.properties.totalPages
    totalCaseCount: MetaOapg.properties.totalCaseCount
    results: MetaOapg.properties.results
    object: MetaOapg.properties.object
    totalPartyRoleCount: MetaOapg.properties.totalPartyRoleCount
    
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
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPartyRoleCount"]) -> MetaOapg.properties.totalPartyRoleCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "object", "previousPageAPI", "results", "totalCaseCount", "totalPages", "totalPartyRoleCount", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPartyRoleCount"]) -> MetaOapg.properties.totalPartyRoleCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "object", "previousPageAPI", "results", "totalCaseCount", "totalPages", "totalPartyRoleCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        nextPageAPI: typing.Union[MetaOapg.properties.nextPageAPI, None, str, ],
        previousPageAPI: typing.Union[MetaOapg.properties.previousPageAPI, None, str, ],
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, ],
        totalCaseCount: typing.Union[MetaOapg.properties.totalCaseCount, decimal.Decimal, int, ],
        results: typing.Union[MetaOapg.properties.results, list, tuple, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        totalPartyRoleCount: typing.Union[MetaOapg.properties.totalPartyRoleCount, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseCountAnalyticsByPartyRoleResponse':
        return super().__new__(
            cls,
            *args,
            nextPageAPI=nextPageAPI,
            previousPageAPI=previousPageAPI,
            totalPages=totalPages,
            totalCaseCount=totalCaseCount,
            results=results,
            object=object,
            totalPartyRoleCount=totalPartyRoleCount,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_count_analytics_by_party_role import CaseCountAnalyticsByPartyRole
