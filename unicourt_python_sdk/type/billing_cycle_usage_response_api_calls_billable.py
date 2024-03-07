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


class RequiredBillingCycleUsageResponseApiCallsBillable(TypedDict):
    # Total API calls billed  for the billing cycle
    count: int

    # Last Updated date and time for the field apiCallsBillable
    lastUpdated: typing.Optional[datetime]

class OptionalBillingCycleUsageResponseApiCallsBillable(TypedDict, total=False):
    pass

class BillingCycleUsageResponseApiCallsBillable(RequiredBillingCycleUsageResponseApiCallsBillable, OptionalBillingCycleUsageResponseApiCallsBillable):
    pass