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


class CaseCountAnalyticsByAreaOfLaw(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "caseSearchAPI",
            "areaOfLaw",
            "caseCount",
            "object",
        }
        
        class properties:
        
            @staticmethod
            def areaOfLaw() -> typing.Type['AreaOfLaw']:
                return AreaOfLaw
            caseCount = schemas.IntSchema
            
            
            class caseSearchAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 29
            __annotations__ = {
                "areaOfLaw": areaOfLaw,
                "caseCount": caseCount,
                "caseSearchAPI": caseSearchAPI,
                "object": object,
            }
    
    caseSearchAPI: MetaOapg.properties.caseSearchAPI
    areaOfLaw: 'AreaOfLaw'
    caseCount: MetaOapg.properties.caseCount
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["areaOfLaw"]) -> 'AreaOfLaw': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["areaOfLaw", "caseCount", "caseSearchAPI", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["areaOfLaw"]) -> 'AreaOfLaw': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["areaOfLaw", "caseCount", "caseSearchAPI", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        caseSearchAPI: typing.Union[MetaOapg.properties.caseSearchAPI, str, ],
        areaOfLaw: 'AreaOfLaw',
        caseCount: typing.Union[MetaOapg.properties.caseCount, decimal.Decimal, int, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseCountAnalyticsByAreaOfLaw':
        return super().__new__(
            cls,
            *args,
            caseSearchAPI=caseSearchAPI,
            areaOfLaw=areaOfLaw,
            caseCount=caseCount,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.area_of_law import AreaOfLaw
