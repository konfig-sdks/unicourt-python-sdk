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


class AttorneyTypeResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "pageNumber",
            "nextPageAPI",
            "previousPageAPI",
            "totalPages",
            "attorneyTypeArray",
            "totalCount",
            "object",
        }
        
        class properties:
            
            
            class attorneyTypeArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AttorneyType']:
                        return AttorneyType
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AttorneyType'], typing.List['AttorneyType']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attorneyTypeArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AttorneyType':
                    return super().__getitem__(i)
            
            
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
            
            
            class totalCount(
                schemas.IntSchema
            ):
                pass
            
            
            class totalPages(
                schemas.IntSchema
            ):
                pass
            __annotations__ = {
                "attorneyTypeArray": attorneyTypeArray,
                "nextPageAPI": nextPageAPI,
                "object": object,
                "pageNumber": pageNumber,
                "previousPageAPI": previousPageAPI,
                "totalCount": totalCount,
                "totalPages": totalPages,
            }
    
    pageNumber: MetaOapg.properties.pageNumber
    nextPageAPI: MetaOapg.properties.nextPageAPI
    previousPageAPI: MetaOapg.properties.previousPageAPI
    totalPages: MetaOapg.properties.totalPages
    attorneyTypeArray: MetaOapg.properties.attorneyTypeArray
    totalCount: MetaOapg.properties.totalCount
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attorneyTypeArray"]) -> MetaOapg.properties.attorneyTypeArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previousPageAPI"]) -> MetaOapg.properties.previousPageAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attorneyTypeArray", "nextPageAPI", "object", "pageNumber", "previousPageAPI", "totalCount", "totalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attorneyTypeArray"]) -> MetaOapg.properties.attorneyTypeArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextPageAPI"]) -> MetaOapg.properties.nextPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previousPageAPI"]) -> MetaOapg.properties.previousPageAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attorneyTypeArray", "nextPageAPI", "object", "pageNumber", "previousPageAPI", "totalCount", "totalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pageNumber: typing.Union[MetaOapg.properties.pageNumber, decimal.Decimal, int, ],
        nextPageAPI: typing.Union[MetaOapg.properties.nextPageAPI, None, str, ],
        previousPageAPI: typing.Union[MetaOapg.properties.previousPageAPI, None, str, ],
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, ],
        attorneyTypeArray: typing.Union[MetaOapg.properties.attorneyTypeArray, list, tuple, ],
        totalCount: typing.Union[MetaOapg.properties.totalCount, decimal.Decimal, int, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AttorneyTypeResponse':
        return super().__new__(
            cls,
            *args,
            pageNumber=pageNumber,
            nextPageAPI=nextPageAPI,
            previousPageAPI=previousPageAPI,
            totalPages=totalPages,
            attorneyTypeArray=attorneyTypeArray,
            totalCount=totalCount,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.attorney_type import AttorneyType
