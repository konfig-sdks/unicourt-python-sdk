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

from unicourt_python_sdk.pydantic.case_analytics_api import CaseAnalyticsAPI
from unicourt_python_sdk.pydantic.norm_organization import NormOrganization
from unicourt_python_sdk.pydantic.norm_party_individual_data import NormPartyIndividualData
from unicourt_python_sdk.pydantic.party_analytics_api import PartyAnalyticsAPI
from unicourt_python_sdk.pydantic.related_norm_party import RelatedNormParty

class NormParty(BaseModel):
    case_analytics_a_p_i: CaseAnalyticsAPI = Field(alias='caseAnalyticsAPI')

    case_search_a_p_i: str = Field(alias='caseSearchAPI')

    individual_data: NormPartyIndividualData = Field(alias='individualData')

    name: str = Field(alias='name')

    norm_organization_data: NormOrganization = Field(alias='normOrganizationData')

    norm_party_id: str = Field(alias='normPartyId')

    object: str = Field(alias='object')

    party_analytics_a_p_i: PartyAnalyticsAPI = Field(alias='partyAnalyticsAPI')

    party_classification_type: Literal["Individual", "Organization"] = Field(alias='partyClassificationType')

    related_norm_party_array: typing.List[RelatedNormParty] = Field(alias='relatedNormPartyArray')
    class Config:
        arbitrary_types_allowed = True
