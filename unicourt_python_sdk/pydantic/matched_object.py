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


class MatchedObject(BaseModel):
    highlight_snippet: str = Field(alias='highlightSnippet')

    matched_object_a_p_i: str = Field(alias='matchedObjectAPI')

    matched_object_attribute: str = Field(alias='matchedObjectAttribute')

    matched_object_id: str = Field(alias='matchedObjectId')

    matched_object_name: str = Field(alias='matchedObjectName')

    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
