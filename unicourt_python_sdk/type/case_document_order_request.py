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

from unicourt_python_sdk.type.case_document_order_pacer_options import CaseDocumentOrderPacerOptions

class RequiredCaseDocumentOrderRequest(TypedDict):
    # Document ID which you want to order.
    caseDocumentId: str

    # Flag value to determine if the document order is a preview order or no.
    isPreviewOnly: bool

class OptionalCaseDocumentOrderRequest(TypedDict, total=False):
    pacerOptions: CaseDocumentOrderPacerOptions

class CaseDocumentOrderRequest(RequiredCaseDocumentOrderRequest, OptionalCaseDocumentOrderRequest):
    pass
