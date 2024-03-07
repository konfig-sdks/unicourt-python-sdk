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

from unicourt_python_sdk.pydantic.matched_object import MatchedObject

class NormPartySearchResult(BaseModel):
    first_fetch_date: datetime = Field(alias='firstFetchDate')

    last_fetch_date: datetime = Field(alias='lastFetchDate')

    matched_object_array: typing.List[MatchedObject] = Field(alias='matchedObjectArray')

    name: str = Field(alias='name')

    norm_party_details_a_p_i: str = Field(alias='normPartyDetailsAPI')

    norm_party_id: str = Field(alias='normPartyId')

    object: str = Field(alias='object')

    party_classification_type: str = Field(alias='partyClassificationType')
    class Config:
        arbitrary_types_allowed = True