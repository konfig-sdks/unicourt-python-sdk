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


class PACERCaseSearchResults(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "uniCourtContent",
            "hasOnlyMetaInfo",
            "pacerContent",
            "object",
        }
        
        class properties:
            hasOnlyMetaInfo = schemas.BoolSchema
            
            
            class object(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def pacerContent() -> typing.Type['PACERCaseSearchContent']:
                return PACERCaseSearchContent
        
            @staticmethod
            def uniCourtContent() -> typing.Type['CaseSearchResult']:
                return CaseSearchResult
            __annotations__ = {
                "hasOnlyMetaInfo": hasOnlyMetaInfo,
                "object": object,
                "pacerContent": pacerContent,
                "uniCourtContent": uniCourtContent,
            }
    
    uniCourtContent: 'CaseSearchResult'
    hasOnlyMetaInfo: MetaOapg.properties.hasOnlyMetaInfo
    pacerContent: 'PACERCaseSearchContent'
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasOnlyMetaInfo"]) -> MetaOapg.properties.hasOnlyMetaInfo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pacerContent"]) -> 'PACERCaseSearchContent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uniCourtContent"]) -> 'CaseSearchResult': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hasOnlyMetaInfo", "object", "pacerContent", "uniCourtContent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasOnlyMetaInfo"]) -> MetaOapg.properties.hasOnlyMetaInfo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pacerContent"]) -> 'PACERCaseSearchContent': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uniCourtContent"]) -> 'CaseSearchResult': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hasOnlyMetaInfo", "object", "pacerContent", "uniCourtContent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uniCourtContent: 'CaseSearchResult',
        hasOnlyMetaInfo: typing.Union[MetaOapg.properties.hasOnlyMetaInfo, bool, ],
        pacerContent: 'PACERCaseSearchContent',
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PACERCaseSearchResults':
        return super().__new__(
            cls,
            *args,
            uniCourtContent=uniCourtContent,
            hasOnlyMetaInfo=hasOnlyMetaInfo,
            pacerContent=pacerContent,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_search_result import CaseSearchResult
from unicourt_python_sdk.model.pacer_case_search_content import PACERCaseSearchContent
