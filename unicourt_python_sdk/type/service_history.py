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


class RequiredServiceHistory(TypedDict):
    # Title held by the Judge.
    title: typing.Optional[str]

    # The President-in-charge of the Judges appointment.
    appointedBy: typing.Optional[str]

    # The year in which the Judge began practicing in his current service.
    fromDate: typing.Optional[datetime]

    # The year in which the Judge began practicing in his current service.
    fromYear: typing.Optional[int]

    # Boolean indicating if the service history  is visible or not.
    isVisible: bool

    object: str

    # The reason for the Judges termination for the current position.
    reasonForTermination: typing.Optional[str]

    # The court served by the Judge. The court is taken from source.
    sourceCourt: typing.Optional[str]

    # The year in which the Judge stoped practicing in his current service.
    toDate: typing.Optional[datetime]

    # The year in which the Judge stoped practicing in his current service.
    toYear: typing.Optional[int]

class OptionalServiceHistory(TypedDict, total=False):
    pass

class ServiceHistory(RequiredServiceHistory, OptionalServiceHistory):
    pass