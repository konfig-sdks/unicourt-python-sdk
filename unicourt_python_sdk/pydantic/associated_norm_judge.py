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

from unicourt_python_sdk.pydantic.case_timeline import CaseTimeline

class AssociatedNormJudge(BaseModel):
    version: str = Field(alias='version')

    case_count: int = Field(alias='caseCount')

    # Link to related cases for this association.
    case_search_a_p_i: str = Field(alias='caseSearchAPI')

    case_timeline: CaseTimeline = Field(alias='caseTimeline')

    first_name: str = Field(alias='firstName')

    last_name: str = Field(alias='lastName')

    middle_name: typing.Optional[str] = Field(alias='middleName')

    name: str = Field(alias='name')

    # Link to Details from the Judge.
    norm_judge_a_p_i: str = Field(alias='normJudgeAPI')

    norm_judge_id: str = Field(alias='normJudgeId')

    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
