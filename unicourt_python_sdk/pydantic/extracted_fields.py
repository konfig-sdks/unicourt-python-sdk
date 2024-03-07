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


class ExtractedFields(BaseModel):
    # This can be an field that is extracted from rawOrderedDataArray on request of different users.
    key: typing.Optional[typing.Optional[str]] = Field(None, alias='key')
    class Config:
        arbitrary_types_allowed = True
