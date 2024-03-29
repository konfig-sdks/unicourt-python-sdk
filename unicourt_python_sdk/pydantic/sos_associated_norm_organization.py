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


class SOSAssociatedNormOrganization(BaseModel):
    from_date: datetime = Field(alias='fromDate')

    name: str = Field(alias='name')

    norm_organization_a_p_i: typing.Optional[str] = Field(alias='normOrganizationAPI')

    norm_organization_id: typing.Optional[str] = Field(alias='normOrganizationId')

    object: str = Field(alias='object')

    relationship_type: Literal["Parent", "Child"] = Field(alias='relationshipType')

    to_date: typing.Optional[datetime] = Field(alias='toDate')
    class Config:
        arbitrary_types_allowed = True
