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

from unicourt_python_sdk.pydantic.pacer_credential import PacerCredential

class PacerCredentialListResponse(BaseModel):
    # Link for the next page.
    next_page_a_p_i: typing.Optional[str] = Field(alias='nextPageAPI')

    # Name of the object.
    object: str = Field(alias='object')

    # Array of pacer credentials.
    pacer_credential_array: typing.List[PacerCredential] = Field(alias='pacerCredentialArray')

    # Current page number.
    page_number: int = Field(alias='pageNumber')

    # Link for the previous page.
    previous_page_a_p_i: typing.Optional[str] = Field(alias='previousPageAPI')

    # Total number of pacer credentials available.
    total_count: int = Field(alias='totalCount')

    # Total number of pages available.
    total_pages: int = Field(alias='totalPages')
    class Config:
        arbitrary_types_allowed = True