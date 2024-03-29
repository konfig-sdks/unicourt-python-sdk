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


class BarSourceDataPublicHearingArrayItem(BaseModel):
    conduct: typing.Optional[str] = Field(alias='conduct')

    date: typing.Optional[datetime] = Field(alias='date')

    issued_by: typing.Optional[str] = Field(alias='issuedBy')

    order: typing.Optional[str] = Field(alias='order')

    respondent: typing.Optional[str] = Field(alias='respondent')
    class Config:
        arbitrary_types_allowed = True
