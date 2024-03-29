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


class RequiredAttorneyLawFirm(TypedDict):
    # ID for the law firm of an attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.
    attorneyLawFirmId: typing.Optional[str]

    # Is the date when the document was first fetched from the court site.
    firstFetchDate: str

    # Signifies if the attorney as this attorney type is currently isVisible or not for the case.
    isVisible: bool

    # Is the date when the document was last fetched from the court site.
    lastFetchDate: str

    # Name of the law firm as provided by Court.
    name: str

    # Name of the object
    object: str

class OptionalAttorneyLawFirm(TypedDict, total=False):
    pass

class AttorneyLawFirm(RequiredAttorneyLawFirm, OptionalAttorneyLawFirm):
    pass
