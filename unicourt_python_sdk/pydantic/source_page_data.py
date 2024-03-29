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

from unicourt_python_sdk.pydantic.source_structured_data import SourceStructuredData

class SourcePageData(BaseModel):
    additional_source_data: SourceStructuredData = Field(alias='additionalSourceData')

    # When was the page first fetched from the court site.
    first_fetch_date: str = Field(alias='firstFetchDate')

    # When was the page last fetched from the court site.
    last_fetch_date: str = Field(alias='lastFetchDate')

    # Name of the object
    object: str = Field(alias='object')

    # Pages supported for PACER pacerCaseQuery, pacerDocketReport, pacerCaseSummary, pacerAssociatedCases, pacerCaseLocatorResults, hearing, relatedCases.
    page_name: str = Field(alias='pageName')
    class Config:
        arbitrary_types_allowed = True
