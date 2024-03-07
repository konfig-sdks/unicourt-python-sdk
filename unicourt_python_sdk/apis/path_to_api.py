import typing_extensions

from unicourt_python_sdk.paths import PathValues
from unicourt_python_sdk.apis.paths.attorney_attorney_id import AttorneyAttorneyId
from unicourt_python_sdk.apis.paths.attorney_attorney_id_associated_parties import AttorneyAttorneyIdAssociatedParties
from unicourt_python_sdk.apis.paths.billing_cycle_usage_billing_cycle import BillingCycleUsageBillingCycle
from unicourt_python_sdk.apis.paths.billing_cycles import BillingCycles
from unicourt_python_sdk.apis.paths.callbacks import Callbacks
from unicourt_python_sdk.apis.paths.case_case_id import CaseCaseId
from unicourt_python_sdk.apis.paths.case_case_id_attorneys import CaseCaseIdAttorneys
from unicourt_python_sdk.apis.paths.case_case_id_docket_entries import CaseCaseIdDocketEntries
from unicourt_python_sdk.apis.paths.case_case_id_docket_entries_primary_documents import CaseCaseIdDocketEntriesPrimaryDocuments
from unicourt_python_sdk.apis.paths.case_case_id_docket_entries_secondary_documents import CaseCaseIdDocketEntriesSecondaryDocuments
from unicourt_python_sdk.apis.paths.case_case_id_documents import CaseCaseIdDocuments
from unicourt_python_sdk.apis.paths.case_case_id_hearings import CaseCaseIdHearings
from unicourt_python_sdk.apis.paths.case_case_id_judges import CaseCaseIdJudges
from unicourt_python_sdk.apis.paths.case_case_id_parties import CaseCaseIdParties
from unicourt_python_sdk.apis.paths.case_case_id_related_cases import CaseCaseIdRelatedCases
from unicourt_python_sdk.apis.paths.case_count_analytics_by_area_of_law import CaseCountAnalyticsByAreaOfLaw
from unicourt_python_sdk.apis.paths.case_count_analytics_by_case_class import CaseCountAnalyticsByCaseClass
from unicourt_python_sdk.apis.paths.case_count_analytics_by_case_filed_date import CaseCountAnalyticsByCaseFiledDate
from unicourt_python_sdk.apis.paths.case_count_analytics_by_case_type import CaseCountAnalyticsByCaseType
from unicourt_python_sdk.apis.paths.case_count_analytics_by_case_type_group import CaseCountAnalyticsByCaseTypeGroup
from unicourt_python_sdk.apis.paths.case_count_analytics_by_court import CaseCountAnalyticsByCourt
from unicourt_python_sdk.apis.paths.case_count_analytics_by_court_location import CaseCountAnalyticsByCourtLocation
from unicourt_python_sdk.apis.paths.case_count_analytics_by_court_system import CaseCountAnalyticsByCourtSystem
from unicourt_python_sdk.apis.paths.case_count_analytics_by_court_type import CaseCountAnalyticsByCourtType
from unicourt_python_sdk.apis.paths.case_count_analytics_by_jurisdiction_geo import CaseCountAnalyticsByJurisdictionGeo
from unicourt_python_sdk.apis.paths.case_count_analytics_by_norm_attorney import CaseCountAnalyticsByNormAttorney
from unicourt_python_sdk.apis.paths.case_count_analytics_by_norm_judge import CaseCountAnalyticsByNormJudge
from unicourt_python_sdk.apis.paths.case_count_analytics_by_norm_law_firm import CaseCountAnalyticsByNormLawFirm
from unicourt_python_sdk.apis.paths.case_count_analytics_by_norm_party import CaseCountAnalyticsByNormParty
from unicourt_python_sdk.apis.paths.case_count_analytics_by_party_role import CaseCountAnalyticsByPartyRole
from unicourt_python_sdk.apis.paths.case_count_analytics_by_party_role_group import CaseCountAnalyticsByPartyRoleGroup
from unicourt_python_sdk.apis.paths.case_document_case_document_id import CaseDocumentCaseDocumentId
from unicourt_python_sdk.apis.paths.case_document_download_case_document_id import CaseDocumentDownloadCaseDocumentId
from unicourt_python_sdk.apis.paths.case_document_order import CaseDocumentOrder
from unicourt_python_sdk.apis.paths.case_document_order_callbacks import CaseDocumentOrderCallbacks
from unicourt_python_sdk.apis.paths.case_document_order_callbacks_case_document_order_callback_id import CaseDocumentOrderCallbacksCaseDocumentOrderCallbackId
from unicourt_python_sdk.apis.paths.case_export_callbacks import CaseExportCallbacks
from unicourt_python_sdk.apis.paths.case_export_callbacks_case_export_callback_id import CaseExportCallbacksCaseExportCallbackId
from unicourt_python_sdk.apis.paths.case_export_case_id import CaseExportCaseId
from unicourt_python_sdk.apis.paths.case_search import CaseSearch
from unicourt_python_sdk.apis.paths.case_search_case_search_id import CaseSearchCaseSearchId
from unicourt_python_sdk.apis.paths.case_track import CaseTrack
from unicourt_python_sdk.apis.paths.case_track_case_id import CaseTrackCaseId
from unicourt_python_sdk.apis.paths.case_tracks import CaseTracks
from unicourt_python_sdk.apis.paths.case_update import CaseUpdate
from unicourt_python_sdk.apis.paths.case_update_case_id import CaseUpdateCaseId
from unicourt_python_sdk.apis.paths.case_updates import CaseUpdates
from unicourt_python_sdk.apis.paths.court_coverage_court_id import CourtCoverageCourtId
from unicourt_python_sdk.apis.paths.daily_usage_date import DailyUsageDate
from unicourt_python_sdk.apis.paths.generate_new_token import GenerateNewToken
from unicourt_python_sdk.apis.paths.invalidate_all_tokens import InvalidateAllTokens
from unicourt_python_sdk.apis.paths.invalidate_token import InvalidateToken
from unicourt_python_sdk.apis.paths.judge_judge_id import JudgeJudgeId
from unicourt_python_sdk.apis.paths.list_all_token_ids import ListAllTokenIds
from unicourt_python_sdk.apis.paths.master_data_area_of_law import MasterDataAreaOfLaw
from unicourt_python_sdk.apis.paths.master_data_area_of_law_area_of_law_id import MasterDataAreaOfLawAreaOfLawId
from unicourt_python_sdk.apis.paths.master_data_attorney_representation_type import MasterDataAttorneyRepresentationType
from unicourt_python_sdk.apis.paths.master_data_attorney_representation_type_attorney_representation_type_id import MasterDataAttorneyRepresentationTypeAttorneyRepresentationTypeId
from unicourt_python_sdk.apis.paths.master_data_attorney_type import MasterDataAttorneyType
from unicourt_python_sdk.apis.paths.master_data_attorney_type_attorney_type_id import MasterDataAttorneyTypeAttorneyTypeId
from unicourt_python_sdk.apis.paths.master_data_case_class import MasterDataCaseClass
from unicourt_python_sdk.apis.paths.master_data_case_class_case_class_id import MasterDataCaseClassCaseClassId
from unicourt_python_sdk.apis.paths.master_data_case_relationship_type import MasterDataCaseRelationshipType
from unicourt_python_sdk.apis.paths.master_data_case_relationship_type_case_relationship_type_id import MasterDataCaseRelationshipTypeCaseRelationshipTypeId
from unicourt_python_sdk.apis.paths.master_data_case_status import MasterDataCaseStatus
from unicourt_python_sdk.apis.paths.master_data_case_status_case_status_id import MasterDataCaseStatusCaseStatusId
from unicourt_python_sdk.apis.paths.master_data_case_status_group import MasterDataCaseStatusGroup
from unicourt_python_sdk.apis.paths.master_data_case_status_group_case_status_group_id import MasterDataCaseStatusGroupCaseStatusGroupId
from unicourt_python_sdk.apis.paths.master_data_case_type import MasterDataCaseType
from unicourt_python_sdk.apis.paths.master_data_case_type_case_type_id import MasterDataCaseTypeCaseTypeId
from unicourt_python_sdk.apis.paths.master_data_case_type_group import MasterDataCaseTypeGroup
from unicourt_python_sdk.apis.paths.master_data_case_type_group_case_type_group_id import MasterDataCaseTypeGroupCaseTypeGroupId
from unicourt_python_sdk.apis.paths.master_data_cause_of_action import MasterDataCauseOfAction
from unicourt_python_sdk.apis.paths.master_data_cause_of_action_cause_of_action_id import MasterDataCauseOfActionCauseOfActionId
from unicourt_python_sdk.apis.paths.master_data_cause_of_action_additional_data import MasterDataCauseOfActionAdditionalData
from unicourt_python_sdk.apis.paths.master_data_cause_of_action_additional_data_cause_of_action_additional_data_id import MasterDataCauseOfActionAdditionalDataCauseOfActionAdditionalDataId
from unicourt_python_sdk.apis.paths.master_data_cause_of_action_group import MasterDataCauseOfActionGroup
from unicourt_python_sdk.apis.paths.master_data_cause_of_action_group_cause_of_action_group_id import MasterDataCauseOfActionGroupCauseOfActionGroupId
from unicourt_python_sdk.apis.paths.master_data_charge import MasterDataCharge
from unicourt_python_sdk.apis.paths.master_data_charge_charge_id import MasterDataChargeChargeId
from unicourt_python_sdk.apis.paths.master_data_charge_additional_data import MasterDataChargeAdditionalData
from unicourt_python_sdk.apis.paths.master_data_charge_additional_data_charge_additional_data_id import MasterDataChargeAdditionalDataChargeAdditionalDataId
from unicourt_python_sdk.apis.paths.master_data_charge_degree import MasterDataChargeDegree
from unicourt_python_sdk.apis.paths.master_data_charge_degree_charge_degree_id import MasterDataChargeDegreeChargeDegreeId
from unicourt_python_sdk.apis.paths.master_data_charge_group import MasterDataChargeGroup
from unicourt_python_sdk.apis.paths.master_data_charge_group_charge_group_id import MasterDataChargeGroupChargeGroupId
from unicourt_python_sdk.apis.paths.master_data_charge_severity import MasterDataChargeSeverity
from unicourt_python_sdk.apis.paths.master_data_charge_severity_charge_severity_id import MasterDataChargeSeverityChargeSeverityId
from unicourt_python_sdk.apis.paths.master_data_court import MasterDataCourt
from unicourt_python_sdk.apis.paths.master_data_court_court_id import MasterDataCourtCourtId
from unicourt_python_sdk.apis.paths.master_data_court_court_id_appeal_courts import MasterDataCourtCourtIdAppealCourts
from unicourt_python_sdk.apis.paths.master_data_court_court_id_court_locations import MasterDataCourtCourtIdCourtLocations
from unicourt_python_sdk.apis.paths.master_data_court_court_id_jurisdiction_geo import MasterDataCourtCourtIdJurisdictionGeo
from unicourt_python_sdk.apis.paths.master_data_court_location import MasterDataCourtLocation
from unicourt_python_sdk.apis.paths.master_data_court_location_court_location_id import MasterDataCourtLocationCourtLocationId
from unicourt_python_sdk.apis.paths.master_data_court_location_court_location_id_courts import MasterDataCourtLocationCourtLocationIdCourts
from unicourt_python_sdk.apis.paths.master_data_court_service_status import MasterDataCourtServiceStatus
from unicourt_python_sdk.apis.paths.master_data_court_service_status_court_service_status_id import MasterDataCourtServiceStatusCourtServiceStatusId
from unicourt_python_sdk.apis.paths.master_data_court_system import MasterDataCourtSystem
from unicourt_python_sdk.apis.paths.master_data_court_system_court_system_id import MasterDataCourtSystemCourtSystemId
from unicourt_python_sdk.apis.paths.master_data_court_type import MasterDataCourtType
from unicourt_python_sdk.apis.paths.master_data_court_type_court_type_id import MasterDataCourtTypeCourtTypeId
from unicourt_python_sdk.apis.paths.master_data_judge_type import MasterDataJudgeType
from unicourt_python_sdk.apis.paths.master_data_judge_type_judge_type_id import MasterDataJudgeTypeJudgeTypeId
from unicourt_python_sdk.apis.paths.master_data_jurisdiction_geo import MasterDataJurisdictionGeo
from unicourt_python_sdk.apis.paths.master_data_jurisdiction_geo_jurisdiction_geo_id import MasterDataJurisdictionGeoJurisdictionGeoId
from unicourt_python_sdk.apis.paths.master_data_jurisdiction_geo_jurisdiction_geo_id_courts import MasterDataJurisdictionGeoJurisdictionGeoIdCourts
from unicourt_python_sdk.apis.paths.master_data_party_role import MasterDataPartyRole
from unicourt_python_sdk.apis.paths.master_data_party_role_party_role_id import MasterDataPartyRolePartyRoleId
from unicourt_python_sdk.apis.paths.master_data_party_role_group import MasterDataPartyRoleGroup
from unicourt_python_sdk.apis.paths.master_data_party_role_group_party_role_group_id import MasterDataPartyRoleGroupPartyRoleGroupId
from unicourt_python_sdk.apis.paths.norm_attorney_norm_attorney_id import NormAttorneyNormAttorneyId
from unicourt_python_sdk.apis.paths.norm_attorney_norm_attorney_id_associated_norm_judges import NormAttorneyNormAttorneyIdAssociatedNormJudges
from unicourt_python_sdk.apis.paths.norm_attorney_norm_attorney_id_associated_norm_law_firms import NormAttorneyNormAttorneyIdAssociatedNormLawFirms
from unicourt_python_sdk.apis.paths.norm_attorney_norm_attorney_id_associated_norm_parties import NormAttorneyNormAttorneyIdAssociatedNormParties
from unicourt_python_sdk.apis.paths.norm_attorney_norm_attorney_id_case_count_analytics_by_opposing_norm_attorney import NormAttorneyNormAttorneyIdCaseCountAnalyticsByOpposingNormAttorney
from unicourt_python_sdk.apis.paths.norm_attorney_search import NormAttorneySearch
from unicourt_python_sdk.apis.paths.norm_attorney_search_norm_attorney_search_id import NormAttorneySearchNormAttorneySearchId
from unicourt_python_sdk.apis.paths.norm_judge_norm_judge_id import NormJudgeNormJudgeId
from unicourt_python_sdk.apis.paths.norm_judge_norm_judge_id_associated_norm_attorneys import NormJudgeNormJudgeIdAssociatedNormAttorneys
from unicourt_python_sdk.apis.paths.norm_judge_norm_judge_id_associated_norm_law_firms import NormJudgeNormJudgeIdAssociatedNormLawFirms
from unicourt_python_sdk.apis.paths.norm_judge_norm_judge_id_associated_norm_parties import NormJudgeNormJudgeIdAssociatedNormParties
from unicourt_python_sdk.apis.paths.norm_judge_search import NormJudgeSearch
from unicourt_python_sdk.apis.paths.norm_judge_search_norm_judge_search_id import NormJudgeSearchNormJudgeSearchId
from unicourt_python_sdk.apis.paths.norm_law_firm_norm_law_firm_id import NormLawFirmNormLawFirmId
from unicourt_python_sdk.apis.paths.norm_law_firm_norm_law_firm_id_associated_norm_attorneys import NormLawFirmNormLawFirmIdAssociatedNormAttorneys
from unicourt_python_sdk.apis.paths.norm_law_firm_norm_law_firm_id_associated_norm_judges import NormLawFirmNormLawFirmIdAssociatedNormJudges
from unicourt_python_sdk.apis.paths.norm_law_firm_norm_law_firm_id_associated_norm_parties import NormLawFirmNormLawFirmIdAssociatedNormParties
from unicourt_python_sdk.apis.paths.norm_law_firm_norm_law_firm_id_case_count_analytics_by_opposing_norm_law_firm import NormLawFirmNormLawFirmIdCaseCountAnalyticsByOpposingNormLawFirm
from unicourt_python_sdk.apis.paths.norm_law_firm_search import NormLawFirmSearch
from unicourt_python_sdk.apis.paths.norm_law_firm_search_norm_law_firm_search_id import NormLawFirmSearchNormLawFirmSearchId
from unicourt_python_sdk.apis.paths.norm_party_norm_party_id import NormPartyNormPartyId
from unicourt_python_sdk.apis.paths.norm_party_norm_party_id_associated_norm_attorneys import NormPartyNormPartyIdAssociatedNormAttorneys
from unicourt_python_sdk.apis.paths.norm_party_norm_party_id_associated_norm_judges import NormPartyNormPartyIdAssociatedNormJudges
from unicourt_python_sdk.apis.paths.norm_party_norm_party_id_associated_norm_law_firms import NormPartyNormPartyIdAssociatedNormLawFirms
from unicourt_python_sdk.apis.paths.norm_party_norm_party_id_case_count_analytics_by_opposing_norm_party import NormPartyNormPartyIdCaseCountAnalyticsByOpposingNormParty
from unicourt_python_sdk.apis.paths.norm_party_search import NormPartySearch
from unicourt_python_sdk.apis.paths.norm_party_search_norm_party_search_id import NormPartySearchNormPartySearchId
from unicourt_python_sdk.apis.paths.pacer_import_case_by_court_using_case_number import PacerImportCaseByCourtUsingCaseNumber
from unicourt_python_sdk.apis.paths.pacer_case_locator_case_search_all_courts import PacerCaseLocatorCaseSearchAllCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_case_search_appeal_courts import PacerCaseLocatorCaseSearchAppealCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_case_search_bankruptcy_courts import PacerCaseLocatorCaseSearchBankruptcyCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_case_search_civil_courts import PacerCaseLocatorCaseSearchCivilCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_case_search_criminal_courts import PacerCaseLocatorCaseSearchCriminalCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_case_search_multi_district_courts import PacerCaseLocatorCaseSearchMultiDistrictCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_party_search_all_courts import PacerCaseLocatorPartySearchAllCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_party_search_appeal_courts import PacerCaseLocatorPartySearchAppealCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_party_search_bankruptcy_courts import PacerCaseLocatorPartySearchBankruptcyCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_party_search_civil_courts import PacerCaseLocatorPartySearchCivilCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_party_search_criminal_courts import PacerCaseLocatorPartySearchCriminalCourts
from unicourt_python_sdk.apis.paths.pacer_case_locator_party_search_multi_district_courts import PacerCaseLocatorPartySearchMultiDistrictCourts
from unicourt_python_sdk.apis.paths.pacer_credential import PacerCredential
from unicourt_python_sdk.apis.paths.pacer_credential_pacer_user_id import PacerCredentialPacerUserId
from unicourt_python_sdk.apis.paths.party_party_id import PartyPartyId
from unicourt_python_sdk.apis.paths.party_party_id_associated_attorneys import PartyPartyIdAssociatedAttorneys

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ATTORNEY_ATTORNEY_ID: AttorneyAttorneyId,
        PathValues.ATTORNEY_ATTORNEY_ID_ASSOCIATED_PARTIES: AttorneyAttorneyIdAssociatedParties,
        PathValues.BILLING_CYCLE_USAGE_BILLING_CYCLE: BillingCycleUsageBillingCycle,
        PathValues.BILLING_CYCLES: BillingCycles,
        PathValues.CALLBACKS: Callbacks,
        PathValues.CASE_CASE_ID: CaseCaseId,
        PathValues.CASE_CASE_ID_ATTORNEYS: CaseCaseIdAttorneys,
        PathValues.CASE_CASE_ID_DOCKET_ENTRIES: CaseCaseIdDocketEntries,
        PathValues.CASE_CASE_ID_DOCKET_ENTRIES_PRIMARY_DOCUMENTS: CaseCaseIdDocketEntriesPrimaryDocuments,
        PathValues.CASE_CASE_ID_DOCKET_ENTRIES_SECONDARY_DOCUMENTS: CaseCaseIdDocketEntriesSecondaryDocuments,
        PathValues.CASE_CASE_ID_DOCUMENTS: CaseCaseIdDocuments,
        PathValues.CASE_CASE_ID_HEARINGS: CaseCaseIdHearings,
        PathValues.CASE_CASE_ID_JUDGES: CaseCaseIdJudges,
        PathValues.CASE_CASE_ID_PARTIES: CaseCaseIdParties,
        PathValues.CASE_CASE_ID_RELATED_CASES: CaseCaseIdRelatedCases,
        PathValues.CASE_COUNT_ANALYTICS_BY_AREA_OF_LAW: CaseCountAnalyticsByAreaOfLaw,
        PathValues.CASE_COUNT_ANALYTICS_BY_CASE_CLASS: CaseCountAnalyticsByCaseClass,
        PathValues.CASE_COUNT_ANALYTICS_BY_CASE_FILED_DATE: CaseCountAnalyticsByCaseFiledDate,
        PathValues.CASE_COUNT_ANALYTICS_BY_CASE_TYPE: CaseCountAnalyticsByCaseType,
        PathValues.CASE_COUNT_ANALYTICS_BY_CASE_TYPE_GROUP: CaseCountAnalyticsByCaseTypeGroup,
        PathValues.CASE_COUNT_ANALYTICS_BY_COURT: CaseCountAnalyticsByCourt,
        PathValues.CASE_COUNT_ANALYTICS_BY_COURT_LOCATION: CaseCountAnalyticsByCourtLocation,
        PathValues.CASE_COUNT_ANALYTICS_BY_COURT_SYSTEM: CaseCountAnalyticsByCourtSystem,
        PathValues.CASE_COUNT_ANALYTICS_BY_COURT_TYPE: CaseCountAnalyticsByCourtType,
        PathValues.CASE_COUNT_ANALYTICS_BY_JURISDICTION_GEO: CaseCountAnalyticsByJurisdictionGeo,
        PathValues.CASE_COUNT_ANALYTICS_BY_NORM_ATTORNEY: CaseCountAnalyticsByNormAttorney,
        PathValues.CASE_COUNT_ANALYTICS_BY_NORM_JUDGE: CaseCountAnalyticsByNormJudge,
        PathValues.CASE_COUNT_ANALYTICS_BY_NORM_LAW_FIRM: CaseCountAnalyticsByNormLawFirm,
        PathValues.CASE_COUNT_ANALYTICS_BY_NORM_PARTY: CaseCountAnalyticsByNormParty,
        PathValues.CASE_COUNT_ANALYTICS_BY_PARTY_ROLE: CaseCountAnalyticsByPartyRole,
        PathValues.CASE_COUNT_ANALYTICS_BY_PARTY_ROLE_GROUP: CaseCountAnalyticsByPartyRoleGroup,
        PathValues.CASE_DOCUMENT_CASE_DOCUMENT_ID: CaseDocumentCaseDocumentId,
        PathValues.CASE_DOCUMENT_DOWNLOAD_CASE_DOCUMENT_ID: CaseDocumentDownloadCaseDocumentId,
        PathValues.CASE_DOCUMENT_ORDER: CaseDocumentOrder,
        PathValues.CASE_DOCUMENT_ORDER_CALLBACKS: CaseDocumentOrderCallbacks,
        PathValues.CASE_DOCUMENT_ORDER_CALLBACKS_CASE_DOCUMENT_ORDER_CALLBACK_ID: CaseDocumentOrderCallbacksCaseDocumentOrderCallbackId,
        PathValues.CASE_EXPORT_CALLBACKS: CaseExportCallbacks,
        PathValues.CASE_EXPORT_CALLBACKS_CASE_EXPORT_CALLBACK_ID: CaseExportCallbacksCaseExportCallbackId,
        PathValues.CASE_EXPORT_CASE_ID: CaseExportCaseId,
        PathValues.CASE_SEARCH: CaseSearch,
        PathValues.CASE_SEARCH_CASE_SEARCH_ID: CaseSearchCaseSearchId,
        PathValues.CASE_TRACK: CaseTrack,
        PathValues.CASE_TRACK_CASE_ID: CaseTrackCaseId,
        PathValues.CASE_TRACKS: CaseTracks,
        PathValues.CASE_UPDATE: CaseUpdate,
        PathValues.CASE_UPDATE_CASE_ID: CaseUpdateCaseId,
        PathValues.CASE_UPDATES: CaseUpdates,
        PathValues.COURT_COVERAGE_COURT_ID: CourtCoverageCourtId,
        PathValues.DAILY_USAGE_DATE: DailyUsageDate,
        PathValues.GENERATE_NEW_TOKEN: GenerateNewToken,
        PathValues.INVALIDATE_ALL_TOKENS: InvalidateAllTokens,
        PathValues.INVALIDATE_TOKEN: InvalidateToken,
        PathValues.JUDGE_JUDGE_ID: JudgeJudgeId,
        PathValues.LIST_ALL_TOKEN_IDS: ListAllTokenIds,
        PathValues.MASTER_DATA_AREA_OF_LAW: MasterDataAreaOfLaw,
        PathValues.MASTER_DATA_AREA_OF_LAW_AREA_OF_LAW_ID: MasterDataAreaOfLawAreaOfLawId,
        PathValues.MASTER_DATA_ATTORNEY_REPRESENTATION_TYPE: MasterDataAttorneyRepresentationType,
        PathValues.MASTER_DATA_ATTORNEY_REPRESENTATION_TYPE_ATTORNEY_REPRESENTATION_TYPE_ID: MasterDataAttorneyRepresentationTypeAttorneyRepresentationTypeId,
        PathValues.MASTER_DATA_ATTORNEY_TYPE: MasterDataAttorneyType,
        PathValues.MASTER_DATA_ATTORNEY_TYPE_ATTORNEY_TYPE_ID: MasterDataAttorneyTypeAttorneyTypeId,
        PathValues.MASTER_DATA_CASE_CLASS: MasterDataCaseClass,
        PathValues.MASTER_DATA_CASE_CLASS_CASE_CLASS_ID: MasterDataCaseClassCaseClassId,
        PathValues.MASTER_DATA_CASE_RELATIONSHIP_TYPE: MasterDataCaseRelationshipType,
        PathValues.MASTER_DATA_CASE_RELATIONSHIP_TYPE_CASE_RELATIONSHIP_TYPE_ID: MasterDataCaseRelationshipTypeCaseRelationshipTypeId,
        PathValues.MASTER_DATA_CASE_STATUS: MasterDataCaseStatus,
        PathValues.MASTER_DATA_CASE_STATUS_CASE_STATUS_ID: MasterDataCaseStatusCaseStatusId,
        PathValues.MASTER_DATA_CASE_STATUS_GROUP: MasterDataCaseStatusGroup,
        PathValues.MASTER_DATA_CASE_STATUS_GROUP_CASE_STATUS_GROUP_ID: MasterDataCaseStatusGroupCaseStatusGroupId,
        PathValues.MASTER_DATA_CASE_TYPE: MasterDataCaseType,
        PathValues.MASTER_DATA_CASE_TYPE_CASE_TYPE_ID: MasterDataCaseTypeCaseTypeId,
        PathValues.MASTER_DATA_CASE_TYPE_GROUP: MasterDataCaseTypeGroup,
        PathValues.MASTER_DATA_CASE_TYPE_GROUP_CASE_TYPE_GROUP_ID: MasterDataCaseTypeGroupCaseTypeGroupId,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION: MasterDataCauseOfAction,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_CAUSE_OF_ACTION_ID: MasterDataCauseOfActionCauseOfActionId,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_ADDITIONAL_DATA: MasterDataCauseOfActionAdditionalData,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_ADDITIONAL_DATA_CAUSE_OF_ACTION_ADDITIONAL_DATA_ID: MasterDataCauseOfActionAdditionalDataCauseOfActionAdditionalDataId,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_GROUP: MasterDataCauseOfActionGroup,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_GROUP_CAUSE_OF_ACTION_GROUP_ID: MasterDataCauseOfActionGroupCauseOfActionGroupId,
        PathValues.MASTER_DATA_CHARGE: MasterDataCharge,
        PathValues.MASTER_DATA_CHARGE_CHARGE_ID: MasterDataChargeChargeId,
        PathValues.MASTER_DATA_CHARGE_ADDITIONAL_DATA: MasterDataChargeAdditionalData,
        PathValues.MASTER_DATA_CHARGE_ADDITIONAL_DATA_CHARGE_ADDITIONAL_DATA_ID: MasterDataChargeAdditionalDataChargeAdditionalDataId,
        PathValues.MASTER_DATA_CHARGE_DEGREE: MasterDataChargeDegree,
        PathValues.MASTER_DATA_CHARGE_DEGREE_CHARGE_DEGREE_ID: MasterDataChargeDegreeChargeDegreeId,
        PathValues.MASTER_DATA_CHARGE_GROUP: MasterDataChargeGroup,
        PathValues.MASTER_DATA_CHARGE_GROUP_CHARGE_GROUP_ID: MasterDataChargeGroupChargeGroupId,
        PathValues.MASTER_DATA_CHARGE_SEVERITY: MasterDataChargeSeverity,
        PathValues.MASTER_DATA_CHARGE_SEVERITY_CHARGE_SEVERITY_ID: MasterDataChargeSeverityChargeSeverityId,
        PathValues.MASTER_DATA_COURT: MasterDataCourt,
        PathValues.MASTER_DATA_COURT_COURT_ID: MasterDataCourtCourtId,
        PathValues.MASTER_DATA_COURT_COURT_ID_APPEAL_COURTS: MasterDataCourtCourtIdAppealCourts,
        PathValues.MASTER_DATA_COURT_COURT_ID_COURT_LOCATIONS: MasterDataCourtCourtIdCourtLocations,
        PathValues.MASTER_DATA_COURT_COURT_ID_JURISDICTION_GEO: MasterDataCourtCourtIdJurisdictionGeo,
        PathValues.MASTER_DATA_COURT_LOCATION: MasterDataCourtLocation,
        PathValues.MASTER_DATA_COURT_LOCATION_COURT_LOCATION_ID: MasterDataCourtLocationCourtLocationId,
        PathValues.MASTER_DATA_COURT_LOCATION_COURT_LOCATION_ID_COURTS: MasterDataCourtLocationCourtLocationIdCourts,
        PathValues.MASTER_DATA_COURT_SERVICE_STATUS: MasterDataCourtServiceStatus,
        PathValues.MASTER_DATA_COURT_SERVICE_STATUS_COURT_SERVICE_STATUS_ID: MasterDataCourtServiceStatusCourtServiceStatusId,
        PathValues.MASTER_DATA_COURT_SYSTEM: MasterDataCourtSystem,
        PathValues.MASTER_DATA_COURT_SYSTEM_COURT_SYSTEM_ID: MasterDataCourtSystemCourtSystemId,
        PathValues.MASTER_DATA_COURT_TYPE: MasterDataCourtType,
        PathValues.MASTER_DATA_COURT_TYPE_COURT_TYPE_ID: MasterDataCourtTypeCourtTypeId,
        PathValues.MASTER_DATA_JUDGE_TYPE: MasterDataJudgeType,
        PathValues.MASTER_DATA_JUDGE_TYPE_JUDGE_TYPE_ID: MasterDataJudgeTypeJudgeTypeId,
        PathValues.MASTER_DATA_JURISDICTION_GEO: MasterDataJurisdictionGeo,
        PathValues.MASTER_DATA_JURISDICTION_GEO_JURISDICTION_GEO_ID: MasterDataJurisdictionGeoJurisdictionGeoId,
        PathValues.MASTER_DATA_JURISDICTION_GEO_JURISDICTION_GEO_ID_COURTS: MasterDataJurisdictionGeoJurisdictionGeoIdCourts,
        PathValues.MASTER_DATA_PARTY_ROLE: MasterDataPartyRole,
        PathValues.MASTER_DATA_PARTY_ROLE_PARTY_ROLE_ID: MasterDataPartyRolePartyRoleId,
        PathValues.MASTER_DATA_PARTY_ROLE_GROUP: MasterDataPartyRoleGroup,
        PathValues.MASTER_DATA_PARTY_ROLE_GROUP_PARTY_ROLE_GROUP_ID: MasterDataPartyRoleGroupPartyRoleGroupId,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID: NormAttorneyNormAttorneyId,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID_ASSOCIATED_NORM_JUDGES: NormAttorneyNormAttorneyIdAssociatedNormJudges,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID_ASSOCIATED_NORM_LAW_FIRMS: NormAttorneyNormAttorneyIdAssociatedNormLawFirms,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID_ASSOCIATED_NORM_PARTIES: NormAttorneyNormAttorneyIdAssociatedNormParties,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID_CASE_COUNT_ANALYTICS_BY_OPPOSING_NORM_ATTORNEY: NormAttorneyNormAttorneyIdCaseCountAnalyticsByOpposingNormAttorney,
        PathValues.NORM_ATTORNEY_SEARCH: NormAttorneySearch,
        PathValues.NORM_ATTORNEY_SEARCH_NORM_ATTORNEY_SEARCH_ID: NormAttorneySearchNormAttorneySearchId,
        PathValues.NORM_JUDGE_NORM_JUDGE_ID: NormJudgeNormJudgeId,
        PathValues.NORM_JUDGE_NORM_JUDGE_ID_ASSOCIATED_NORM_ATTORNEYS: NormJudgeNormJudgeIdAssociatedNormAttorneys,
        PathValues.NORM_JUDGE_NORM_JUDGE_ID_ASSOCIATED_NORM_LAW_FIRMS: NormJudgeNormJudgeIdAssociatedNormLawFirms,
        PathValues.NORM_JUDGE_NORM_JUDGE_ID_ASSOCIATED_NORM_PARTIES: NormJudgeNormJudgeIdAssociatedNormParties,
        PathValues.NORM_JUDGE_SEARCH: NormJudgeSearch,
        PathValues.NORM_JUDGE_SEARCH_NORM_JUDGE_SEARCH_ID: NormJudgeSearchNormJudgeSearchId,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID: NormLawFirmNormLawFirmId,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID_ASSOCIATED_NORM_ATTORNEYS: NormLawFirmNormLawFirmIdAssociatedNormAttorneys,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID_ASSOCIATED_NORM_JUDGES: NormLawFirmNormLawFirmIdAssociatedNormJudges,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID_ASSOCIATED_NORM_PARTIES: NormLawFirmNormLawFirmIdAssociatedNormParties,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID_CASE_COUNT_ANALYTICS_BY_OPPOSING_NORM_LAW_FIRM: NormLawFirmNormLawFirmIdCaseCountAnalyticsByOpposingNormLawFirm,
        PathValues.NORM_LAW_FIRM_SEARCH: NormLawFirmSearch,
        PathValues.NORM_LAW_FIRM_SEARCH_NORM_LAW_FIRM_SEARCH_ID: NormLawFirmSearchNormLawFirmSearchId,
        PathValues.NORM_PARTY_NORM_PARTY_ID: NormPartyNormPartyId,
        PathValues.NORM_PARTY_NORM_PARTY_ID_ASSOCIATED_NORM_ATTORNEYS: NormPartyNormPartyIdAssociatedNormAttorneys,
        PathValues.NORM_PARTY_NORM_PARTY_ID_ASSOCIATED_NORM_JUDGES: NormPartyNormPartyIdAssociatedNormJudges,
        PathValues.NORM_PARTY_NORM_PARTY_ID_ASSOCIATED_NORM_LAW_FIRMS: NormPartyNormPartyIdAssociatedNormLawFirms,
        PathValues.NORM_PARTY_NORM_PARTY_ID_CASE_COUNT_ANALYTICS_BY_OPPOSING_NORM_PARTY: NormPartyNormPartyIdCaseCountAnalyticsByOpposingNormParty,
        PathValues.NORM_PARTY_SEARCH: NormPartySearch,
        PathValues.NORM_PARTY_SEARCH_NORM_PARTY_SEARCH_ID: NormPartySearchNormPartySearchId,
        PathValues.PACER_IMPORT_CASE_BY_COURT_USING_CASE_NUMBER: PacerImportCaseByCourtUsingCaseNumber,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_ALL_COURTS: PacerCaseLocatorCaseSearchAllCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_APPEAL_COURTS: PacerCaseLocatorCaseSearchAppealCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_BANKRUPTCY_COURTS: PacerCaseLocatorCaseSearchBankruptcyCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_CIVIL_COURTS: PacerCaseLocatorCaseSearchCivilCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_CRIMINAL_COURTS: PacerCaseLocatorCaseSearchCriminalCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_MULTI_DISTRICT_COURTS: PacerCaseLocatorCaseSearchMultiDistrictCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_ALL_COURTS: PacerCaseLocatorPartySearchAllCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_APPEAL_COURTS: PacerCaseLocatorPartySearchAppealCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_BANKRUPTCY_COURTS: PacerCaseLocatorPartySearchBankruptcyCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_CIVIL_COURTS: PacerCaseLocatorPartySearchCivilCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_CRIMINAL_COURTS: PacerCaseLocatorPartySearchCriminalCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_MULTI_DISTRICT_COURTS: PacerCaseLocatorPartySearchMultiDistrictCourts,
        PathValues.PACER_CREDENTIAL: PacerCredential,
        PathValues.PACER_CREDENTIAL_PACER_USER_ID: PacerCredentialPacerUserId,
        PathValues.PARTY_PARTY_ID: PartyPartyId,
        PathValues.PARTY_PARTY_ID_ASSOCIATED_ATTORNEYS: PartyPartyIdAssociatedAttorneys,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ATTORNEY_ATTORNEY_ID: AttorneyAttorneyId,
        PathValues.ATTORNEY_ATTORNEY_ID_ASSOCIATED_PARTIES: AttorneyAttorneyIdAssociatedParties,
        PathValues.BILLING_CYCLE_USAGE_BILLING_CYCLE: BillingCycleUsageBillingCycle,
        PathValues.BILLING_CYCLES: BillingCycles,
        PathValues.CALLBACKS: Callbacks,
        PathValues.CASE_CASE_ID: CaseCaseId,
        PathValues.CASE_CASE_ID_ATTORNEYS: CaseCaseIdAttorneys,
        PathValues.CASE_CASE_ID_DOCKET_ENTRIES: CaseCaseIdDocketEntries,
        PathValues.CASE_CASE_ID_DOCKET_ENTRIES_PRIMARY_DOCUMENTS: CaseCaseIdDocketEntriesPrimaryDocuments,
        PathValues.CASE_CASE_ID_DOCKET_ENTRIES_SECONDARY_DOCUMENTS: CaseCaseIdDocketEntriesSecondaryDocuments,
        PathValues.CASE_CASE_ID_DOCUMENTS: CaseCaseIdDocuments,
        PathValues.CASE_CASE_ID_HEARINGS: CaseCaseIdHearings,
        PathValues.CASE_CASE_ID_JUDGES: CaseCaseIdJudges,
        PathValues.CASE_CASE_ID_PARTIES: CaseCaseIdParties,
        PathValues.CASE_CASE_ID_RELATED_CASES: CaseCaseIdRelatedCases,
        PathValues.CASE_COUNT_ANALYTICS_BY_AREA_OF_LAW: CaseCountAnalyticsByAreaOfLaw,
        PathValues.CASE_COUNT_ANALYTICS_BY_CASE_CLASS: CaseCountAnalyticsByCaseClass,
        PathValues.CASE_COUNT_ANALYTICS_BY_CASE_FILED_DATE: CaseCountAnalyticsByCaseFiledDate,
        PathValues.CASE_COUNT_ANALYTICS_BY_CASE_TYPE: CaseCountAnalyticsByCaseType,
        PathValues.CASE_COUNT_ANALYTICS_BY_CASE_TYPE_GROUP: CaseCountAnalyticsByCaseTypeGroup,
        PathValues.CASE_COUNT_ANALYTICS_BY_COURT: CaseCountAnalyticsByCourt,
        PathValues.CASE_COUNT_ANALYTICS_BY_COURT_LOCATION: CaseCountAnalyticsByCourtLocation,
        PathValues.CASE_COUNT_ANALYTICS_BY_COURT_SYSTEM: CaseCountAnalyticsByCourtSystem,
        PathValues.CASE_COUNT_ANALYTICS_BY_COURT_TYPE: CaseCountAnalyticsByCourtType,
        PathValues.CASE_COUNT_ANALYTICS_BY_JURISDICTION_GEO: CaseCountAnalyticsByJurisdictionGeo,
        PathValues.CASE_COUNT_ANALYTICS_BY_NORM_ATTORNEY: CaseCountAnalyticsByNormAttorney,
        PathValues.CASE_COUNT_ANALYTICS_BY_NORM_JUDGE: CaseCountAnalyticsByNormJudge,
        PathValues.CASE_COUNT_ANALYTICS_BY_NORM_LAW_FIRM: CaseCountAnalyticsByNormLawFirm,
        PathValues.CASE_COUNT_ANALYTICS_BY_NORM_PARTY: CaseCountAnalyticsByNormParty,
        PathValues.CASE_COUNT_ANALYTICS_BY_PARTY_ROLE: CaseCountAnalyticsByPartyRole,
        PathValues.CASE_COUNT_ANALYTICS_BY_PARTY_ROLE_GROUP: CaseCountAnalyticsByPartyRoleGroup,
        PathValues.CASE_DOCUMENT_CASE_DOCUMENT_ID: CaseDocumentCaseDocumentId,
        PathValues.CASE_DOCUMENT_DOWNLOAD_CASE_DOCUMENT_ID: CaseDocumentDownloadCaseDocumentId,
        PathValues.CASE_DOCUMENT_ORDER: CaseDocumentOrder,
        PathValues.CASE_DOCUMENT_ORDER_CALLBACKS: CaseDocumentOrderCallbacks,
        PathValues.CASE_DOCUMENT_ORDER_CALLBACKS_CASE_DOCUMENT_ORDER_CALLBACK_ID: CaseDocumentOrderCallbacksCaseDocumentOrderCallbackId,
        PathValues.CASE_EXPORT_CALLBACKS: CaseExportCallbacks,
        PathValues.CASE_EXPORT_CALLBACKS_CASE_EXPORT_CALLBACK_ID: CaseExportCallbacksCaseExportCallbackId,
        PathValues.CASE_EXPORT_CASE_ID: CaseExportCaseId,
        PathValues.CASE_SEARCH: CaseSearch,
        PathValues.CASE_SEARCH_CASE_SEARCH_ID: CaseSearchCaseSearchId,
        PathValues.CASE_TRACK: CaseTrack,
        PathValues.CASE_TRACK_CASE_ID: CaseTrackCaseId,
        PathValues.CASE_TRACKS: CaseTracks,
        PathValues.CASE_UPDATE: CaseUpdate,
        PathValues.CASE_UPDATE_CASE_ID: CaseUpdateCaseId,
        PathValues.CASE_UPDATES: CaseUpdates,
        PathValues.COURT_COVERAGE_COURT_ID: CourtCoverageCourtId,
        PathValues.DAILY_USAGE_DATE: DailyUsageDate,
        PathValues.GENERATE_NEW_TOKEN: GenerateNewToken,
        PathValues.INVALIDATE_ALL_TOKENS: InvalidateAllTokens,
        PathValues.INVALIDATE_TOKEN: InvalidateToken,
        PathValues.JUDGE_JUDGE_ID: JudgeJudgeId,
        PathValues.LIST_ALL_TOKEN_IDS: ListAllTokenIds,
        PathValues.MASTER_DATA_AREA_OF_LAW: MasterDataAreaOfLaw,
        PathValues.MASTER_DATA_AREA_OF_LAW_AREA_OF_LAW_ID: MasterDataAreaOfLawAreaOfLawId,
        PathValues.MASTER_DATA_ATTORNEY_REPRESENTATION_TYPE: MasterDataAttorneyRepresentationType,
        PathValues.MASTER_DATA_ATTORNEY_REPRESENTATION_TYPE_ATTORNEY_REPRESENTATION_TYPE_ID: MasterDataAttorneyRepresentationTypeAttorneyRepresentationTypeId,
        PathValues.MASTER_DATA_ATTORNEY_TYPE: MasterDataAttorneyType,
        PathValues.MASTER_DATA_ATTORNEY_TYPE_ATTORNEY_TYPE_ID: MasterDataAttorneyTypeAttorneyTypeId,
        PathValues.MASTER_DATA_CASE_CLASS: MasterDataCaseClass,
        PathValues.MASTER_DATA_CASE_CLASS_CASE_CLASS_ID: MasterDataCaseClassCaseClassId,
        PathValues.MASTER_DATA_CASE_RELATIONSHIP_TYPE: MasterDataCaseRelationshipType,
        PathValues.MASTER_DATA_CASE_RELATIONSHIP_TYPE_CASE_RELATIONSHIP_TYPE_ID: MasterDataCaseRelationshipTypeCaseRelationshipTypeId,
        PathValues.MASTER_DATA_CASE_STATUS: MasterDataCaseStatus,
        PathValues.MASTER_DATA_CASE_STATUS_CASE_STATUS_ID: MasterDataCaseStatusCaseStatusId,
        PathValues.MASTER_DATA_CASE_STATUS_GROUP: MasterDataCaseStatusGroup,
        PathValues.MASTER_DATA_CASE_STATUS_GROUP_CASE_STATUS_GROUP_ID: MasterDataCaseStatusGroupCaseStatusGroupId,
        PathValues.MASTER_DATA_CASE_TYPE: MasterDataCaseType,
        PathValues.MASTER_DATA_CASE_TYPE_CASE_TYPE_ID: MasterDataCaseTypeCaseTypeId,
        PathValues.MASTER_DATA_CASE_TYPE_GROUP: MasterDataCaseTypeGroup,
        PathValues.MASTER_DATA_CASE_TYPE_GROUP_CASE_TYPE_GROUP_ID: MasterDataCaseTypeGroupCaseTypeGroupId,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION: MasterDataCauseOfAction,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_CAUSE_OF_ACTION_ID: MasterDataCauseOfActionCauseOfActionId,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_ADDITIONAL_DATA: MasterDataCauseOfActionAdditionalData,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_ADDITIONAL_DATA_CAUSE_OF_ACTION_ADDITIONAL_DATA_ID: MasterDataCauseOfActionAdditionalDataCauseOfActionAdditionalDataId,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_GROUP: MasterDataCauseOfActionGroup,
        PathValues.MASTER_DATA_CAUSE_OF_ACTION_GROUP_CAUSE_OF_ACTION_GROUP_ID: MasterDataCauseOfActionGroupCauseOfActionGroupId,
        PathValues.MASTER_DATA_CHARGE: MasterDataCharge,
        PathValues.MASTER_DATA_CHARGE_CHARGE_ID: MasterDataChargeChargeId,
        PathValues.MASTER_DATA_CHARGE_ADDITIONAL_DATA: MasterDataChargeAdditionalData,
        PathValues.MASTER_DATA_CHARGE_ADDITIONAL_DATA_CHARGE_ADDITIONAL_DATA_ID: MasterDataChargeAdditionalDataChargeAdditionalDataId,
        PathValues.MASTER_DATA_CHARGE_DEGREE: MasterDataChargeDegree,
        PathValues.MASTER_DATA_CHARGE_DEGREE_CHARGE_DEGREE_ID: MasterDataChargeDegreeChargeDegreeId,
        PathValues.MASTER_DATA_CHARGE_GROUP: MasterDataChargeGroup,
        PathValues.MASTER_DATA_CHARGE_GROUP_CHARGE_GROUP_ID: MasterDataChargeGroupChargeGroupId,
        PathValues.MASTER_DATA_CHARGE_SEVERITY: MasterDataChargeSeverity,
        PathValues.MASTER_DATA_CHARGE_SEVERITY_CHARGE_SEVERITY_ID: MasterDataChargeSeverityChargeSeverityId,
        PathValues.MASTER_DATA_COURT: MasterDataCourt,
        PathValues.MASTER_DATA_COURT_COURT_ID: MasterDataCourtCourtId,
        PathValues.MASTER_DATA_COURT_COURT_ID_APPEAL_COURTS: MasterDataCourtCourtIdAppealCourts,
        PathValues.MASTER_DATA_COURT_COURT_ID_COURT_LOCATIONS: MasterDataCourtCourtIdCourtLocations,
        PathValues.MASTER_DATA_COURT_COURT_ID_JURISDICTION_GEO: MasterDataCourtCourtIdJurisdictionGeo,
        PathValues.MASTER_DATA_COURT_LOCATION: MasterDataCourtLocation,
        PathValues.MASTER_DATA_COURT_LOCATION_COURT_LOCATION_ID: MasterDataCourtLocationCourtLocationId,
        PathValues.MASTER_DATA_COURT_LOCATION_COURT_LOCATION_ID_COURTS: MasterDataCourtLocationCourtLocationIdCourts,
        PathValues.MASTER_DATA_COURT_SERVICE_STATUS: MasterDataCourtServiceStatus,
        PathValues.MASTER_DATA_COURT_SERVICE_STATUS_COURT_SERVICE_STATUS_ID: MasterDataCourtServiceStatusCourtServiceStatusId,
        PathValues.MASTER_DATA_COURT_SYSTEM: MasterDataCourtSystem,
        PathValues.MASTER_DATA_COURT_SYSTEM_COURT_SYSTEM_ID: MasterDataCourtSystemCourtSystemId,
        PathValues.MASTER_DATA_COURT_TYPE: MasterDataCourtType,
        PathValues.MASTER_DATA_COURT_TYPE_COURT_TYPE_ID: MasterDataCourtTypeCourtTypeId,
        PathValues.MASTER_DATA_JUDGE_TYPE: MasterDataJudgeType,
        PathValues.MASTER_DATA_JUDGE_TYPE_JUDGE_TYPE_ID: MasterDataJudgeTypeJudgeTypeId,
        PathValues.MASTER_DATA_JURISDICTION_GEO: MasterDataJurisdictionGeo,
        PathValues.MASTER_DATA_JURISDICTION_GEO_JURISDICTION_GEO_ID: MasterDataJurisdictionGeoJurisdictionGeoId,
        PathValues.MASTER_DATA_JURISDICTION_GEO_JURISDICTION_GEO_ID_COURTS: MasterDataJurisdictionGeoJurisdictionGeoIdCourts,
        PathValues.MASTER_DATA_PARTY_ROLE: MasterDataPartyRole,
        PathValues.MASTER_DATA_PARTY_ROLE_PARTY_ROLE_ID: MasterDataPartyRolePartyRoleId,
        PathValues.MASTER_DATA_PARTY_ROLE_GROUP: MasterDataPartyRoleGroup,
        PathValues.MASTER_DATA_PARTY_ROLE_GROUP_PARTY_ROLE_GROUP_ID: MasterDataPartyRoleGroupPartyRoleGroupId,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID: NormAttorneyNormAttorneyId,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID_ASSOCIATED_NORM_JUDGES: NormAttorneyNormAttorneyIdAssociatedNormJudges,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID_ASSOCIATED_NORM_LAW_FIRMS: NormAttorneyNormAttorneyIdAssociatedNormLawFirms,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID_ASSOCIATED_NORM_PARTIES: NormAttorneyNormAttorneyIdAssociatedNormParties,
        PathValues.NORM_ATTORNEY_NORM_ATTORNEY_ID_CASE_COUNT_ANALYTICS_BY_OPPOSING_NORM_ATTORNEY: NormAttorneyNormAttorneyIdCaseCountAnalyticsByOpposingNormAttorney,
        PathValues.NORM_ATTORNEY_SEARCH: NormAttorneySearch,
        PathValues.NORM_ATTORNEY_SEARCH_NORM_ATTORNEY_SEARCH_ID: NormAttorneySearchNormAttorneySearchId,
        PathValues.NORM_JUDGE_NORM_JUDGE_ID: NormJudgeNormJudgeId,
        PathValues.NORM_JUDGE_NORM_JUDGE_ID_ASSOCIATED_NORM_ATTORNEYS: NormJudgeNormJudgeIdAssociatedNormAttorneys,
        PathValues.NORM_JUDGE_NORM_JUDGE_ID_ASSOCIATED_NORM_LAW_FIRMS: NormJudgeNormJudgeIdAssociatedNormLawFirms,
        PathValues.NORM_JUDGE_NORM_JUDGE_ID_ASSOCIATED_NORM_PARTIES: NormJudgeNormJudgeIdAssociatedNormParties,
        PathValues.NORM_JUDGE_SEARCH: NormJudgeSearch,
        PathValues.NORM_JUDGE_SEARCH_NORM_JUDGE_SEARCH_ID: NormJudgeSearchNormJudgeSearchId,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID: NormLawFirmNormLawFirmId,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID_ASSOCIATED_NORM_ATTORNEYS: NormLawFirmNormLawFirmIdAssociatedNormAttorneys,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID_ASSOCIATED_NORM_JUDGES: NormLawFirmNormLawFirmIdAssociatedNormJudges,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID_ASSOCIATED_NORM_PARTIES: NormLawFirmNormLawFirmIdAssociatedNormParties,
        PathValues.NORM_LAW_FIRM_NORM_LAW_FIRM_ID_CASE_COUNT_ANALYTICS_BY_OPPOSING_NORM_LAW_FIRM: NormLawFirmNormLawFirmIdCaseCountAnalyticsByOpposingNormLawFirm,
        PathValues.NORM_LAW_FIRM_SEARCH: NormLawFirmSearch,
        PathValues.NORM_LAW_FIRM_SEARCH_NORM_LAW_FIRM_SEARCH_ID: NormLawFirmSearchNormLawFirmSearchId,
        PathValues.NORM_PARTY_NORM_PARTY_ID: NormPartyNormPartyId,
        PathValues.NORM_PARTY_NORM_PARTY_ID_ASSOCIATED_NORM_ATTORNEYS: NormPartyNormPartyIdAssociatedNormAttorneys,
        PathValues.NORM_PARTY_NORM_PARTY_ID_ASSOCIATED_NORM_JUDGES: NormPartyNormPartyIdAssociatedNormJudges,
        PathValues.NORM_PARTY_NORM_PARTY_ID_ASSOCIATED_NORM_LAW_FIRMS: NormPartyNormPartyIdAssociatedNormLawFirms,
        PathValues.NORM_PARTY_NORM_PARTY_ID_CASE_COUNT_ANALYTICS_BY_OPPOSING_NORM_PARTY: NormPartyNormPartyIdCaseCountAnalyticsByOpposingNormParty,
        PathValues.NORM_PARTY_SEARCH: NormPartySearch,
        PathValues.NORM_PARTY_SEARCH_NORM_PARTY_SEARCH_ID: NormPartySearchNormPartySearchId,
        PathValues.PACER_IMPORT_CASE_BY_COURT_USING_CASE_NUMBER: PacerImportCaseByCourtUsingCaseNumber,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_ALL_COURTS: PacerCaseLocatorCaseSearchAllCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_APPEAL_COURTS: PacerCaseLocatorCaseSearchAppealCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_BANKRUPTCY_COURTS: PacerCaseLocatorCaseSearchBankruptcyCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_CIVIL_COURTS: PacerCaseLocatorCaseSearchCivilCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_CRIMINAL_COURTS: PacerCaseLocatorCaseSearchCriminalCourts,
        PathValues.PACER_CASE_LOCATOR_CASE_SEARCH_MULTI_DISTRICT_COURTS: PacerCaseLocatorCaseSearchMultiDistrictCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_ALL_COURTS: PacerCaseLocatorPartySearchAllCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_APPEAL_COURTS: PacerCaseLocatorPartySearchAppealCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_BANKRUPTCY_COURTS: PacerCaseLocatorPartySearchBankruptcyCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_CIVIL_COURTS: PacerCaseLocatorPartySearchCivilCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_CRIMINAL_COURTS: PacerCaseLocatorPartySearchCriminalCourts,
        PathValues.PACER_CASE_LOCATOR_PARTY_SEARCH_MULTI_DISTRICT_COURTS: PacerCaseLocatorPartySearchMultiDistrictCourts,
        PathValues.PACER_CREDENTIAL: PacerCredential,
        PathValues.PACER_CREDENTIAL_PACER_USER_ID: PacerCredentialPacerUserId,
        PathValues.PARTY_PARTY_ID: PartyPartyId,
        PathValues.PARTY_PARTY_ID_ASSOCIATED_ATTORNEYS: PartyPartyIdAssociatedAttorneys,
    }
)
