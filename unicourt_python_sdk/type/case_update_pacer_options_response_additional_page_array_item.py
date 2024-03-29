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


class RequiredCaseUpdatePacerOptionsResponseAdditionalPageArrayItem(TypedDict):
    pass

class OptionalCaseUpdatePacerOptionsResponseAdditionalPageArrayItem(TypedDict, total=False):
    # You can limit how often this page information is fetched to reduce your PACER fees.  Min days is 0 and Max days is 100.  Example: 1.  Specifying a value of 0 ensures that this page is fetched from PACER for this case update irrespective of when the page was last fetched. 2.  Specifying a value of 30 ensures that this page is fetched from PACER for this case update only if the last fetch was older than 30 days. 
    fetchIfOlderThanDays: int

    page: str

class CaseUpdatePacerOptionsResponseAdditionalPageArrayItem(RequiredCaseUpdatePacerOptionsResponseAdditionalPageArrayItem, OptionalCaseUpdatePacerOptionsResponseAdditionalPageArrayItem):
    pass
