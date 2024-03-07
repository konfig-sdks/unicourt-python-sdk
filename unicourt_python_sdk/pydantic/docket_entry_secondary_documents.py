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

from unicourt_python_sdk.pydantic.case_document import CaseDocument

class DocketEntrySecondaryDocuments(BaseModel):
    case_document_array: typing.List[CaseDocument] = Field(alias='caseDocumentArray')

    # Link to next page of a particular entity in a Case.
    next_page_a_p_i: typing.Optional[str] = Field(alias='nextPageAPI')

    # Name of the object
    object: str = Field(alias='object')

    # Page number for which results where obtained.
    page_number: int = Field(alias='pageNumber')

    # Total number of parties of the Case. entity in a Case.
    total_count: int = Field(alias='totalCount')

    # Total number of pages to obtain all the objects of a party in the Case.
    total_pages: int = Field(alias='totalPages')
    class Config:
        arbitrary_types_allowed = True
