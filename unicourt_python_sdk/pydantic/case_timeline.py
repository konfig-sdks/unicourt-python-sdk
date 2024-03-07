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


class CaseTimeline(BaseModel):
    # The first date when the two entities have appeared together in the case. (These dates are determined from case filed dates)
    first_case_filed_date: datetime = Field(alias='firstCaseFiledDate')

    # The last date when the two entities have appeared together in the case. (These dates are determined from case filed dates)
    last_case_filed_date: datetime = Field(alias='lastCaseFiledDate')

    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True