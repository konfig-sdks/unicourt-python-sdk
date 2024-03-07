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
from pydantic import BaseModel, Field, RootModel


class CaseCountAnalyticsByNormJudge(BaseModel):
    case_count: int = Field(alias='caseCount')

    # Link to cases for this criteria.
    case_search_a_p_i: str = Field(alias='caseSearchAPI')

    norm_judge_id: str = Field(alias='normJudgeId')

    norm_judge_name: str = Field(alias='normJudgeName')

    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
