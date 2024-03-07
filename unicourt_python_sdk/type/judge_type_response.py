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

from unicourt_python_sdk.type.judge_type import JudgeType

class RequiredJudgeTypeResponse(TypedDict):
    judgeTypeArray: typing.List[JudgeType]

    # Link to next page.
    nextPageAPI: typing.Optional[str]

    object: str

    # Page number for which results where obtained.
    pageNumber: int

    # Link to previous page.
    previousPageAPI: typing.Optional[str]

    # Total number of matches found.
    totalCount: int

    # Total number of pages to obtain all the objects.
    totalPages: int

class OptionalJudgeTypeResponse(TypedDict, total=False):
    pass

class JudgeTypeResponse(RequiredJudgeTypeResponse, OptionalJudgeTypeResponse):
    pass
