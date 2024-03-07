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

from unicourt_python_sdk.type.pacer_case_search_results import PACERCaseSearchResults
from unicourt_python_sdk.type.pacer_search_page_info import PACERSearchPageInfo
from unicourt_python_sdk.type.pacer_search_receipt import PACERSearchReceipt

class RequiredPCLCase(TypedDict):
    # Link to next page of the PCL Search Results.
    nextPageAPI: typing.Optional[str]

    # Name of the object
    object: str

    pacerPageInfo: PACERSearchPageInfo

    pacerReceipt: PACERSearchReceipt

    pacerSearchResultsArray: typing.List[PACERCaseSearchResults]

    # Page number for which results where obtained.
    pageNumber: int

    # Total number of records available for this Search.
    totalCount: int

    # Total number of pages to obtain all the objects the current PCL Search.
    totalPages: int

class OptionalPCLCase(TypedDict, total=False):
    pass

class PCLCase(RequiredPCLCase, OptionalPCLCase):
    pass