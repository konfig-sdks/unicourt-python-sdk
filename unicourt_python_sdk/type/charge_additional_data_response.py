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

from unicourt_python_sdk.type.charge_additional_data import ChargeAdditionalData

class RequiredChargeAdditionalDataResponse(TypedDict):
    chargeAdditionalDataArray: typing.List[ChargeAdditionalData]

    # Link to next page.
    nextPageAPI: typing.Optional[str]

    object: str

    # Page number for which results where obtained.
    pageNumber: int

    # Link to previous page.
    previousPageAPI: typing.Optional[str]

    # Total number of matches found.
    totalCount: int

    # Total number of pages to obtain all the objects.
    totalPages: int

class OptionalChargeAdditionalDataResponse(TypedDict, total=False):
    pass

class ChargeAdditionalDataResponse(RequiredChargeAdditionalDataResponse, OptionalChargeAdditionalDataResponse):
    pass
