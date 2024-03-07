# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from unicourt_python_sdk.type.possible_norm_law_firm_score_constituents import PossibleNormLawFirmScoreConstituents
from unicourt_python_sdk.type.possible_norm_law_firm_source_details import PossibleNormLawFirmSourceDetails

class RequiredPossibleNormLawFirm(TypedDict):
    associatedNormAttorneyAPI: str

    associatedNormJudgeAPI: str

    associatedNormPartiesAPI: str

    bestMatch: bool

    caseCountAnalyticsByNormLawFirmAPI: str

    caseCountAnalyticsByOpposingNormLawFirmAPI: str

    confidenceScore: typing.Union[int, float]

    normLawFirmAPI: str

    normLawFirmId: str

    normLawFirmName: str

    # Name of the object
    object: str

    scoreConstituents: PossibleNormLawFirmScoreConstituents

    sourceDetails: PossibleNormLawFirmSourceDetails

class OptionalPossibleNormLawFirm(TypedDict, total=False):
    pass

class PossibleNormLawFirm(RequiredPossibleNormLawFirm, OptionalPossibleNormLawFirm):
    pass
