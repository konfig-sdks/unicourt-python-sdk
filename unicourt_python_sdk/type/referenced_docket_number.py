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


class RequiredReferencedDocketNumber(TypedDict):
    # Link to Docket Entries API with the current docket number. The response of this API will give all the primary documents and secondary documents that are associated to it.
    docketEntriesAPI: typing.Optional[str]

    # Each referenced docket number
    docketNumber: int

    # Name of the object
    object: str

class OptionalReferencedDocketNumber(TypedDict, total=False):
    pass

class ReferencedDocketNumber(RequiredReferencedDocketNumber, OptionalReferencedDocketNumber):
    pass
