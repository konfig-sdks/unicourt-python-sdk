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


class RequiredSOSAssociatedNormOrganization(TypedDict):
    fromDate: datetime

    name: str

    normOrganizationAPI: typing.Optional[str]

    normOrganizationId: typing.Optional[str]

    object: str

    relationshipType: str

    toDate: typing.Optional[datetime]

class OptionalSOSAssociatedNormOrganization(TypedDict, total=False):
    pass

class SOSAssociatedNormOrganization(RequiredSOSAssociatedNormOrganization, OptionalSOSAssociatedNormOrganization):
    pass
