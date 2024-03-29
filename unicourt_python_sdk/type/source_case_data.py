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

from unicourt_python_sdk.type.nature_of_suit import NatureOfSuit
from unicourt_python_sdk.type.source_cause_of_action import SourceCauseOfAction
from unicourt_python_sdk.type.source_charge import SourceCharge
from unicourt_python_sdk.type.source_page_data import SourcePageData

class RequiredSourceCaseData(TypedDict):
    # Array of Charges for a case which is provided by the Court.
    natureOfSuitArray: typing.List[NatureOfSuit]

    # Name of the object
    object: str

    # Case Status as provided by Court.
    sourceCaseStatus: str

    # Case Type for a case which is provided by the Court.
    sourceCaseType: str

    # Array of Cause Of Action for a case which is provided by the Court.
    sourceCauseOfActionArray: typing.List[SourceCauseOfAction]

    # Array of Charges for a case which is provided by the Court.
    sourceChargeArray: typing.List[SourceCharge]

    # Courtrhouse as provided by Court.
    sourceCourt: str

    sourcePageData: typing.List[SourcePageData]

class OptionalSourceCaseData(TypedDict, total=False):
    pass

class SourceCaseData(RequiredSourceCaseData, OptionalSourceCaseData):
    pass
