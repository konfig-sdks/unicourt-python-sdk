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

from unicourt_python_sdk.pydantic.attorneys import Attorneys
from unicourt_python_sdk.pydantic.case_cause_of_action import CaseCauseOfAction
from unicourt_python_sdk.pydantic.case_charge import CaseCharge
from unicourt_python_sdk.pydantic.case_documents import CaseDocuments
from unicourt_python_sdk.pydantic.case_stats import CaseStats
from unicourt_python_sdk.pydantic.case_status import CaseStatus
from unicourt_python_sdk.pydantic.case_type import CaseType
from unicourt_python_sdk.pydantic.court import Court
from unicourt_python_sdk.pydantic.court_location import CourtLocation
from unicourt_python_sdk.pydantic.docket_entries import DocketEntries
from unicourt_python_sdk.pydantic.hearings import Hearings
from unicourt_python_sdk.pydantic.judges import Judges
from unicourt_python_sdk.pydantic.parties import Parties
from unicourt_python_sdk.pydantic.related_cases import RelatedCases
from unicourt_python_sdk.pydantic.source_case_data import SourceCaseData

class Case(BaseModel):
    attorneys: Attorneys = Field(alias='attorneys')

    case_documents: CaseDocuments = Field(alias='caseDocuments')

    # Unique identifier of Case.
    case_id: str = Field(alias='caseId')

    # Case name as provided by Court.
    case_name: typing.Optional[str] = Field(alias='caseName')

    # Case number as provided by Court.
    case_number: str = Field(alias='caseNumber')

    case_stats: CaseStats = Field(alias='caseStats')

    case_status: CaseStatus = Field(alias='caseStatus')

    case_type: CaseType = Field(alias='caseType')

    # Array of cause of Actions that are added to this case.
    cause_of_action_array: typing.List[CaseCauseOfAction] = Field(alias='causeOfActionArray')

    # Array of charges that are added to this case.
    charge_array: typing.List[CaseCharge] = Field(alias='chargeArray')

    court: Court = Field(alias='court')

    court_location: CourtLocation = Field(alias='courtLocation')

    # API to get the service statuses of the given case.
    court_service_status_a_p_i: typing.Optional[str] = Field(alias='courtServiceStatusAPI')

    # Court Service Status ID of the requested case where we can use it to get the service status
    court_service_status_id: typing.Optional[str] = Field(alias='courtServiceStatusId')

    docket_entries: DocketEntries = Field(alias='docketEntries')

    # When a case is beyond the threshold of entities we provide this link so that the user can request and get all the data of the case with one additional call. This data will be zipped and sent via a webhoook.
    export_a_p_i: str = Field(alias='exportAPI')

    # Filing date for the case provided by the Court. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz
    filed_date: datetime = Field(alias='filedDate')

    # The date and time when the case was first fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,.
    first_fetch_date: datetime = Field(alias='firstFetchDate')

    # This field will be set to TRUE if atleast one document has a preview.
    has_documents_with_preview: bool = Field(alias='hasDocumentsWithPreview')

    # This field determines if this case object has only meta information. If the value is true and if the full information is required you would need to call the updateCase API.
    has_only_meta_info: bool = Field(alias='hasOnlyMetaInfo')

    hearings: Hearings = Field(alias='hearings')

    judges: Judges = Field(alias='judges')

    # The date and time when the case was last fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: It is not necessary that every time the case is fetched from Court we find changes in the case information. It could be that we already have the latest information from the Court and no changes exist.
    last_fetch_date: datetime = Field(alias='lastFetchDate')

    # The date and time when the case was last fetched from the Court where we found changes in the case information. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,
    last_fetch_date_with_updates: datetime = Field(alias='lastFetchDateWithUpdates')

    # Name of the object
    object: str = Field(alias='object')

    # The date and time when parties/attorneys were last updated from the Court. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: This is currently applicable for Federal PACER cases since we have an option to exclude parties and fetch only latest docket entries when updating cases to save PACER fees.
    participants_last_fetch_date: typing.Optional[datetime] = Field(alias='participantsLastFetchDate')

    parties: Parties = Field(alias='parties')

    related_cases: RelatedCases = Field(alias='relatedCases')

    source_case_data: SourceCaseData = Field(alias='sourceCaseData')

    # The status of source data of case. If the value of sourceDataStatus is SOURCE_DEPRECATED then it means that the Case has been migrated from old court site to a new court site and the data being shown in the API response is from a old court site. If the sourceDataStatus is NO_LONGER_AVAILABLE_IN_COURT then it means that a particular case is invalid in the court site.
    source_data_status: Literal["NO_LONGER_AVAILABLE_IN_COURT", "SOURCE_DEPRECATED", None] = Field(alias='sourceDataStatus')

    # URL to the case page in UniCourt Application.
    url: typing.Optional[str] = Field(alias='url')
    class Config:
        arbitrary_types_allowed = True
