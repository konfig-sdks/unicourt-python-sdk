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

from unicourt_python_sdk.type.contact import Contact
from unicourt_python_sdk.type.judge_type import JudgeType
from unicourt_python_sdk.type.possible_norm_judge import PossibleNormJudge

class RequiredJudge(TypedDict):
    contact: Contact

    # When was the judge first fetched from the court site.
    firstFetchDate: datetime

    # First name of the judge. This is normalized by UniCourt.
    firstName: typing.Optional[str]

    # Signifies if the judge as this judge type is currently isVisible or not for the case.
    isVisible: bool

    # ID for the judge in this case. This ID is unique within a case and NOT across cases. If the same Judge were to appear in another case this ID would be different.
    judgeId: str

    judgeType: JudgeType

    # When was the judge last fetched from the court site.
    lastFetchDate: datetime

    # Last name of the judge. This is normalized by UniCourt.
    lastName: typing.Optional[str]

    # Middle name of the judge. This is normalized by UniCourt.
    middleName: typing.Optional[str]

    # Name of the judge as provided by Court.
    name: str

    namePrefix: typing.Optional[str]

    nameSuffix: typing.Optional[str]

    # Name of the object
    object: str

    possibleNormJudgeArray: typing.List[PossibleNormJudge]

    sourceJudgeType: str

class OptionalJudge(TypedDict, total=False):
    pass

class Judge(RequiredJudge, OptionalJudge):
    pass
