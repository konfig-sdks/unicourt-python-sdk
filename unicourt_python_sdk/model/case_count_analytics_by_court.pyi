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


class CaseCountAnalyticsByCourt(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "Geo",
            "caseSearchAPI",
            "caseCount",
            "court",
            "object",
        }
        
        class properties:
        
            @staticmethod
            def Geo() -> typing.Type['CaseCountAnalyticsByCourtGeo']:
                return CaseCountAnalyticsByCourtGeo
            caseCount = schemas.IntSchema
            
            
            class caseSearchAPI(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def court() -> typing.Type['Court']:
                return Court
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "Geo": Geo,
                "caseCount": caseCount,
                "caseSearchAPI": caseSearchAPI,
                "court": court,
                "object": object,
            }
    
    Geo: 'CaseCountAnalyticsByCourtGeo'
    caseSearchAPI: MetaOapg.properties.caseSearchAPI
    caseCount: MetaOapg.properties.caseCount
    court: 'Court'
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Geo"]) -> 'CaseCountAnalyticsByCourtGeo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["court"]) -> 'Court': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Geo", "caseCount", "caseSearchAPI", "court", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Geo"]) -> 'CaseCountAnalyticsByCourtGeo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["court"]) -> 'Court': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Geo", "caseCount", "caseSearchAPI", "court", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Geo: 'CaseCountAnalyticsByCourtGeo',
        caseSearchAPI: typing.Union[MetaOapg.properties.caseSearchAPI, str, ],
        caseCount: typing.Union[MetaOapg.properties.caseCount, decimal.Decimal, int, ],
        court: 'Court',
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseCountAnalyticsByCourt':
        return super().__new__(
            cls,
            *args,
            Geo=Geo,
            caseSearchAPI=caseSearchAPI,
            caseCount=caseCount,
            court=court,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_count_analytics_by_court_geo import CaseCountAnalyticsByCourtGeo
from unicourt_python_sdk.model.court import Court
