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


class NormAttorneySearchResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "normAttorneySearchId",
            "q",
            "pageNumber",
            "nextPageAPI",
            "previousPageAPI",
            "totalPages",
            "totalCount",
            "normAttorneySearchResultArray",
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
                    max_length = 2120
                    min_length = 1
            
            
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
            
            
            class normAttorneySearchId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 18
            
            
            class normAttorneySearchResultArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NormAttorneySearchResult']:
                        return NormAttorneySearchResult
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['NormAttorneySearchResult'], typing.List['NormAttorneySearchResult']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'normAttorneySearchResultArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NormAttorneySearchResult':
                    return super().__getitem__(i)
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 26
                    min_length = 26
            
            
            class pageNumber(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
            
            
            class previousPageAPI(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 2119
                    min_length = 1
            
            
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
            
            
            class q(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2048
                    min_length = 3
            
            
            class totalCount(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
            
            
            class totalPages(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
            __annotations__ = {
                "nextPageAPI": nextPageAPI,
                "normAttorneySearchId": normAttorneySearchId,
                "normAttorneySearchResultArray": normAttorneySearchResultArray,
                "object": object,
                "pageNumber": pageNumber,
                "previousPageAPI": previousPageAPI,
                "q": q,
                "totalCount": totalCount,
                "totalPages": totalPages,
            }
    
    normAttorneySearchId: MetaOapg.properties.normAttorneySearchId
    q: MetaOapg.properties.q
    pageNumber: MetaOapg.properties.pageNumber
    nextPageAPI: MetaOapg.properties.nextPageAPI
    previousPageAPI: MetaOapg.properties.previousPageAPI
    totalPages: MetaOapg.properties.totalPages
    totalCount: MetaOapg.properties.totalCount
    normAttorneySearchResultArray: MetaOapg.properties.normAttorneySearchResultArray
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normAttorneySearchId"]) -> MetaOapg.properties.normAttorneySearchId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normAttorneySearchResultArray"]) -> MetaOapg.properties.normAttorneySearchResultArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previousPageAPI"]) -> MetaOapg.properties.previousPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["q"]) -> MetaOapg.properties.q: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "normAttorneySearchId", "normAttorneySearchResultArray", "object", "pageNumber", "previousPageAPI", "q", "totalCount", "totalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normAttorneySearchId"]) -> MetaOapg.properties.normAttorneySearchId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normAttorneySearchResultArray"]) -> MetaOapg.properties.normAttorneySearchResultArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previousPageAPI"]) -> MetaOapg.properties.previousPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["q"]) -> MetaOapg.properties.q: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "normAttorneySearchId", "normAttorneySearchResultArray", "object", "pageNumber", "previousPageAPI", "q", "totalCount", "totalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        normAttorneySearchId: typing.Union[MetaOapg.properties.normAttorneySearchId, str, ],
        q: typing.Union[MetaOapg.properties.q, str, ],
        pageNumber: typing.Union[MetaOapg.properties.pageNumber, decimal.Decimal, int, ],
        nextPageAPI: typing.Union[MetaOapg.properties.nextPageAPI, None, str, ],
        previousPageAPI: typing.Union[MetaOapg.properties.previousPageAPI, None, str, ],
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, ],
        totalCount: typing.Union[MetaOapg.properties.totalCount, decimal.Decimal, int, ],
        normAttorneySearchResultArray: typing.Union[MetaOapg.properties.normAttorneySearchResultArray, list, tuple, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NormAttorneySearchResponse':
        return super().__new__(
            cls,
            *args,
            normAttorneySearchId=normAttorneySearchId,
            q=q,
            pageNumber=pageNumber,
            nextPageAPI=nextPageAPI,
            previousPageAPI=previousPageAPI,
            totalPages=totalPages,
            totalCount=totalCount,
            normAttorneySearchResultArray=normAttorneySearchResultArray,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.norm_attorney_search_result import NormAttorneySearchResult