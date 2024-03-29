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

from unicourt_python_sdk.pydantic.case_status import CaseStatus
from unicourt_python_sdk.pydantic.case_type import CaseType
from unicourt_python_sdk.pydantic.court import Court
from unicourt_python_sdk.pydantic.court_location import CourtLocation
from unicourt_python_sdk.pydantic.matched_object import MatchedObject

class CaseSearchResult(BaseModel):
    case_a_p_i: str = Field(alias='caseAPI')

    case_id: str = Field(alias='caseId')

    case_name: typing.Optional[str] = Field(alias='caseName')

    case_number: str = Field(alias='caseNumber')

    case_status: CaseStatus = Field(alias='caseStatus')

    case_type: CaseType = Field(alias='caseType')

    court: Court = Field(alias='court')

    court_location: CourtLocation = Field(alias='courtLocation')

    filed_date: datetime = Field(alias='filedDate')

    first_fetch_date: datetime = Field(alias='firstFetchDate')

    last_fetch_date: datetime = Field(alias='lastFetchDate')

    last_fetch_date_with_updates: datetime = Field(alias='lastFetchDateWithUpdates')

    matched_object_array: typing.List[MatchedObject] = Field(alias='matchedObjectArray')

    object: str = Field(alias='object')

    participants_last_fetch_date: typing.Optional[datetime] = Field(alias='participantsLastFetchDate')
    class Config:
        arbitrary_types_allowed = True
