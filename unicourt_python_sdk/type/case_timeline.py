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


class RequiredCaseTimeline(TypedDict):
    # The first date when the two entities have appeared together in the case. (These dates are determined from case filed dates)
    firstCaseFiledDate: datetime

    # The last date when the two entities have appeared together in the case. (These dates are determined from case filed dates)
    lastCaseFiledDate: datetime

    object: str

class OptionalCaseTimeline(TypedDict, total=False):
    pass

class CaseTimeline(RequiredCaseTimeline, OptionalCaseTimeline):
    pass
