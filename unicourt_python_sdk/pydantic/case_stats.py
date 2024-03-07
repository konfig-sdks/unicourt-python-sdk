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


class CaseStats(BaseModel):
    # Count which includes the freeCaseDocumentCount and paidCaseDocumentCount.
    all_case_document_count: int = Field(alias='allCaseDocumentCount')

    # Count of number of attornies available in the case being requested for.
    attorney_count: int = Field(alias='attorneyCount')

    # Count of number of documents that are available in the UniCourt CrowdSourced Library for the case being requested for.
    case_document_in_library_count: int = Field(alias='caseDocumentInLibraryCount')

    # Count of number of docket entries available in the case being requested for.
    docket_entry_count: int = Field(alias='docketEntryCount')

    # Count of number of free documents available in the case being requested for.
    free_case_document_count: int = Field(alias='freeCaseDocumentCount')

    # Count of number of hearings available in the case being requested for.
    hearing_count: int = Field(alias='hearingCount')

    # Count of number of judges available in the case being requested for.
    judge_count: int = Field(alias='judgeCount')

    # Name of the object
    object: str = Field(alias='object')

    # Count of number of paid documents available in the case being requested for.
    paid_case_document_count: int = Field(alias='paidCaseDocumentCount')

    # Count of number of parties available in the case being requested for.
    party_count: int = Field(alias='partyCount')

    # Count of related cases that are available in the case being requested.
    related_case_count: int = Field(alias='relatedCaseCount')
    class Config:
        arbitrary_types_allowed = True