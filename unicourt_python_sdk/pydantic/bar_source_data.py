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

from unicourt_python_sdk.pydantic.bar_source_data_administrative_actions_array import BarSourceDataAdministrativeActionsArray
from unicourt_python_sdk.pydantic.bar_source_data_advanced_degree_array import BarSourceDataAdvancedDegreeArray
from unicourt_python_sdk.pydantic.bar_source_data_bar_status_array import BarSourceDataBarStatusArray
from unicourt_python_sdk.pydantic.bar_source_data_board_certifications_array import BarSourceDataBoardCertificationsArray
from unicourt_python_sdk.pydantic.bar_source_data_clients_represented_array import BarSourceDataClientsRepresentedArray
from unicourt_python_sdk.pydantic.bar_source_data_committees_array import BarSourceDataCommitteesArray
from unicourt_python_sdk.pydantic.bar_source_data_court_history_array import BarSourceDataCourtHistoryArray
from unicourt_python_sdk.pydantic.bar_source_data_court_of_admissions import BarSourceDataCourtOfAdmissions
from unicourt_python_sdk.pydantic.bar_source_data_disciplinary_history_array import BarSourceDataDisciplinaryHistoryArray
from unicourt_python_sdk.pydantic.bar_source_data_discipline_summaries_array import BarSourceDataDisciplineSummariesArray
from unicourt_python_sdk.pydantic.bar_source_data_dismissals_array import BarSourceDataDismissalsArray
from unicourt_python_sdk.pydantic.bar_source_data_employment_history_array import BarSourceDataEmploymentHistoryArray
from unicourt_python_sdk.pydantic.bar_source_data_fees_options_array import BarSourceDataFeesOptionsArray
from unicourt_python_sdk.pydantic.bar_source_data_involvements_array import BarSourceDataInvolvementsArray
from unicourt_python_sdk.pydantic.bar_source_data_languages_array import BarSourceDataLanguagesArray
from unicourt_python_sdk.pydantic.bar_source_data_law_school_array import BarSourceDataLawSchoolArray
from unicourt_python_sdk.pydantic.bar_source_data_legal_speciality_array import BarSourceDataLegalSpecialityArray
from unicourt_python_sdk.pydantic.bar_source_data_name import BarSourceDataName
from unicourt_python_sdk.pydantic.bar_source_data_open_action_status_array import BarSourceDataOpenActionStatusArray
from unicourt_python_sdk.pydantic.bar_source_data_other_jurisdiction_array import BarSourceDataOtherJurisdictionArray
from unicourt_python_sdk.pydantic.bar_source_data_other_name_array import BarSourceDataOtherNameArray
from unicourt_python_sdk.pydantic.bar_source_data_pending_proceeding_array import BarSourceDataPendingProceedingArray
from unicourt_python_sdk.pydantic.bar_source_data_practice_area_array import BarSourceDataPracticeAreaArray
from unicourt_python_sdk.pydantic.bar_source_data_practice_location_array import BarSourceDataPracticeLocationArray
from unicourt_python_sdk.pydantic.bar_source_data_public_hearing_array import BarSourceDataPublicHearingArray
from unicourt_python_sdk.pydantic.bar_source_data_reason_for_inactivation import BarSourceDataReasonForInactivation
from unicourt_python_sdk.pydantic.bar_source_data_related_cases_array import BarSourceDataRelatedCasesArray
from unicourt_python_sdk.pydantic.bar_source_data_sections_array import BarSourceDataSectionsArray
from unicourt_python_sdk.pydantic.bar_source_data_services_array import BarSourceDataServicesArray
from unicourt_python_sdk.pydantic.bar_source_data_source_info import BarSourceDataSourceInfo
from unicourt_python_sdk.pydantic.bar_source_data_statewide_grievance_committee_history_array import BarSourceDataStatewideGrievanceCommitteeHistoryArray
from unicourt_python_sdk.pydantic.bar_source_data_status_history_array import BarSourceDataStatusHistoryArray
from unicourt_python_sdk.pydantic.bar_source_data_ten_year_discipline_array import BarSourceDataTenYearDisciplineArray

class BarSourceData(BaseModel):
    administrative_actions_array: BarSourceDataAdministrativeActionsArray = Field(alias='administrativeActionsArray')

    admission_type: typing.Optional[str] = Field(alias='admissionType')

    advanced_degree_array: BarSourceDataAdvancedDegreeArray = Field(alias='advancedDegreeArray')

    appellate_court_district: typing.Optional[str] = Field(alias='appellateCourtDistrict')

    appellate_division_department: typing.Optional[str] = Field(alias='appellateDivisionDepartment')

    attorney_group: typing.Optional[str] = Field(alias='attorneyGroup')

    authorized: typing.Optional[str] = Field(alias='authorized')

    bar_law_firm: typing.Optional[str] = Field(alias='barLawFirm')

    bar_service_class: typing.Optional[str] = Field(alias='barServiceClass')

    bar_status_array: BarSourceDataBarStatusArray = Field(alias='barStatusArray')

    bio: typing.Optional[str] = Field(alias='bio')

    board_certifications_array: BarSourceDataBoardCertificationsArray = Field(alias='boardCertificationsArray')

    board_district: typing.Optional[str] = Field(alias='boardDistrict')

    circuit: typing.Optional[str] = Field(alias='circuit')

    clients_represented_array: BarSourceDataClientsRepresentedArray = Field(alias='clientsRepresentedArray')

    comments: typing.Optional[str] = Field(alias='comments')

    committees_array: BarSourceDataCommitteesArray = Field(alias='committeesArray')

    court_history_array: BarSourceDataCourtHistoryArray = Field(alias='courtHistoryArray')

    court_of_admissions: BarSourceDataCourtOfAdmissions = Field(alias='courtOfAdmissions')

    court_service_email: typing.Optional[str] = Field(alias='courtServiceEmail')

    disciplinary_history_array: BarSourceDataDisciplinaryHistoryArray = Field(alias='disciplinaryHistoryArray')

    discipline_summaries_array: BarSourceDataDisciplineSummariesArray = Field(alias='disciplineSummariesArray')

    dismissals_array: BarSourceDataDismissalsArray = Field(alias='dismissalsArray')

    district: typing.Optional[str] = Field(alias='district')

    employment_history_array: BarSourceDataEmploymentHistoryArray = Field(alias='employmentHistoryArray')

    expiration_date: typing.Optional[datetime] = Field(alias='expirationDate')

    fees_options_array: BarSourceDataFeesOptionsArray = Field(alias='feesOptionsArray')

    firm_size: typing.Optional[str] = Field(alias='firmSize')

    firm_website: typing.Optional[str] = Field(alias='firmWebsite')

    # The firstAdmittedDate is the date when an attorney was admitted to the bar for the very first time regardless of which U.S state.
    first_admitted_date: typing.Optional[datetime] = Field(alias='firstAdmittedDate')

    first_admitted_year: typing.Optional[int] = Field(alias='firstAdmittedYear')

    home_county: typing.Optional[str] = Field(alias='homeCounty')

    in_good_standing: typing.Optional[str] = Field(alias='inGoodStanding')

    insurance: typing.Optional[str] = Field(alias='insurance')

    involvements_array: BarSourceDataInvolvementsArray = Field(alias='involvementsArray')

    judicial_district: typing.Optional[str] = Field(alias='judicialDistrict')

    juris_type: typing.Optional[str] = Field(alias='jurisType')

    languages_array: BarSourceDataLanguagesArray = Field(alias='languagesArray')

    last_renewal_date: typing.Optional[datetime] = Field(alias='lastRenewalDate')

    law_school_array: BarSourceDataLawSchoolArray = Field(alias='lawSchoolArray')

    legal_speciality_array: BarSourceDataLegalSpecialityArray = Field(alias='legalSpecialityArray')

    license_type: typing.Optional[str] = Field(alias='licenseType')

    name: BarSourceDataName = Field(alias='name')

    next_registration: typing.Optional[datetime] = Field(alias='nextRegistration')

    next_renewal_date: typing.Optional[datetime] = Field(alias='nextRenewalDate')

    object: str = Field(alias='object')

    open_action_status_array: BarSourceDataOpenActionStatusArray = Field(alias='openActionStatusArray')

    other_jurisdiction_array: BarSourceDataOtherJurisdictionArray = Field(alias='otherJurisdictionArray')

    other_name_array: BarSourceDataOtherNameArray = Field(alias='otherNameArray')

    parish: typing.Optional[str] = Field(alias='parish')

    pending_proceeding_array: BarSourceDataPendingProceedingArray = Field(alias='pendingProceedingArray')

    position: typing.Optional[str] = Field(alias='position')

    practice_area_array: BarSourceDataPracticeAreaArray = Field(alias='practiceAreaArray')

    practice_location_array: BarSourceDataPracticeLocationArray = Field(alias='practiceLocationArray')

    private_law_practice: typing.Optional[str] = Field(alias='privateLawPractice')

    profile_last_certified: typing.Optional[datetime] = Field(alias='profileLastCertified')

    public_hearing_array: BarSourceDataPublicHearingArray = Field(alias='publicHearingArray')

    reason_for_inactivation: BarSourceDataReasonForInactivation = Field(alias='reasonForInactivation')

    related_cases_array: BarSourceDataRelatedCasesArray = Field(alias='relatedCasesArray')

    sections_array: BarSourceDataSectionsArray = Field(alias='sectionsArray')

    services_array: BarSourceDataServicesArray = Field(alias='servicesArray')

    source_info: BarSourceDataSourceInfo = Field(alias='sourceInfo')

    statewide_grievance_committee_history_array: BarSourceDataStatewideGrievanceCommitteeHistoryArray = Field(alias='statewideGrievanceCommitteeHistoryArray')

    status: typing.Optional[str] = Field(alias='status')

    status_date: typing.Optional[datetime] = Field(alias='statusDate')

    status_hint: typing.Optional[str] = Field(alias='statusHint')

    status_history_array: BarSourceDataStatusHistoryArray = Field(alias='statusHistoryArray')

    ten_year_discipline_array: BarSourceDataTenYearDisciplineArray = Field(alias='tenYearDisciplineArray')

    undergraduate_school: typing.Optional[str] = Field(alias='undergraduateSchool')

    years_of_practice: typing.Optional[str] = Field(alias='yearsOfPractice')
    class Config:
        arbitrary_types_allowed = True