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


class AttorneyAnalyticsAPI(BaseModel):
    associated_norm_judges_a_p_i: str = Field(alias='associatedNormJudgesAPI')

    associated_norm_law_firms_a_p_i: str = Field(alias='associatedNormLawFirmsAPI')

    associated_norm_parties_a_p_i: str = Field(alias='associatedNormPartiesAPI')

    case_count_analytics_by_opposing_norm_attorney_a_p_i: str = Field(alias='caseCountAnalyticsByOpposingNormAttorneyAPI')

    case_count_analytics_by_opposing_norm_law_firm_a_p_i: typing.Optional[str] = Field(alias='caseCountAnalyticsByOpposingNormLawFirmAPI')

    case_count_analytics_by_opposing_norm_party_a_p_i: typing.Optional[str] = Field(alias='caseCountAnalyticsByOpposingNormPartyAPI')

    # Link to Details for the Attorney.
    norm_attorney_a_p_i: str = Field(alias='normAttorneyAPI')

    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
