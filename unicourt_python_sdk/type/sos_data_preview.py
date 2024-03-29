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


class RequiredSOSDataPreview(TypedDict):
    object: str

    sosNumber: str

    stateCode: str

class OptionalSOSDataPreview(TypedDict, total=False):
    pass

class SOSDataPreview(RequiredSOSDataPreview, OptionalSOSDataPreview):
    pass
