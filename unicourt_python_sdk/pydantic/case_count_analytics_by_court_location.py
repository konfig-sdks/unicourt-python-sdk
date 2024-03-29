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

from unicourt_python_sdk.pydantic.case_count_analytics_by_court_location_geo import CaseCountAnalyticsByCourtLocationGeo
from unicourt_python_sdk.pydantic.court import Court
from unicourt_python_sdk.pydantic.court_location import CourtLocation

class CaseCountAnalyticsByCourtLocation(BaseModel):
    geo: CaseCountAnalyticsByCourtLocationGeo = Field(alias='Geo')

    case_count: int = Field(alias='caseCount')

    # link to cases for this criteria.
    case_search_a_p_i: str = Field(alias='caseSearchAPI')

    court: Court = Field(alias='court')

    court_location: CourtLocation = Field(alias='courtLocation')

    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
