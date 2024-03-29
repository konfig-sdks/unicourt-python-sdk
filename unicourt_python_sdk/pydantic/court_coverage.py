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

from unicourt_python_sdk.pydantic.case_class_coverage import CaseClassCoverage
from unicourt_python_sdk.pydantic.court import Court

class CourtCoverage(BaseModel):
    case_class_coverage_array: typing.List[CaseClassCoverage] = Field(alias='caseClassCoverageArray')

    court: Court = Field(alias='court')

    # Date when it was last updated.
    last_update_count_date: str = Field(alias='lastUpdateCountDate')

    # Name of the object
    object: str = Field(alias='object')

    # Total Cases for a specific court.
    total_case_count: int = Field(alias='totalCaseCount')

    # Count of total Case Documents added in UniCourt Library.
    total_case_document_in_library_count: int = Field(alias='totalCaseDocumentInLibraryCount')

    # Count of total Case Documents added in UniCourt Library in last 30 days
    total_case_document_in_library_in_last_thirty_days_count: int = Field(alias='totalCaseDocumentInLibraryInLastThirtyDaysCount')

    # Total Cases in last 30 days that were added to UniCourt
    total_cases_in_last_thirty_days_count: int = Field(alias='totalCasesInLastThirtyDaysCount')

    # Total Free Case Documents for a specific court.
    total_free_case_document_count: int = Field(alias='totalFreeCaseDocumentCount')

    # Total Free Case Documents in last 30 days that were added to UniCourt
    total_free_case_documents_in_last_thirty_days_count: int = Field(alias='totalFreeCaseDocumentsInLastThirtyDaysCount')

    # Total Paid Case Documents for a specific court.
    total_paid_case_document_count: int = Field(alias='totalPaidCaseDocumentCount')

    # Total Paid Case Documents in last 30 days that were added to UniCourt
    total_paid_case_documents_in_last_thirty_days_count: int = Field(alias='totalPaidCaseDocumentsInLastThirtyDaysCount')
    class Config:
        arbitrary_types_allowed = True
