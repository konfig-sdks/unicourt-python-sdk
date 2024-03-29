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

from unicourt_python_sdk.type.attorney_law_firm import AttorneyLawFirm
from unicourt_python_sdk.type.attorney_party_role_group_id_array import AttorneyPartyRoleGroupIdArray
from unicourt_python_sdk.type.attorney_party_role_id_array import AttorneyPartyRoleIdArray
from unicourt_python_sdk.type.attorney_type import AttorneyType
from unicourt_python_sdk.type.contact import Contact
from unicourt_python_sdk.type.party_attorney_associations import PartyAttorneyAssociations
from unicourt_python_sdk.type.possible_norm_attorney import PossibleNormAttorney
from unicourt_python_sdk.type.possible_norm_law_firm import PossibleNormLawFirm

class RequiredAttorney(TypedDict):
    # ID for the attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.
    attorneyId: str

    attorneyLawFirmArray: typing.List[AttorneyLawFirm]

    attorneyType: AttorneyType

    # The bar enrollment number of an attorney.
    barNumber: typing.Optional[str]

    contact: Contact

    # When was the attorney first fetched from the court site.
    firstFetchDate: datetime

    # First name of the attorney. This is normalized by UniCourt.
    firstName: typing.Optional[str]

    # Signifies if the attorney as this attorney type is currently isVisible or not for the case.
    isVisible: bool

    # When was the attorney last fetched from the court site.
    lastFetchDate: datetime

    # Last name of the attorney. This is normalized by UniCourt.
    lastName: typing.Optional[str]

    # Middle name of the attorney. This is normalized by UniCourt.
    middleName: typing.Optional[str]

    # Name of the attorney as provided by Court.
    name: str

    namePrefix: typing.Optional[str]

    nameSuffix: typing.Optional[str]

    # Name of the object
    object: str

    partyAttorneyAssociations: PartyAttorneyAssociations

    partyRoleGroupIdArray: AttorneyPartyRoleGroupIdArray

    partyRoleIdArray: AttorneyPartyRoleIdArray

    possibleNormAttorneyArray: typing.List[PossibleNormAttorney]

    # Possible Norm Lawfirm array for a Attorney.
    possibleNormLawFirmArray: typing.List[PossibleNormLawFirm]

    # Attorney Type as provided by Court.
    sourceAttorneyType: str

class OptionalAttorney(TypedDict, total=False):
    pass

class Attorney(RequiredAttorney, OptionalAttorney):
    pass
