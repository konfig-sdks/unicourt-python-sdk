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


class RequiredPartyRoleGroup(TypedDict):
    description: typing.Optional[str]

    # The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    createdDate: datetime

    name: str

    object: str

    partyRoleGroupId: str

class OptionalPartyRoleGroup(TypedDict, total=False):
    pass

class PartyRoleGroup(RequiredPartyRoleGroup, OptionalPartyRoleGroup):
    pass