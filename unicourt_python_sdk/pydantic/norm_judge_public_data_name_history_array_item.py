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


class NormJudgePublicDataNameHistoryArrayItem(BaseModel):
    first_name: typing.Optional[str] = Field(alias='firstName')

    is_visible: bool = Field(alias='isVisible')

    last_name: typing.Optional[str] = Field(alias='lastName')

    middle_name: typing.Optional[str] = Field(alias='middleName')

    prefix: typing.Optional[str] = Field(alias='prefix')

    suffix: typing.Optional[str] = Field(alias='suffix')
    class Config:
        arbitrary_types_allowed = True
