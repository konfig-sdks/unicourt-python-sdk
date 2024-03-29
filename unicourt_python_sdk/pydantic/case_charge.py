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
from pydantic import BaseModel, Field, RootModel

from unicourt_python_sdk.pydantic.charge import Charge
from unicourt_python_sdk.pydantic.charge_additional_data import ChargeAdditionalData
from unicourt_python_sdk.pydantic.charge_degree import ChargeDegree
from unicourt_python_sdk.pydantic.charge_severity import ChargeSeverity

class CaseCharge(BaseModel):
    charge: Charge = Field(alias='charge')

    charge_additional_data_array: typing.List[ChargeAdditionalData] = Field(alias='chargeAdditionalDataArray')

    charge_degree: ChargeDegree = Field(alias='chargeDegree')

    charge_severity: ChargeSeverity = Field(alias='chargeSeverity')

    # Name of the object
    object: str = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
