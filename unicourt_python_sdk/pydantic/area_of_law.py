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


class AreaOfLaw(BaseModel):
    area_of_law_id: str = Field(alias='areaOfLawId')

    case_class: str = Field(alias='caseClass')

    case_class_id: str = Field(alias='caseClassId')

    # The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    created_date: datetime = Field(alias='createdDate')

    name: str = Field(alias='name')

    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True