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

from unicourt_python_sdk.type.case_count_analytics_by_case_type_group import CaseCountAnalyticsByCaseTypeGroup

class RequiredCaseCountAnalyticsByCaseTypeGroupResponse(TypedDict):
    # Next page of results if applicable.
    nextPageAPI: typing.Optional[str]

    object: str

    # Link to previous page of results.
    previousPageAPI: typing.Optional[str]

    results: typing.List[CaseCountAnalyticsByCaseTypeGroup]

    # Total no. of Cases for this criteria.
    totalCaseCount: int

    # Total no. of Case Type Group for this criteria.
    totalCaseTypeGroupCount: int

    # Total no. of pages.
    totalPages: int

class OptionalCaseCountAnalyticsByCaseTypeGroupResponse(TypedDict, total=False):
    pass

class CaseCountAnalyticsByCaseTypeGroupResponse(RequiredCaseCountAnalyticsByCaseTypeGroupResponse, OptionalCaseCountAnalyticsByCaseTypeGroupResponse):
    pass
