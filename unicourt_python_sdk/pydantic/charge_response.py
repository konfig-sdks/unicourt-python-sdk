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

from unicourt_python_sdk.pydantic.charge import Charge

class ChargeResponse(BaseModel):
    charge_array: typing.List[Charge] = Field(alias='chargeArray')

    # Link to next page.
    next_page_a_p_i: typing.Optional[str] = Field(alias='nextPageAPI')

    object: str = Field(alias='object')

    # Page number for which results where obtained.
    page_number: int = Field(alias='pageNumber')

    # Link to previous page.
    previous_page_a_p_i: typing.Optional[str] = Field(alias='previousPageAPI')

    # Total number of matches found.
    total_count: int = Field(alias='totalCount')

    # Total number of pages to obtain all the objects.
    total_pages: int = Field(alias='totalPages')
    class Config:
        arbitrary_types_allowed = True
