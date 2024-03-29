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

from unicourt_python_sdk.type.access_token_id_response import AccessTokenIdResponse

class RequiredAccessTokenIdListResponse(TypedDict):
    # Array of access tokens Id.
    AccessTokenIdArray: typing.List[AccessTokenIdResponse]

    # Name of the object.
    object: str

class OptionalAccessTokenIdListResponse(TypedDict, total=False):
    pass

class AccessTokenIdListResponse(RequiredAccessTokenIdListResponse, OptionalAccessTokenIdListResponse):
    pass
