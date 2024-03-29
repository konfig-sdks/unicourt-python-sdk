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

from unicourt_python_sdk.type.cause_of_action import CauseOfAction
from unicourt_python_sdk.type.cause_of_action_additional_data import CauseOfActionAdditionalData

class RequiredCaseCauseOfAction(TypedDict):
    causeOfAction: CauseOfAction

    causeOfActionAdditionalDataArray: typing.List[CauseOfActionAdditionalData]

    # Name of the object
    object: str

class OptionalCaseCauseOfAction(TypedDict, total=False):
    pass

class CaseCauseOfAction(RequiredCaseCauseOfAction, OptionalCaseCauseOfAction):
    pass
