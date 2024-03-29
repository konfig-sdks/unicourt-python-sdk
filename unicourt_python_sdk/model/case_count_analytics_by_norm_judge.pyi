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


class CaseCountAnalyticsByNormJudge(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "caseSearchAPI",
            "normJudgeId",
            "caseCount",
            "normJudgeName",
            "object",
        }
        
        class properties:
            caseCount = schemas.IntSchema
            
            
            class caseSearchAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class normJudgeId(
                schemas.StrSchema
            ):
                pass
            
            
            class normJudgeName(
                schemas.StrSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "caseCount": caseCount,
                "caseSearchAPI": caseSearchAPI,
                "normJudgeId": normJudgeId,
                "normJudgeName": normJudgeName,
                "object": object,
            }
    
    caseSearchAPI: MetaOapg.properties.caseSearchAPI
    normJudgeId: MetaOapg.properties.normJudgeId
    caseCount: MetaOapg.properties.caseCount
    normJudgeName: MetaOapg.properties.normJudgeName
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normJudgeId"]) -> MetaOapg.properties.normJudgeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normJudgeName"]) -> MetaOapg.properties.normJudgeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["caseCount", "caseSearchAPI", "normJudgeId", "normJudgeName", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCount"]) -> MetaOapg.properties.caseCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseSearchAPI"]) -> MetaOapg.properties.caseSearchAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normJudgeId"]) -> MetaOapg.properties.normJudgeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normJudgeName"]) -> MetaOapg.properties.normJudgeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["caseCount", "caseSearchAPI", "normJudgeId", "normJudgeName", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        caseSearchAPI: typing.Union[MetaOapg.properties.caseSearchAPI, str, ],
        normJudgeId: typing.Union[MetaOapg.properties.normJudgeId, str, ],
        caseCount: typing.Union[MetaOapg.properties.caseCount, decimal.Decimal, int, ],
        normJudgeName: typing.Union[MetaOapg.properties.normJudgeName, str, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CaseCountAnalyticsByNormJudge':
        return super().__new__(
            cls,
            *args,
            caseSearchAPI=caseSearchAPI,
            normJudgeId=normJudgeId,
            caseCount=caseCount,
            normJudgeName=normJudgeName,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )
