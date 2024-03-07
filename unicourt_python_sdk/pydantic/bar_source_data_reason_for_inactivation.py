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


class BarSourceDataReasonForInactivation(BaseModel):
    case_number: typing.Optional[str] = Field(alias='caseNumber')

    link: typing.Optional[str] = Field(alias='link')
    class Config:
        arbitrary_types_allowed = True