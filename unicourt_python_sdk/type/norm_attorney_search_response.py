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

from unicourt_python_sdk.type.norm_attorney_search_result import NormAttorneySearchResult

class RequiredNormAttorneySearchResponse(TypedDict):
    # Link to next page.
    nextPageAPI: typing.Optional[str]

    # Query been sent by client
    normAttorneySearchId: str

    normAttorneySearchResultArray: typing.List[NormAttorneySearchResult]

    object: str

    pageNumber: int

    # Link to previous page.
    previousPageAPI: typing.Optional[str]

    # Query been sent by client
    q: str

    # The number of matches that were found in the index.
    totalCount: int

    # Total pages for matches that were found in the index.
    totalPages: int

class OptionalNormAttorneySearchResponse(TypedDict, total=False):
    pass

class NormAttorneySearchResponse(RequiredNormAttorneySearchResponse, OptionalNormAttorneySearchResponse):
    pass