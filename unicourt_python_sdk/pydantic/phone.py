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


class Phone(BaseModel):
    # Date at which this record is created in UniCourt.
    first_fetch_date: datetime = Field(alias='firstFetchDate')

    # Boolean indicating if the phone is visible or not.
    is_visible: bool = Field(alias='isVisible')

    # Date at which this record was updated in UniCourt.
    last_fetch_date: datetime = Field(alias='lastFetchDate')

    object: str = Field(alias='object')

    # Phone Number
    phone_number: str = Field(alias='phoneNumber')

    # Resolved phone type (ideally from master data).
    phone_type: Literal["DEFAULT", "OFFICE", "FAX", "PHONE"] = Field(alias='phoneType')
    class Config:
        arbitrary_types_allowed = True
