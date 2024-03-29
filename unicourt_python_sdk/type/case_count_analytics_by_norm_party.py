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


class RequiredCaseCountAnalyticsByNormParty(TypedDict):
    caseCount: int

    # Link to cases for this criteria.
    caseSearchAPI: str

    normPartyId: str

    normPartyName: str

    object: str

class OptionalCaseCountAnalyticsByNormParty(TypedDict, total=False):
    pass

class CaseCountAnalyticsByNormParty(RequiredCaseCountAnalyticsByNormParty, OptionalCaseCountAnalyticsByNormParty):
    pass
