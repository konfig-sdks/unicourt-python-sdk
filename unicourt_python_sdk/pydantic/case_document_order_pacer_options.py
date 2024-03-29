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


class CaseDocumentOrderPacerOptions(BaseModel):
    # Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.
    pacer_user_id: str = Field(alias='pacerUserId')

    # PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code.
    pacer_client_code: typing.Optional[typing.Optional[str]] = Field(None, alias='pacerClientCode')
    class Config:
        arbitrary_types_allowed = True
