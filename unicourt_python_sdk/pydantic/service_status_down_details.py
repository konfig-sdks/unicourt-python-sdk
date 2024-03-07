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


class ServiceStatusDownDetails(BaseModel):
    # Details of the reason.
    details: typing.Optional[str] = Field(alias='details')

    # Estimated Time this Service could be Up again for the use.
    eta: typing.Optional[str] = Field(alias='eta')

    # Name of the object
    object: str = Field(alias='object')

    # This field determines the reason behind status being down. Following are the possible reason for the service to be down:   underMaintenance: It means that the site is under scheduled maintenance.   notIntegrated: When an court with specific case type is not integrated in UniCourt.   brokenIntegration: Due to some updates made to the court site our existing Integration has broken and will require a fix to be made to support this court again for a spcific case type category.   sourceMigrated: When a source is migrated from one site to another for a specific case type category.
    reason: Literal["underMaintenance", "notIntegrated", "brokenIntegration", "sourceMigrated"] = Field(alias='reason')
    class Config:
        arbitrary_types_allowed = True