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

from unicourt_python_sdk.pydantic.possible_norm_party_score_constituents import PossibleNormPartyScoreConstituents

class PossibleNormParty(BaseModel):
    associated_norm_attorneys_a_p_i: str = Field(alias='associatedNormAttorneysAPI')

    associated_norm_judges_a_p_i: str = Field(alias='associatedNormJudgesAPI')

    associated_norm_law_firms_a_p_i: str = Field(alias='associatedNormLawFirmsAPI')

    best_match: bool = Field(alias='bestMatch')

    case_count_analytics_by_norm_party_a_p_i: str = Field(alias='caseCountAnalyticsByNormPartyAPI')

    case_count_analytics_by_opposing_norm_party_a_p_i: str = Field(alias='caseCountAnalyticsByOpposingNormPartyAPI')

    confidence_score: typing.Union[int, float] = Field(alias='confidenceScore')

    # Link to Details For the Party.
    norm_party_a_p_i: str = Field(alias='normPartyAPI')

    norm_party_id: str = Field(alias='normPartyId')

    norm_party_name: str = Field(alias='normPartyName')

    # Name of the object
    object: str = Field(alias='object')

    score_constituents: PossibleNormPartyScoreConstituents = Field(alias='scoreConstituents')
    class Config:
        arbitrary_types_allowed = True
