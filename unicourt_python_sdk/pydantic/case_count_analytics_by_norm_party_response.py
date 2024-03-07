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

from unicourt_python_sdk.pydantic.case_count_analytics_by_norm_party import CaseCountAnalyticsByNormParty

class CaseCountAnalyticsByNormPartyResponse(BaseModel):
    # Next page of results if applicable.
    next_page_a_p_i: typing.Optional[str] = Field(alias='nextPageAPI')

    object: str = Field(alias='object')

    # Link to previous page of results.
    previous_page_a_p_i: typing.Optional[str] = Field(alias='previousPageAPI')

    results: typing.List[CaseCountAnalyticsByNormParty] = Field(alias='results')

    # Total no. of Cases for this criteria.
    total_case_count: int = Field(alias='totalCaseCount')

    # Total no. of NormParty for this criteria.
    total_norm_party_count: int = Field(alias='totalNormPartyCount')

    # Total no. of pages.
    total_pages: int = Field(alias='totalPages')
    class Config:
        arbitrary_types_allowed = True
