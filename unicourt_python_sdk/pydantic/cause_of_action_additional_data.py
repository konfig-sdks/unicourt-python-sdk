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


class CauseOfActionAdditionalData(BaseModel):
    cause_of_action_additional_data_id: str = Field(alias='causeOfActionAdditionalDataId')

    # The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    created_date: datetime = Field(alias='createdDate')

    object: str = Field(alias='object')

    type: str = Field(alias='type')

    value: str = Field(alias='value')
    class Config:
        arbitrary_types_allowed = True
