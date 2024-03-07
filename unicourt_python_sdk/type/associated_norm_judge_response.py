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

from unicourt_python_sdk.type.associated_norm_judge import AssociatedNormJudge

class RequiredAssociatedNormJudgeResponse(TypedDict):
    associatedNormJudgeArray: typing.List[AssociatedNormJudge]

    # Next page of results if applicable.
    nextPageAPI: typing.Optional[str]

    # Previous page of results if applicable.
    previousPageAPI: typing.Optional[str]

    # Total no. of results for this criteria.
    totalCount: int

    # Total no. of pages.
    totalPages: int

class OptionalAssociatedNormJudgeResponse(TypedDict, total=False):
    pass

class AssociatedNormJudgeResponse(RequiredAssociatedNormJudgeResponse, OptionalAssociatedNormJudgeResponse):
    pass