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

from unicourt_python_sdk.type.case_status import CaseStatus
from unicourt_python_sdk.type.case_type import CaseType
from unicourt_python_sdk.type.court import Court
from unicourt_python_sdk.type.court_location import CourtLocation
from unicourt_python_sdk.type.matched_object import MatchedObject

class RequiredCaseSearchResult(TypedDict):
    caseAPI: str

    caseId: str

    caseName: typing.Optional[str]

    caseNumber: str

    caseStatus: CaseStatus

    caseType: CaseType

    court: Court

    courtLocation: CourtLocation

    filedDate: datetime

    firstFetchDate: datetime

    lastFetchDate: datetime

    lastFetchDateWithUpdates: datetime

    matchedObjectArray: typing.List[MatchedObject]

    object: str

    participantsLastFetchDate: typing.Optional[datetime]

class OptionalCaseSearchResult(TypedDict, total=False):
    pass

class CaseSearchResult(RequiredCaseSearchResult, OptionalCaseSearchResult):
    pass
