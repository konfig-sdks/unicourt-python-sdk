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

from unicourt_python_sdk.pydantic.associated_so_s_person import AssociatedSoSPerson
from unicourt_python_sdk.pydantic.contact import Contact
from unicourt_python_sdk.pydantic.sos_associated_norm_organization import SOSAssociatedNormOrganization
from unicourt_python_sdk.pydantic.sos_name_change import SOSNameChange

class SOSData(BaseModel):
    associated_so_s_person_array: typing.List[AssociatedSoSPerson] = Field(alias='associatedSoSPersonArray')

    contact: Contact = Field(alias='contact')

    domestic_registration: bool = Field(alias='domesticRegistration')

    fein: typing.Optional[str] = Field(alias='fein')

    first_fetch_date: datetime = Field(alias='firstFetchDate')

    inactivation_date: typing.Optional[datetime] = Field(alias='inactivationDate')

    is_active: bool = Field(alias='isActive')

    last_fetch_date: datetime = Field(alias='lastFetchDate')

    # Last Fetch Date of Organization with Updates.
    last_fetch_date_with_updates: datetime = Field(alias='lastFetchDateWithUpdates')

    name_changes_array: typing.List[SOSNameChange] = Field(alias='nameChangesArray')

    object: str = Field(alias='object')

    registered_date: typing.Optional[datetime] = Field(alias='registeredDate')

    sos_associated_norm_organization_array: typing.List[SOSAssociatedNormOrganization] = Field(alias='sosAssociatedNormOrganizationArray')

    sos_number: typing.Optional[str] = Field(alias='sosNumber')

    state_code: str = Field(alias='stateCode')

    status: Literal["Active"] = Field(alias='status')
    class Config:
        arbitrary_types_allowed = True
