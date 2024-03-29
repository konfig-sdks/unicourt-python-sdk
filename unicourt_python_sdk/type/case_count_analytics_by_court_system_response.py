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

from unicourt_python_sdk.type.case_count_analytics_by_court_system import CaseCountAnalyticsByCourtSystem

class RequiredCaseCountAnalyticsByCourtSystemResponse(TypedDict):
    # Next page of results if applicable.
    nextPageAPI: typing.Optional[str]

    object: str

    # Link to previous page of results.
    previousPageAPI: typing.Optional[str]

    results: typing.List[CaseCountAnalyticsByCourtSystem]

    # Total no. of Cases for this criteria.
    totalCaseCount: int

    # Total no. of Court System for this criteria.
    totalCourtSystemCount: int

    # Total no. of pages.
    totalPages: int

class OptionalCaseCountAnalyticsByCourtSystemResponse(TypedDict, total=False):
    pass

class CaseCountAnalyticsByCourtSystemResponse(RequiredCaseCountAnalyticsByCourtSystemResponse, OptionalCaseCountAnalyticsByCourtSystemResponse):
    pass
