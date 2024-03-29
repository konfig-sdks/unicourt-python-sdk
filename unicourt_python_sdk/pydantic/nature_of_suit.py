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


class NatureOfSuit(BaseModel):
    # Nos Code from the source site which is extracted from the sourceText.
    code: int = Field(alias='code')

    # Code Name from the source site which is extracted from the sourceText.
    name: typing.Optional[str] = Field(alias='name')

    # Name of the object
    object: str = Field(alias='object')

    # Section of a nos code extracted from the sourceText.
    section: typing.Optional[str] = Field(alias='section')

    # Source nos code data from the court site.
    source_text: typing.Optional[str] = Field(alias='sourceText')
    class Config:
        arbitrary_types_allowed = True
