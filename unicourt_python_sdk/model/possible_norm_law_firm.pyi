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


class PossibleNormLawFirm(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "normLawFirmName",
            "scoreConstituents",
            "associatedNormAttorneyAPI",
            "normLawFirmAPI",
            "associatedNormPartiesAPI",
            "confidenceScore",
            "bestMatch",
            "normLawFirmId",
            "associatedNormJudgeAPI",
            "caseCountAnalyticsByOpposingNormLawFirmAPI",
            "sourceDetails",
            "caseCountAnalyticsByNormLawFirmAPI",
            "object",
        }
        
        class properties:
            
            
            class associatedNormAttorneyAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class associatedNormJudgeAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class associatedNormPartiesAPI(
                schemas.StrSchema
            ):
                pass
            bestMatch = schemas.BoolSchema
            
            
            class caseCountAnalyticsByNormLawFirmAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class caseCountAnalyticsByOpposingNormLawFirmAPI(
                schemas.StrSchema
            ):
                pass
            confidenceScore = schemas.Float32Schema
            
            
            class normLawFirmAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class normLawFirmId(
                schemas.StrSchema
            ):
                pass
            
            
            class normLawFirmName(
                schemas.StrSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def scoreConstituents() -> typing.Type['PossibleNormLawFirmScoreConstituents']:
                return PossibleNormLawFirmScoreConstituents
        
            @staticmethod
            def sourceDetails() -> typing.Type['PossibleNormLawFirmSourceDetails']:
                return PossibleNormLawFirmSourceDetails
            __annotations__ = {
                "associatedNormAttorneyAPI": associatedNormAttorneyAPI,
                "associatedNormJudgeAPI": associatedNormJudgeAPI,
                "associatedNormPartiesAPI": associatedNormPartiesAPI,
                "bestMatch": bestMatch,
                "caseCountAnalyticsByNormLawFirmAPI": caseCountAnalyticsByNormLawFirmAPI,
                "caseCountAnalyticsByOpposingNormLawFirmAPI": caseCountAnalyticsByOpposingNormLawFirmAPI,
                "confidenceScore": confidenceScore,
                "normLawFirmAPI": normLawFirmAPI,
                "normLawFirmId": normLawFirmId,
                "normLawFirmName": normLawFirmName,
                "object": object,
                "scoreConstituents": scoreConstituents,
                "sourceDetails": sourceDetails,
            }

    
    normLawFirmName: MetaOapg.properties.normLawFirmName
    scoreConstituents: 'PossibleNormLawFirmScoreConstituents'
    associatedNormAttorneyAPI: MetaOapg.properties.associatedNormAttorneyAPI
    normLawFirmAPI: MetaOapg.properties.normLawFirmAPI
    associatedNormPartiesAPI: MetaOapg.properties.associatedNormPartiesAPI
    confidenceScore: MetaOapg.properties.confidenceScore
    bestMatch: MetaOapg.properties.bestMatch
    normLawFirmId: MetaOapg.properties.normLawFirmId
    associatedNormJudgeAPI: MetaOapg.properties.associatedNormJudgeAPI
    caseCountAnalyticsByOpposingNormLawFirmAPI: MetaOapg.properties.caseCountAnalyticsByOpposingNormLawFirmAPI
    sourceDetails: 'PossibleNormLawFirmSourceDetails'
    caseCountAnalyticsByNormLawFirmAPI: MetaOapg.properties.caseCountAnalyticsByNormLawFirmAPI
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormAttorneyAPI"]) -> MetaOapg.properties.associatedNormAttorneyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormJudgeAPI"]) -> MetaOapg.properties.associatedNormJudgeAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormPartiesAPI"]) -> MetaOapg.properties.associatedNormPartiesAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bestMatch"]) -> MetaOapg.properties.bestMatch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCountAnalyticsByNormLawFirmAPI"]) -> MetaOapg.properties.caseCountAnalyticsByNormLawFirmAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormLawFirmAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormLawFirmAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confidenceScore"]) -> MetaOapg.properties.confidenceScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normLawFirmAPI"]) -> MetaOapg.properties.normLawFirmAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normLawFirmId"]) -> MetaOapg.properties.normLawFirmId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normLawFirmName"]) -> MetaOapg.properties.normLawFirmName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreConstituents"]) -> 'PossibleNormLawFirmScoreConstituents': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceDetails"]) -> 'PossibleNormLawFirmSourceDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["associatedNormAttorneyAPI", "associatedNormJudgeAPI", "associatedNormPartiesAPI", "bestMatch", "caseCountAnalyticsByNormLawFirmAPI", "caseCountAnalyticsByOpposingNormLawFirmAPI", "confidenceScore", "normLawFirmAPI", "normLawFirmId", "normLawFirmName", "object", "scoreConstituents", "sourceDetails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormAttorneyAPI"]) -> MetaOapg.properties.associatedNormAttorneyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormJudgeAPI"]) -> MetaOapg.properties.associatedNormJudgeAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormPartiesAPI"]) -> MetaOapg.properties.associatedNormPartiesAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bestMatch"]) -> MetaOapg.properties.bestMatch: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCountAnalyticsByNormLawFirmAPI"]) -> MetaOapg.properties.caseCountAnalyticsByNormLawFirmAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormLawFirmAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormLawFirmAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confidenceScore"]) -> MetaOapg.properties.confidenceScore: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normLawFirmAPI"]) -> MetaOapg.properties.normLawFirmAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normLawFirmId"]) -> MetaOapg.properties.normLawFirmId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normLawFirmName"]) -> MetaOapg.properties.normLawFirmName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreConstituents"]) -> 'PossibleNormLawFirmScoreConstituents': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceDetails"]) -> 'PossibleNormLawFirmSourceDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["associatedNormAttorneyAPI", "associatedNormJudgeAPI", "associatedNormPartiesAPI", "bestMatch", "caseCountAnalyticsByNormLawFirmAPI", "caseCountAnalyticsByOpposingNormLawFirmAPI", "confidenceScore", "normLawFirmAPI", "normLawFirmId", "normLawFirmName", "object", "scoreConstituents", "sourceDetails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PossibleNormLawFirm':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.possible_norm_law_firm_score_constituents import PossibleNormLawFirmScoreConstituents
from unicourt_python_sdk.model.possible_norm_law_firm_source_details import PossibleNormLawFirmSourceDetails
