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

from unicourt_python_sdk.type.pacer_import_case_results import PACERImportCaseResults

class RequiredPACERImportCase(TypedDict):
    # Court Fee charged for the Find Case request. This is only applicable for Appeal Cases.
    courtFee: typing.Optional[typing.Union[int, float]]

    # Name of the object
    object: str

    pacerImportCaseResultsArray: typing.List[PACERImportCaseResults]

class OptionalPACERImportCase(TypedDict, total=False):
    pass

class PACERImportCase(RequiredPACERImportCase, OptionalPACERImportCase):
    pass
