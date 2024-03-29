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

from unicourt_python_sdk.type.case_count_analytics_by_court_type_geo import CaseCountAnalyticsByCourtTypeGeo
from unicourt_python_sdk.type.court_type import CourtType

class RequiredCaseCountAnalyticsByCourtType(TypedDict):
    Geo: CaseCountAnalyticsByCourtTypeGeo

    caseCount: int

    # link to cases for this criteria.
    caseSearchAPI: str

    courtType: CourtType

    object: str

class OptionalCaseCountAnalyticsByCourtType(TypedDict, total=False):
    pass

class CaseCountAnalyticsByCourtType(RequiredCaseCountAnalyticsByCourtType, OptionalCaseCountAnalyticsByCourtType):
    pass
