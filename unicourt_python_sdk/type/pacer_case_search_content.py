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


class RequiredPACERCaseSearchContent(TypedDict):
    # Name of the object
    object: str

    # This parameter represents the bankruptcy chapter of the case when it is present
    pclBankruptcyChapter: typing.Optional[str]

    # Sequentially generated number that identifies the case.
    pclCaseId: int

    # Link to case in the case management/electronic case files (CM/ECF) system at the court.
    pclCaseLink: typing.Optional[str]

    # The sequence number of the case.
    pclCaseNumber: int

    # Case Number.
    pclCaseNumberFull: typing.Optional[str]

    # The divisional office in which the case was filed.
    pclCaseOffice: typing.Optional[str]

    # Title of the case.
    pclCaseTitle: typing.Optional[str]

    # Code that identifies the type of case.
    pclCaseType: typing.Optional[str]

    # The year in which the case falls. Could be two or four digit.
    pclCaseYear: int

    # This parameter represents the civil cto number of the case when it is present
    pclCivilCtoNumber: typing.Optional[str]

    # This parameter represents the civil disposition date of the case when it is present
    pclCivilDateDisposition: typing.Optional[str]

    # This parameter represents the civil initiated date of the case when it is present
    pclCivilDateInitiated: typing.Optional[str]

    # This parameter represents the civil terminated date of the case when it is present
    pclCivilDateTerminated: typing.Optional[str]

    # This parameter represents the civil stat disposition of the case when it is present
    pclCivilStatDisposition: typing.Optional[str]

    # This parameter represents the civil stat initiated of the case when it is present
    pclCivilStatInitiated: typing.Optional[str]

    # This parameter represents the civil stat terminated of the case when it is present
    pclCivilStatTerminated: typing.Optional[str]

    # This parameter represents the civil transferee of the case when it is present
    pclCivilTransferee: typing.Optional[str]

    # The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B
    pclCourtId: typing.Optional[str]

    # This parameter represents the date discharged of the case when it is present
    pclDateDischarged: typing.Optional[str]

    # This parameter represents the date dismissed of the case when it is present
    pclDateDismissed: typing.Optional[str]

    # Filing date of the case.
    pclDateFiled: typing.Optional[str]

    # This parameter represents the date reopened of the case when it is present
    pclDateReopened: typing.Optional[str]

    # This parameter represents the date termed of the case when it is present
    pclDateTermed: typing.Optional[str]

    # This parameter represents the disposition of the case when it is present
    pclDisposition: typing.Optional[str]

    # This parameter represents the disposition method of the case when it is present
    pclDispositionMethod: typing.Optional[str]

    # This parameter represents the joint bankruptcy flag of the case when it is present
    pclJointBankruptcyFlag: typing.Optional[str]

    # This parameter represents the joint discharged date of the case when it is present
    pclJointDischargedDate: typing.Optional[str]

    # This parameter represents the joint dismissed date of the case when it is present
    pclJointDismissedDate: typing.Optional[str]

    # This parameter represents the joint disposition method of the case when it is present
    pclJointDispositionMethod: typing.Optional[str]

    # JPML Case Seed number.
    pclJpmlNumber: typing.Optional[int]

    # Link to case in the case management/electronic case files (CM/ECF) system at the court.
    pclJurisdictionType: str

    # Which court does this mdl belongs too.
    pclMdlCourtId: typing.Optional[str]

    # This parameter represents the mdl date ordered of the case when it is present
    pclMdlDateOrdered: typing.Optional[str]

    # This parameter represents the mdl date received of the case when it is present
    pclMdlDateReceived: typing.Optional[str]

    # This parameter represents the mdl extension of the case when it is present
    pclMdlExtension: typing.Optional[str]

    # This parameter represents the mdl judge lastname of the case when it is present
    pclMdlJudgeLastName: typing.Optional[str]

    # This parameter represents the mdl lit type of the case when it is present
    pclMdlLittype: typing.Optional[str]

    # This parameter represents the mdl status of the case when it is present
    pclMdlStatus: typing.Optional[str]

    # This parameter represents the mdl transferee of the case when it is present
    pclMdlTransferee: typing.Optional[str]

    # This parameter represents the mdl transferee district of the case when it is present
    pclMdlTransfereeDistrict: typing.Optional[str]

    # This parameter represents the nature of suit of the case when it is present
    pclNatureOfSuit: typing.Optional[str]

class OptionalPACERCaseSearchContent(TypedDict, total=False):
    pass

class PACERCaseSearchContent(RequiredPACERCaseSearchContent, OptionalPACERCaseSearchContent):
    pass
