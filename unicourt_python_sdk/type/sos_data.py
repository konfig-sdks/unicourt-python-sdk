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

from unicourt_python_sdk.type.associated_so_s_person import AssociatedSoSPerson
from unicourt_python_sdk.type.contact import Contact
from unicourt_python_sdk.type.sos_associated_norm_organization import SOSAssociatedNormOrganization
from unicourt_python_sdk.type.sos_name_change import SOSNameChange

class RequiredSOSData(TypedDict):
    associatedSoSPersonArray: typing.List[AssociatedSoSPerson]

    contact: Contact

    domesticRegistration: bool

    fein: typing.Optional[str]

    firstFetchDate: datetime

    inactivationDate: typing.Optional[datetime]

    isActive: bool

    lastFetchDate: datetime

    # Last Fetch Date of Organization with Updates.
    lastFetchDateWithUpdates: datetime

    nameChangesArray: typing.List[SOSNameChange]

    object: str

    registeredDate: typing.Optional[datetime]

    sosAssociatedNormOrganizationArray: typing.List[SOSAssociatedNormOrganization]

    sosNumber: typing.Optional[str]

    stateCode: str

    status: typing.Optional[str]

class OptionalSOSData(TypedDict, total=False):
    pass

class SOSData(RequiredSOSData, OptionalSOSData):
    pass
