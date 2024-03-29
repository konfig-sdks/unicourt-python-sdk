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


class PossibleNormAttorney(
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
            "associatedNormPartiesAPI",
            "confidenceScore",
            "bestMatch",
            "associatedNormJudgesAPI",
            "normAttorneyId",
            "associatedNormLawFirmsAPI",
            "scoreConstituents",
            "caseCountAnalyticsByOpposingNormAttorneyAPI",
            "normAttorneyName",
            "caseCountAnalyticsByNormAttorneyAPI",
            "normAttorneyAPI",
            "object",
        }
        
        class properties:
            
            
            class associatedNormJudgesAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class associatedNormLawFirmsAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class associatedNormPartiesAPI(
                schemas.StrSchema
            ):
                pass
            bestMatch = schemas.BoolSchema
            
            
            class caseCountAnalyticsByNormAttorneyAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class caseCountAnalyticsByOpposingNormAttorneyAPI(
                schemas.StrSchema
            ):
                pass
            confidenceScore = schemas.Float32Schema
            
            
            class normAttorneyAPI(
                schemas.StrSchema
            ):
                pass
            
            
            class normAttorneyId(
                schemas.StrSchema
            ):
                pass
            
            
            class normAttorneyName(
                schemas.StrSchema
            ):
                pass
            
            
            class object(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def scoreConstituents() -> typing.Type['PossibleNormAttorneyScoreConstituents']:
                return PossibleNormAttorneyScoreConstituents
            __annotations__ = {
                "associatedNormJudgesAPI": associatedNormJudgesAPI,
                "associatedNormLawFirmsAPI": associatedNormLawFirmsAPI,
                "associatedNormPartiesAPI": associatedNormPartiesAPI,
                "bestMatch": bestMatch,
                "caseCountAnalyticsByNormAttorneyAPI": caseCountAnalyticsByNormAttorneyAPI,
                "caseCountAnalyticsByOpposingNormAttorneyAPI": caseCountAnalyticsByOpposingNormAttorneyAPI,
                "confidenceScore": confidenceScore,
                "normAttorneyAPI": normAttorneyAPI,
                "normAttorneyId": normAttorneyId,
                "normAttorneyName": normAttorneyName,
                "object": object,
                "scoreConstituents": scoreConstituents,
            }

    
    associatedNormPartiesAPI: MetaOapg.properties.associatedNormPartiesAPI
    confidenceScore: MetaOapg.properties.confidenceScore
    bestMatch: MetaOapg.properties.bestMatch
    associatedNormJudgesAPI: MetaOapg.properties.associatedNormJudgesAPI
    normAttorneyId: MetaOapg.properties.normAttorneyId
    associatedNormLawFirmsAPI: MetaOapg.properties.associatedNormLawFirmsAPI
    scoreConstituents: 'PossibleNormAttorneyScoreConstituents'
    caseCountAnalyticsByOpposingNormAttorneyAPI: MetaOapg.properties.caseCountAnalyticsByOpposingNormAttorneyAPI
    normAttorneyName: MetaOapg.properties.normAttorneyName
    caseCountAnalyticsByNormAttorneyAPI: MetaOapg.properties.caseCountAnalyticsByNormAttorneyAPI
    normAttorneyAPI: MetaOapg.properties.normAttorneyAPI
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormJudgesAPI"]) -> MetaOapg.properties.associatedNormJudgesAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormLawFirmsAPI"]) -> MetaOapg.properties.associatedNormLawFirmsAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormPartiesAPI"]) -> MetaOapg.properties.associatedNormPartiesAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bestMatch"]) -> MetaOapg.properties.bestMatch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCountAnalyticsByNormAttorneyAPI"]) -> MetaOapg.properties.caseCountAnalyticsByNormAttorneyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormAttorneyAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormAttorneyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confidenceScore"]) -> MetaOapg.properties.confidenceScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normAttorneyAPI"]) -> MetaOapg.properties.normAttorneyAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normAttorneyId"]) -> MetaOapg.properties.normAttorneyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normAttorneyName"]) -> MetaOapg.properties.normAttorneyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreConstituents"]) -> 'PossibleNormAttorneyScoreConstituents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["associatedNormJudgesAPI", "associatedNormLawFirmsAPI", "associatedNormPartiesAPI", "bestMatch", "caseCountAnalyticsByNormAttorneyAPI", "caseCountAnalyticsByOpposingNormAttorneyAPI", "confidenceScore", "normAttorneyAPI", "normAttorneyId", "normAttorneyName", "object", "scoreConstituents", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormJudgesAPI"]) -> MetaOapg.properties.associatedNormJudgesAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormLawFirmsAPI"]) -> MetaOapg.properties.associatedNormLawFirmsAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormPartiesAPI"]) -> MetaOapg.properties.associatedNormPartiesAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bestMatch"]) -> MetaOapg.properties.bestMatch: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCountAnalyticsByNormAttorneyAPI"]) -> MetaOapg.properties.caseCountAnalyticsByNormAttorneyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCountAnalyticsByOpposingNormAttorneyAPI"]) -> MetaOapg.properties.caseCountAnalyticsByOpposingNormAttorneyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confidenceScore"]) -> MetaOapg.properties.confidenceScore: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normAttorneyAPI"]) -> MetaOapg.properties.normAttorneyAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normAttorneyId"]) -> MetaOapg.properties.normAttorneyId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normAttorneyName"]) -> MetaOapg.properties.normAttorneyName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreConstituents"]) -> 'PossibleNormAttorneyScoreConstituents': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["associatedNormJudgesAPI", "associatedNormLawFirmsAPI", "associatedNormPartiesAPI", "bestMatch", "caseCountAnalyticsByNormAttorneyAPI", "caseCountAnalyticsByOpposingNormAttorneyAPI", "confidenceScore", "normAttorneyAPI", "normAttorneyId", "normAttorneyName", "object", "scoreConstituents", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PossibleNormAttorney':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.possible_norm_attorney_score_constituents import PossibleNormAttorneyScoreConstituents
