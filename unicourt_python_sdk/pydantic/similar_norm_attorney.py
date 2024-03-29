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

from unicourt_python_sdk.pydantic.bar_record_preview import BarRecordPreview

class SimilarNormAttorney(BaseModel):
    bar_record_preview_array: typing.List[BarRecordPreview] = Field(alias='barRecordPreviewArray')

    name: str = Field(alias='name')

    norm_attorney_a_p_i: str = Field(alias='normAttorneyAPI')

    norm_attorney_id: str = Field(alias='normAttorneyId')

    norm_attorney_similarity_score: typing.Union[int, float] = Field(alias='normAttorneySimilarityScore')

    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
