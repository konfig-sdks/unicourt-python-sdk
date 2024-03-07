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


class NormLawFirmSearchResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "normLawFirmSearchId",
            "q",
            "pageNumber",
            "nextPageAPI",
            "normLawFirmSearchResultArray",
            "previousPageAPI",
            "totalPages",
            "totalCount",
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
            
            
            class normLawFirmSearchId(
                schemas.StrSchema
            ):
                pass
            
            
            class normLawFirmSearchResultArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NormLawFirmSearchResult']:
                        return NormLawFirmSearchResult
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['NormLawFirmSearchResult'], typing.List['NormLawFirmSearchResult']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'normLawFirmSearchResultArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NormLawFirmSearchResult':
                    return super().__getitem__(i)
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            
            
            class pageNumber(
                schemas.IntSchema
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
            
            
            class q(
                schemas.StrSchema
            ):
                pass
            
            
            class totalCount(
                schemas.IntSchema
            ):
                pass
            
            
            class totalPages(
                schemas.IntSchema
            ):
                pass
            __annotations__ = {
                "nextPageAPI": nextPageAPI,
                "normLawFirmSearchId": normLawFirmSearchId,
                "normLawFirmSearchResultArray": normLawFirmSearchResultArray,
                "object": object,
                "pageNumber": pageNumber,
                "previousPageAPI": previousPageAPI,
                "q": q,
                "totalCount": totalCount,
                "totalPages": totalPages,
            }
    
    normLawFirmSearchId: MetaOapg.properties.normLawFirmSearchId
    q: MetaOapg.properties.q
    pageNumber: MetaOapg.properties.pageNumber
    nextPageAPI: MetaOapg.properties.nextPageAPI
    normLawFirmSearchResultArray: MetaOapg.properties.normLawFirmSearchResultArray
    previousPageAPI: MetaOapg.properties.previousPageAPI
    totalPages: MetaOapg.properties.totalPages
    totalCount: MetaOapg.properties.totalCount
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normLawFirmSearchId"]) -> MetaOapg.properties.normLawFirmSearchId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normLawFirmSearchResultArray"]) -> MetaOapg.properties.normLawFirmSearchResultArray: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "normLawFirmSearchId", "normLawFirmSearchResultArray", "object", "pageNumber", "previousPageAPI", "q", "totalCount", "totalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normLawFirmSearchId"]) -> MetaOapg.properties.normLawFirmSearchId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normLawFirmSearchResultArray"]) -> MetaOapg.properties.normLawFirmSearchResultArray: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "normLawFirmSearchId", "normLawFirmSearchResultArray", "object", "pageNumber", "previousPageAPI", "q", "totalCount", "totalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        normLawFirmSearchId: typing.Union[MetaOapg.properties.normLawFirmSearchId, str, ],
        q: typing.Union[MetaOapg.properties.q, str, ],
        pageNumber: typing.Union[MetaOapg.properties.pageNumber, decimal.Decimal, int, ],
        nextPageAPI: typing.Union[MetaOapg.properties.nextPageAPI, None, str, ],
        normLawFirmSearchResultArray: typing.Union[MetaOapg.properties.normLawFirmSearchResultArray, list, tuple, ],
        previousPageAPI: typing.Union[MetaOapg.properties.previousPageAPI, None, str, ],
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, ],
        totalCount: typing.Union[MetaOapg.properties.totalCount, decimal.Decimal, int, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NormLawFirmSearchResponse':
        return super().__new__(
            cls,
            *args,
            normLawFirmSearchId=normLawFirmSearchId,
            q=q,
            pageNumber=pageNumber,
            nextPageAPI=nextPageAPI,
            normLawFirmSearchResultArray=normLawFirmSearchResultArray,
            previousPageAPI=previousPageAPI,
            totalPages=totalPages,
            totalCount=totalCount,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.norm_law_firm_search_result import NormLawFirmSearchResult
