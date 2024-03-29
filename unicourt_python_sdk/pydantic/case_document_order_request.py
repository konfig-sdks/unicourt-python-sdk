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

from unicourt_python_sdk.pydantic.case_document_order_pacer_options import CaseDocumentOrderPacerOptions

class CaseDocumentOrderRequest(BaseModel):
    # Document ID which you want to order.
    case_document_id: str = Field(alias='caseDocumentId')

    # Flag value to determine if the document order is a preview order or no.
    is_preview_only: bool = Field(alias='isPreviewOnly')

    pacer_options: typing.Optional[CaseDocumentOrderPacerOptions] = Field(None, alias='pacerOptions')
    class Config:
        arbitrary_types_allowed = True
