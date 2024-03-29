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


class PACERSearchReceipt(BaseModel):
    # Description of the search made.
    description: typing.Optional[str] = Field(alias='description')

    # No of pages that was billed for the given PACER search.
    billable_pages: int = Field(alias='billablePages')

    # client code added if any was set.
    client_code: typing.Optional[str] = Field(alias='clientCode')

    # PACER Account ID.
    cso_id: typing.Optional[int] = Field(alias='csoId')

    # Firm ID.
    firm_id: typing.Optional[str] = Field(alias='firmId')

    # ID which is used for PACER login.
    login_id: str = Field(alias='loginId')

    # Name of the object
    object: str = Field(alias='object')

    # Report ID for the search made.
    report_id: typing.Optional[str] = Field(alias='reportId')

    # Details of the search made for this request.
    search: typing.Optional[str] = Field(alias='search')

    # PACER Search Fee.
    search_fee: str = Field(alias='searchFee')

    # Date when the transaction was made at the pacer court site.
    transaction_date: datetime = Field(alias='transactionDate')
    class Config:
        arbitrary_types_allowed = True
