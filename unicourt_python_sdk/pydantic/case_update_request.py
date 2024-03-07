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

from unicourt_python_sdk.pydantic.case_update_pacer_options import CaseUpdatePacerOptions

class CaseUpdateRequest(BaseModel):
    # UniCourt's Case Id for update.
    case_id: str = Field(alias='caseId')

    pacer_options: typing.Optional[CaseUpdatePacerOptions] = Field(None, alias='pacerOptions')
    class Config:
        arbitrary_types_allowed = True