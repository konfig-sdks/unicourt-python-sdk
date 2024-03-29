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


class PCLParty(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "pacerSearchResultsArray",
            "pageNumber",
            "nextPageAPI",
            "totalPages",
            "pacerPageInfo",
            "totalCount",
            "pacerReceipt",
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
                    max_length = 255
            
            
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
                    max_length = 8
                    min_length = 8
        
            @staticmethod
            def pacerPageInfo() -> typing.Type['PACERSearchPageInfo']:
                return PACERSearchPageInfo
        
            @staticmethod
            def pacerReceipt() -> typing.Type['PACERSearchReceipt']:
                return PACERSearchReceipt
            
            
            class pacerSearchResultsArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PACERPartySearchResults']:
                        return PACERPartySearchResults
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PACERPartySearchResults'], typing.List['PACERPartySearchResults']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pacerSearchResultsArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PACERPartySearchResults':
                    return super().__getitem__(i)
            pageNumber = schemas.IntSchema
            totalCount = schemas.IntSchema
            totalPages = schemas.IntSchema
            __annotations__ = {
                "nextPageAPI": nextPageAPI,
                "object": object,
                "pacerPageInfo": pacerPageInfo,
                "pacerReceipt": pacerReceipt,
                "pacerSearchResultsArray": pacerSearchResultsArray,
                "pageNumber": pageNumber,
                "totalCount": totalCount,
                "totalPages": totalPages,
            }
    
    pacerSearchResultsArray: MetaOapg.properties.pacerSearchResultsArray
    pageNumber: MetaOapg.properties.pageNumber
    nextPageAPI: MetaOapg.properties.nextPageAPI
    totalPages: MetaOapg.properties.totalPages
    pacerPageInfo: 'PACERSearchPageInfo'
    totalCount: MetaOapg.properties.totalCount
    pacerReceipt: 'PACERSearchReceipt'
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pacerPageInfo"]) -> 'PACERSearchPageInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pacerReceipt"]) -> 'PACERSearchReceipt': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pacerSearchResultsArray"]) -> MetaOapg.properties.pacerSearchResultsArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "object", "pacerPageInfo", "pacerReceipt", "pacerSearchResultsArray", "pageNumber", "totalCount", "totalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pacerPageInfo"]) -> 'PACERSearchPageInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pacerReceipt"]) -> 'PACERSearchReceipt': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pacerSearchResultsArray"]) -> MetaOapg.properties.pacerSearchResultsArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nextPageAPI", "object", "pacerPageInfo", "pacerReceipt", "pacerSearchResultsArray", "pageNumber", "totalCount", "totalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pacerSearchResultsArray: typing.Union[MetaOapg.properties.pacerSearchResultsArray, list, tuple, ],
        pageNumber: typing.Union[MetaOapg.properties.pageNumber, decimal.Decimal, int, ],
        nextPageAPI: typing.Union[MetaOapg.properties.nextPageAPI, None, str, ],
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, ],
        pacerPageInfo: 'PACERSearchPageInfo',
        totalCount: typing.Union[MetaOapg.properties.totalCount, decimal.Decimal, int, ],
        pacerReceipt: 'PACERSearchReceipt',
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PCLParty':
        return super().__new__(
            cls,
            *args,
            pacerSearchResultsArray=pacerSearchResultsArray,
            pageNumber=pageNumber,
            nextPageAPI=nextPageAPI,
            totalPages=totalPages,
            pacerPageInfo=pacerPageInfo,
            totalCount=totalCount,
            pacerReceipt=pacerReceipt,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.pacer_party_search_results import PACERPartySearchResults
from unicourt_python_sdk.model.pacer_search_page_info import PACERSearchPageInfo
from unicourt_python_sdk.model.pacer_search_receipt import PACERSearchReceipt
