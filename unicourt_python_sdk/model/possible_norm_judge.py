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


class PossibleNormJudge(
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
            "associatedNormAttorneysAPI",
            "caseCountAnalyticsByNormJudgeAPI",
            "associatedNormLawFirmsAPI",
            "normJudgeAPI",
            "normJudgeId",
            "scoreConstituents",
            "normJudgeName",
            "object",
        }
        
        class properties:
            
            
            class associatedNormAttorneysAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
            
            
            class associatedNormLawFirmsAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
            
            
            class associatedNormPartiesAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
            bestMatch = schemas.BoolSchema
            
            
            class caseCountAnalyticsByNormJudgeAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 250
            
            
            class confidenceScore(
                schemas.Float32Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'float'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'confidenceScore':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class normJudgeAPI(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'uri'
                    max_length = 255
            
            
            class normJudgeId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 18
                    min_length = 18
            
            
            class normJudgeName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 500
            
            
            class object(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 17
                    min_length = 17
        
            @staticmethod
            def scoreConstituents() -> typing.Type['PossibleNormJudgeScoreConstituents']:
                return PossibleNormJudgeScoreConstituents
            __annotations__ = {
                "associatedNormAttorneysAPI": associatedNormAttorneysAPI,
                "associatedNormLawFirmsAPI": associatedNormLawFirmsAPI,
                "associatedNormPartiesAPI": associatedNormPartiesAPI,
                "bestMatch": bestMatch,
                "caseCountAnalyticsByNormJudgeAPI": caseCountAnalyticsByNormJudgeAPI,
                "confidenceScore": confidenceScore,
                "normJudgeAPI": normJudgeAPI,
                "normJudgeId": normJudgeId,
                "normJudgeName": normJudgeName,
                "object": object,
                "scoreConstituents": scoreConstituents,
            }

    
    associatedNormPartiesAPI: MetaOapg.properties.associatedNormPartiesAPI
    confidenceScore: MetaOapg.properties.confidenceScore
    bestMatch: MetaOapg.properties.bestMatch
    associatedNormAttorneysAPI: MetaOapg.properties.associatedNormAttorneysAPI
    caseCountAnalyticsByNormJudgeAPI: MetaOapg.properties.caseCountAnalyticsByNormJudgeAPI
    associatedNormLawFirmsAPI: MetaOapg.properties.associatedNormLawFirmsAPI
    normJudgeAPI: MetaOapg.properties.normJudgeAPI
    normJudgeId: MetaOapg.properties.normJudgeId
    scoreConstituents: 'PossibleNormJudgeScoreConstituents'
    normJudgeName: MetaOapg.properties.normJudgeName
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormAttorneysAPI"]) -> MetaOapg.properties.associatedNormAttorneysAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormLawFirmsAPI"]) -> MetaOapg.properties.associatedNormLawFirmsAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedNormPartiesAPI"]) -> MetaOapg.properties.associatedNormPartiesAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bestMatch"]) -> MetaOapg.properties.bestMatch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseCountAnalyticsByNormJudgeAPI"]) -> MetaOapg.properties.caseCountAnalyticsByNormJudgeAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confidenceScore"]) -> MetaOapg.properties.confidenceScore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normJudgeAPI"]) -> MetaOapg.properties.normJudgeAPI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normJudgeId"]) -> MetaOapg.properties.normJudgeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normJudgeName"]) -> MetaOapg.properties.normJudgeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scoreConstituents"]) -> 'PossibleNormJudgeScoreConstituents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["associatedNormAttorneysAPI", "associatedNormLawFirmsAPI", "associatedNormPartiesAPI", "bestMatch", "caseCountAnalyticsByNormJudgeAPI", "confidenceScore", "normJudgeAPI", "normJudgeId", "normJudgeName", "object", "scoreConstituents", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormAttorneysAPI"]) -> MetaOapg.properties.associatedNormAttorneysAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormLawFirmsAPI"]) -> MetaOapg.properties.associatedNormLawFirmsAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedNormPartiesAPI"]) -> MetaOapg.properties.associatedNormPartiesAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bestMatch"]) -> MetaOapg.properties.bestMatch: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseCountAnalyticsByNormJudgeAPI"]) -> MetaOapg.properties.caseCountAnalyticsByNormJudgeAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confidenceScore"]) -> MetaOapg.properties.confidenceScore: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normJudgeAPI"]) -> MetaOapg.properties.normJudgeAPI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normJudgeId"]) -> MetaOapg.properties.normJudgeId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normJudgeName"]) -> MetaOapg.properties.normJudgeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scoreConstituents"]) -> 'PossibleNormJudgeScoreConstituents': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["associatedNormAttorneysAPI", "associatedNormLawFirmsAPI", "associatedNormPartiesAPI", "bestMatch", "caseCountAnalyticsByNormJudgeAPI", "confidenceScore", "normJudgeAPI", "normJudgeId", "normJudgeName", "object", "scoreConstituents", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PossibleNormJudge':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from unicourt_python_sdk.model.possible_norm_judge_score_constituents import PossibleNormJudgeScoreConstituents
