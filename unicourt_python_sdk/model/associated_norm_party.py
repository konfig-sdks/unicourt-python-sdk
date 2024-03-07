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


class AssociatedNormParty(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "caseSearchAPI",
            "normPartyAPI",
            "name",
            "caseTimeline",
            "caseCount",
            "normPartyId",
            "sosDataArray",
            "object",
        }
        
        class properties:
            caseCount = schemas.IntSchema
            
            
            class caseSearchAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
        
            @staticmethod
            def caseTimeline() -> typing.Type['CaseTimeline']:
                return CaseTimeline
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 500
            
            
            class normPartyAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
            
            
            class normPartyId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 18
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 19
            
            
            class sosDataArray(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SOSDataPreview']:
                        return SOSDataPreview
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SOSDataPreview'], typing.List['SOSDataPreview']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sosDataArray':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SOSDataPreview':
                    return super().__getitem__(i)
            __annotations__ = {
                "caseCount": caseCount,
                "caseSearchAPI": caseSearchAPI,
                "caseTimeline": caseTimeline,
                "name": name,
                "normPartyAPI": normPartyAPI,
                "normPartyId": normPartyId,
                "object": object,
                "sosDataArray": sosDataArray,
            }
    
    caseSearchAPI: MetaOapg.properties.caseSearchAPI
    normPartyAPI: MetaOapg.properties.normPartyAPI
    name: MetaOapg.properties.name
    caseTimeline: 'CaseTimeline'
    caseCount: MetaOapg.properties.caseCount
    normPartyId: MetaOapg.properties.normPartyId
    sosDataArray: MetaOapg.properties.sosDataArray
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseTimeline"]) -> 'CaseTimeline': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normPartyAPI"]) -> MetaOapg.properties.normPartyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normPartyId"]) -> MetaOapg.properties.normPartyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sosDataArray"]) -> MetaOapg.properties.sosDataArray: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["caseCount", "caseSearchAPI", "caseTimeline", "name", "normPartyAPI", "normPartyId", "object", "sosDataArray", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseTimeline"]) -> 'CaseTimeline': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normPartyAPI"]) -> MetaOapg.properties.normPartyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normPartyId"]) -> MetaOapg.properties.normPartyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sosDataArray"]) -> MetaOapg.properties.sosDataArray: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["caseCount", "caseSearchAPI", "caseTimeline", "name", "normPartyAPI", "normPartyId", "object", "sosDataArray", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        caseSearchAPI: typing.Union[MetaOapg.properties.caseSearchAPI, str, ],
        normPartyAPI: typing.Union[MetaOapg.properties.normPartyAPI, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        caseTimeline: 'CaseTimeline',
        caseCount: typing.Union[MetaOapg.properties.caseCount, decimal.Decimal, int, ],
        normPartyId: typing.Union[MetaOapg.properties.normPartyId, str, ],
        sosDataArray: typing.Union[MetaOapg.properties.sosDataArray, list, tuple, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssociatedNormParty':
        return super().__new__(
            cls,
            *args,
            caseSearchAPI=caseSearchAPI,
            normPartyAPI=normPartyAPI,
            name=name,
            caseTimeline=caseTimeline,
            caseCount=caseCount,
            normPartyId=normPartyId,
            sosDataArray=sosDataArray,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.case_timeline import CaseTimeline
from unicourt_python_sdk.model.sos_data_preview import SOSDataPreview
