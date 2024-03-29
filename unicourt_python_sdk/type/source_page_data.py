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

from unicourt_python_sdk.type.source_structured_data import SourceStructuredData

class RequiredSourcePageData(TypedDict):
    additionalSourceData: SourceStructuredData

    # When was the page first fetched from the court site.
    firstFetchDate: str

    # When was the page last fetched from the court site.
    lastFetchDate: str

    # Name of the object
    object: str

    # Pages supported for PACER pacerCaseQuery, pacerDocketReport, pacerCaseSummary, pacerAssociatedCases, pacerCaseLocatorResults, hearing, relatedCases.
    pageName: str

class OptionalSourcePageData(TypedDict, total=False):
    pass

class SourcePageData(RequiredSourcePageData, OptionalSourcePageData):
    pass
