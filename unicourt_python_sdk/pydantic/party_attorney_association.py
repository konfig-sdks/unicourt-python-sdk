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


class PartyAttorneyAssociation(BaseModel):
    # ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.
    attorney_id: str = Field(alias='attorneyId')

    # Signifies if this party attorney relationship is currently isVisible or not for the case.
    is_visible: bool = Field(alias='isVisible')

    # Name of the object
    object: str = Field(alias='object')

    # ID of the association
    party_attorney_association_id: str = Field(alias='partyAttorneyAssociationId')

    # ID for the party in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.
    party_id: str = Field(alias='partyId')
    class Config:
        arbitrary_types_allowed = True
