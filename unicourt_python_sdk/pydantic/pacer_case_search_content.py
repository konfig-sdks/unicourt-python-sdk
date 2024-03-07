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


class PACERCaseSearchContent(BaseModel):
    # Name of the object
    object: str = Field(alias='object')

    # This parameter represents the bankruptcy chapter of the case when it is present
    pcl_bankruptcy_chapter: typing.Optional[str] = Field(alias='pclBankruptcyChapter')

    # Sequentially generated number that identifies the case.
    pcl_case_id: int = Field(alias='pclCaseId')

    # Link to case in the case management/electronic case files (CM/ECF) system at the court.
    pcl_case_link: typing.Optional[str] = Field(alias='pclCaseLink')

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

    # This parameter represents the civil cto number of the case when it is present
    pcl_civil_cto_number: typing.Optional[str] = Field(alias='pclCivilCtoNumber')

    # This parameter represents the civil disposition date of the case when it is present
    pcl_civil_date_disposition: typing.Optional[str] = Field(alias='pclCivilDateDisposition')

    # This parameter represents the civil initiated date of the case when it is present
    pcl_civil_date_initiated: typing.Optional[str] = Field(alias='pclCivilDateInitiated')

    # This parameter represents the civil terminated date of the case when it is present
    pcl_civil_date_terminated: typing.Optional[str] = Field(alias='pclCivilDateTerminated')

    # This parameter represents the civil stat disposition of the case when it is present
    pcl_civil_stat_disposition: typing.Optional[str] = Field(alias='pclCivilStatDisposition')

    # This parameter represents the civil stat initiated of the case when it is present
    pcl_civil_stat_initiated: typing.Optional[str] = Field(alias='pclCivilStatInitiated')

    # This parameter represents the civil stat terminated of the case when it is present
    pcl_civil_stat_terminated: typing.Optional[str] = Field(alias='pclCivilStatTerminated')

    # This parameter represents the civil transferee of the case when it is present
    pcl_civil_transferee: typing.Optional[str] = Field(alias='pclCivilTransferee')

    # The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B
    pcl_court_id: typing.Optional[str] = Field(alias='pclCourtId')

    # This parameter represents the date discharged of the case when it is present
    pcl_date_discharged: typing.Optional[str] = Field(alias='pclDateDischarged')

    # This parameter represents the date dismissed of the case when it is present
    pcl_date_dismissed: typing.Optional[str] = Field(alias='pclDateDismissed')

    # Filing date of the case.
    pcl_date_filed: typing.Optional[str] = Field(alias='pclDateFiled')

    # This parameter represents the date reopened of the case when it is present
    pcl_date_reopened: typing.Optional[str] = Field(alias='pclDateReopened')

    # This parameter represents the date termed of the case when it is present
    pcl_date_termed: typing.Optional[str] = Field(alias='pclDateTermed')

    # This parameter represents the disposition of the case when it is present
    pcl_disposition: typing.Optional[str] = Field(alias='pclDisposition')

    # This parameter represents the disposition method of the case when it is present
    pcl_disposition_method: typing.Optional[str] = Field(alias='pclDispositionMethod')

    # This parameter represents the joint bankruptcy flag of the case when it is present
    pcl_joint_bankruptcy_flag: typing.Optional[str] = Field(alias='pclJointBankruptcyFlag')

    # This parameter represents the joint discharged date of the case when it is present
    pcl_joint_discharged_date: typing.Optional[str] = Field(alias='pclJointDischargedDate')

    # This parameter represents the joint dismissed date of the case when it is present
    pcl_joint_dismissed_date: typing.Optional[str] = Field(alias='pclJointDismissedDate')

    # This parameter represents the joint disposition method of the case when it is present
    pcl_joint_disposition_method: typing.Optional[str] = Field(alias='pclJointDispositionMethod')

    # JPML Case Seed number.
    pcl_jpml_number: typing.Optional[int] = Field(alias='pclJpmlNumber')

    # Link to case in the case management/electronic case files (CM/ECF) system at the court.
    pcl_jurisdiction_type: Literal["Appellate", "Bankruptcy", "Criminal", "Civil", "Multi-district Litigation"] = Field(alias='pclJurisdictionType')

    # Which court does this mdl belongs too.
    pcl_mdl_court_id: typing.Optional[str] = Field(alias='pclMdlCourtId')

    # This parameter represents the mdl date ordered of the case when it is present
    pcl_mdl_date_ordered: typing.Optional[str] = Field(alias='pclMdlDateOrdered')

    # This parameter represents the mdl date received of the case when it is present
    pcl_mdl_date_received: typing.Optional[str] = Field(alias='pclMdlDateReceived')

    # This parameter represents the mdl extension of the case when it is present
    pcl_mdl_extension: typing.Optional[str] = Field(alias='pclMdlExtension')

    # This parameter represents the mdl judge lastname of the case when it is present
    pcl_mdl_judge_last_name: typing.Optional[str] = Field(alias='pclMdlJudgeLastName')

    # This parameter represents the mdl lit type of the case when it is present
    pcl_mdl_littype: typing.Optional[str] = Field(alias='pclMdlLittype')

    # This parameter represents the mdl status of the case when it is present
    pcl_mdl_status: typing.Optional[str] = Field(alias='pclMdlStatus')

    # This parameter represents the mdl transferee of the case when it is present
    pcl_mdl_transferee: typing.Optional[str] = Field(alias='pclMdlTransferee')

    # This parameter represents the mdl transferee district of the case when it is present
    pcl_mdl_transferee_district: typing.Optional[str] = Field(alias='pclMdlTransfereeDistrict')

    # This parameter represents the nature of suit of the case when it is present
    pcl_nature_of_suit: typing.Optional[str] = Field(alias='pclNatureOfSuit')
    class Config:
        arbitrary_types_allowed = True