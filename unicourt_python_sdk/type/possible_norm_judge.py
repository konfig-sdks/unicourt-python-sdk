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

from unicourt_python_sdk.type.possible_norm_judge_score_constituents import PossibleNormJudgeScoreConstituents

class RequiredPossibleNormJudge(TypedDict):
    associatedNormAttorneysAPI: str

    associatedNormLawFirmsAPI: str

    associatedNormPartiesAPI: str

    bestMatch: bool

    caseCountAnalyticsByNormJudgeAPI: str

    confidenceScore: typing.Optional[typing.Union[int, float]]

    # Link to Details For the Judge.
    normJudgeAPI: str

    normJudgeId: str

    normJudgeName: str

    # Name of the object
    object: str

    scoreConstituents: PossibleNormJudgeScoreConstituents

class OptionalPossibleNormJudge(TypedDict, total=False):
    pass

class PossibleNormJudge(RequiredPossibleNormJudge, OptionalPossibleNormJudge):
    pass
