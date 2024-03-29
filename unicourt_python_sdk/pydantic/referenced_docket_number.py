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


class ReferencedDocketNumber(BaseModel):
    # Link to Docket Entries API with the current docket number. The response of this API will give all the primary documents and secondary documents that are associated to it.
    docket_entries_a_p_i: typing.Optional[str] = Field(alias='docketEntriesAPI')

    # Each referenced docket number
    docket_number: int = Field(alias='docketNumber')

    # Name of the object
    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
