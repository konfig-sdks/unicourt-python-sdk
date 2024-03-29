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


class CaseCountAnalyticsByCaseFiledDate(BaseModel):
    case_count: int = Field(alias='caseCount')

    # Link to cases for this criteria.
    case_search_a_p_i: str = Field(alias='caseSearchAPI')

    grouped_by: Literal["Yearly", "Quarterly", "Monthly", "Weekly"] = Field(alias='groupedBy')

    month_int: typing.Optional[int] = Field(alias='monthInt')

    month_string: Literal["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", None] = Field(alias='monthString')

    object: str = Field(alias='object')

    quarter: Literal["Q1", "Q2", "Q3", "Q4", None] = Field(alias='quarter')

    week_of_month: typing.Optional[int] = Field(alias='weekOfMonth')

    week_of_year: typing.Optional[int] = Field(alias='weekOfYear')

    year: int = Field(alias='year')
    class Config:
        arbitrary_types_allowed = True
