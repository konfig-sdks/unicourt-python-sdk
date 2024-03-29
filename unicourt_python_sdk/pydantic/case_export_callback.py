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

from unicourt_python_sdk.pydantic.exception import Exception
from unicourt_python_sdk.pydantic.export_file import ExportFile

class CaseExportCallback(BaseModel):
    # Date when the job is run.
    callback_generated_date: typing.Optional[datetime] = Field(alias='callbackGeneratedDate')

    case_export_callback_a_p_i: str = Field(alias='caseExportCallbackAPI')

    # Unique Id for the Case Export Callback.
    case_export_callback_id: str = Field(alias='caseExportCallbackId')

    # Unique Id for a Case in UniCourt.
    case_id: str = Field(alias='caseId')

    exception: Exception = Field(alias='exception')

    file: ExportFile = Field(alias='file')

    # Name of the object.
    object: str = Field(alias='object')

    # Status of the request.
    status: Literal["COMPLETE", "FAILURE", "IN_PROGRESS"] = Field(alias='status')
    class Config:
        arbitrary_types_allowed = True
