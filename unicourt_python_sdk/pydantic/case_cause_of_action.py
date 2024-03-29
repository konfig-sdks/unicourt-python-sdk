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

from unicourt_python_sdk.pydantic.cause_of_action import CauseOfAction
from unicourt_python_sdk.pydantic.cause_of_action_additional_data import CauseOfActionAdditionalData

class CaseCauseOfAction(BaseModel):
    cause_of_action: CauseOfAction = Field(alias='causeOfAction')

    cause_of_action_additional_data_array: typing.List[CauseOfActionAdditionalData] = Field(alias='causeOfActionAdditionalDataArray')

    # Name of the object
    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
