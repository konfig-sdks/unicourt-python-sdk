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

from unicourt_python_sdk.pydantic.pacer_import_case_results import PACERImportCaseResults

class PACERImportCase(BaseModel):
    # Court Fee charged for the Find Case request. This is only applicable for Appeal Cases.
    court_fee: typing.Optional[typing.Union[int, float]] = Field(alias='courtFee')

    # Name of the object
    object: str = Field(alias='object')

    pacer_import_case_results_array: typing.List[PACERImportCaseResults] = Field(alias='pacerImportCaseResultsArray')
    class Config:
        arbitrary_types_allowed = True
