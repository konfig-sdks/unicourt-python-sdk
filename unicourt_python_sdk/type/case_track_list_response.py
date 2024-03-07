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

from unicourt_python_sdk.type.case_track_preview import CaseTrackPreview

class RequiredCaseTrackListResponse(TypedDict):
    # Array of cases tracked.
    caseTrackPreviewArray: typing.List[CaseTrackPreview]

    # Link for the next page.
    nextPageAPI: typing.Optional[str]

    # Name of the object.
    object: str

    # Current page number.
    pageNumber: int

    # Link for the previous page.
    previousPageAPI: typing.Optional[str]

    # Total number of case track available.
    totalCount: int

    # Total number of pages available.
    totalPages: int

class OptionalCaseTrackListResponse(TypedDict, total=False):
    pass

class CaseTrackListResponse(RequiredCaseTrackListResponse, OptionalCaseTrackListResponse):
    pass
