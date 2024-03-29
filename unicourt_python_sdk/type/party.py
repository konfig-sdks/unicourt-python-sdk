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

from unicourt_python_sdk.type.attorney_representation_type import AttorneyRepresentationType
from unicourt_python_sdk.type.contact import Contact
from unicourt_python_sdk.type.party_attorney_associations import PartyAttorneyAssociations
from unicourt_python_sdk.type.party_role import PartyRole
from unicourt_python_sdk.type.possible_norm_party import PossibleNormParty

class RequiredParty(TypedDict):
    attorneyRepresentationType: AttorneyRepresentationType

    contact: Contact

    # When was the party first fetched from the court site.
    firstFetchDate: datetime

    # First name of the party. This is normalized by UniCourt.
    firstName: typing.Optional[str]

    # Signifies if the party as this party type is currently isVisible or not for the case.
    isVisible: bool

    # When was the party last fetched from the court site.
    lastFetchDate: datetime

    # Last name of the party. This is normalized by UniCourt.
    lastName: typing.Optional[str]

    # Middle name of the party. This is normalized by UniCourt.
    middleName: typing.Optional[str]

    # Name of the party as provided by Court.
    name: str

    namePrefix: typing.Optional[str]

    nameSuffix: typing.Optional[str]

    # Name of the object
    object: str

    partyAttorneyAssociations: PartyAttorneyAssociations

    # To know the type of an entity in a case, if it is an Individual, Company or Other. An entity to a case could be the parties, attorneys or judges involved.
    partyClassificationType: str

    # ID for the party in this case. This ID is unique within a case and NOT across cases. If the same party were to appear in another case this ID would be different.
    partyId: str

    partyRole: PartyRole

    possibleNormPartyArray: typing.List[PossibleNormParty]

    # Party Type as provided by Court.
    sourcePartyRole: str

class OptionalParty(TypedDict, total=False):
    pass

class Party(RequiredParty, OptionalParty):
    pass
