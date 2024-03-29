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

from unicourt_python_sdk.pydantic.pacer_case_search_content import PACERCaseSearchContent

class PACERPartySearchContent(BaseModel):
    # Name of the object
    object: str = Field(alias='object')

    # Sequentially generated number that identifies the case.
    pcl_case_id: int = Field(alias='pclCaseId')

    # The sequence number of the case.
    pcl_case_number: int = Field(alias='pclCaseNumber')

    # Case Number.
    pcl_case_number_full: typing.Optional[str] = Field(alias='pclCaseNumberFull')

    # The divisional office in which the case was filed.
    pcl_case_office: typing.Optional[str] = Field(alias='pclCaseOffice')

    # Title of the case.
    pcl_case_title: typing.Optional[str] = Field(alias='pclCaseTitle')

    # Code that identifies the type of case.
    pcl_case_type: typing.Optional[str] = Field(alias='pclCaseType')

    # The year in which the case falls. Could be two or four digit.
    pcl_case_year: int = Field(alias='pclCaseYear')

    pcl_court_case: PACERCaseSearchContent = Field(alias='pclCourtCase')

    # The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B
    pcl_court_id: typing.Optional[str] = Field(alias='pclCourtId')

    # Filing date of the case.
    pcl_date_filed: typing.Optional[str] = Field(alias='pclDateFiled')

    # This parameter represents the first name of the case when it is present
    pcl_first_name: typing.Optional[str] = Field(alias='pclFirstName')

    # This parameter represents the generation of the case when it is present
    pcl_generation: typing.Optional[str] = Field(alias='pclGeneration')

    # Link to case in the case management/electronic case files (CM/ECF) system at the court.
    pcl_jurisdiction_type: Literal["Appellate", "Bankruptcy", "Criminal", "Civil", "Multi-district Litigation"] = Field(alias='pclJurisdictionType')

    # This parameter represents the last name of the case when it is present
    pcl_last_name: typing.Optional[str] = Field(alias='pclLastName')

    # This parameter represents the middle name of the case when it is present
    pcl_middle_name: typing.Optional[str] = Field(alias='pclMiddleName')

    # This parameter represents the party role of the case when it is present
    pcl_party_role: typing.Optional[str] = Field(alias='pclPartyRole')

    # This parameter represents the party type of the case when it is present
    pcl_party_type: typing.Optional[str] = Field(alias='pclPartyType')
    class Config:
        arbitrary_types_allowed = True
