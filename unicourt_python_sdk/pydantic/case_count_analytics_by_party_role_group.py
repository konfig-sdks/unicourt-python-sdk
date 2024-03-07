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

from unicourt_python_sdk.pydantic.party_role_group import PartyRoleGroup

class CaseCountAnalyticsByPartyRoleGroup(BaseModel):
    case_count: int = Field(alias='caseCount')

    # Link to cases for the entity involving the search criteria. TBD.
    case_search_a_p_i: str = Field(alias='caseSearchAPI')

    object: str = Field(alias='object')

    party_role_group: PartyRoleGroup = Field(alias='partyRoleGroup')
    class Config:
        arbitrary_types_allowed = True
