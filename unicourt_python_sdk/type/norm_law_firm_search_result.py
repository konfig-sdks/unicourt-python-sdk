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

from unicourt_python_sdk.type.matched_object import MatchedObject

class RequiredNormLawFirmSearchResult(TypedDict):
    firstFetchDate: datetime

    lastFetchDate: datetime

    matchedObjectArray: typing.List[MatchedObject]

    name: str

    normLawFirmDetailsAPI: str

    normLawFirmId: str

    object: str

class OptionalNormLawFirmSearchResult(TypedDict, total=False):
    pass

class NormLawFirmSearchResult(RequiredNormLawFirmSearchResult, OptionalNormLawFirmSearchResult):
    pass
