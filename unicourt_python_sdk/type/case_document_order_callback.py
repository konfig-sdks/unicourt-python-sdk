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

from unicourt_python_sdk.type.case_document import CaseDocument
from unicourt_python_sdk.type.exception import Exception
from unicourt_python_sdk.type.export_file import ExportFile

class RequiredCaseDocumentOrderCallback(TypedDict):
    # Date when the job is run.
    callbackGeneratedDate: typing.Optional[datetime]

    caseDocument: CaseDocument

    # UniCourt's Case Document ID.
    caseDocumentId: str

    caseDocumentOrderCallbackAPI: str

    # Unique Id for the Case Document Order Callback.
    caseDocumentOrderCallbackId: str

    exception: Exception

    file: ExportFile

    # Name of the object.
    object: str

    # Status of the request.
    status: str

class OptionalCaseDocumentOrderCallback(TypedDict, total=False):
    pass

class CaseDocumentOrderCallback(RequiredCaseDocumentOrderCallback, OptionalCaseDocumentOrderCallback):
    pass