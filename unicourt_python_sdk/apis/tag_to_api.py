import typing_extensions

from unicourt_python_sdk.apis.tags import TagValues
from unicourt_python_sdk.apis.tags.court_standards_api_api import CourtStandardsAPIApi
from unicourt_python_sdk.apis.tags.case_analytics_api_api import CaseAnalyticsAPIApi
from unicourt_python_sdk.apis.tags.case_docket_api_api import CaseDocketAPIApi
from unicourt_python_sdk.apis.tags.pacerapi_api import PACERAPIApi
from unicourt_python_sdk.apis.tags.case_documents_api_api import CaseDocumentsAPIApi
from unicourt_python_sdk.apis.tags.attorney_analytics_api_api import AttorneyAnalyticsAPIApi
from unicourt_python_sdk.apis.tags.law_firm_analytics_api_api import LawFirmAnalyticsAPIApi
from unicourt_python_sdk.apis.tags.judge_analytics_api_api import JudgeAnalyticsAPIApi
from unicourt_python_sdk.apis.tags.party_analytics_api_api import PartyAnalyticsAPIApi
from unicourt_python_sdk.apis.tags.authentication_api_api import AuthenticationAPIApi
from unicourt_python_sdk.apis.tags.case_tracking_api_api import CaseTrackingAPIApi
from unicourt_python_sdk.apis.tags.pacer_credential_api_api import PACERCredentialAPIApi
from unicourt_python_sdk.apis.tags.usage_api_api import UsageAPIApi
from unicourt_python_sdk.apis.tags.case_export_api_api import CaseExportAPIApi
from unicourt_python_sdk.apis.tags.case_update_api_api import CaseUpdateAPIApi
from unicourt_python_sdk.apis.tags.case_search_api_api import CaseSearchAPIApi
from unicourt_python_sdk.apis.tags.court_availability_api_api import CourtAvailabilityAPIApi
from unicourt_python_sdk.apis.tags.callback_api_api import CallbackAPIApi
from unicourt_python_sdk.apis.tags.webhook_api_api import WebhookAPIApi
from unicourt_python_sdk.apis.tags.company_data_api_api import CompanyDataAPIApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COURT_STANDARDS_API: CourtStandardsAPIApi,
        TagValues.CASE_ANALYTICS_API: CaseAnalyticsAPIApi,
        TagValues.CASE_DOCKET_API: CaseDocketAPIApi,
        TagValues.PACER_API: PACERAPIApi,
        TagValues.CASE_DOCUMENTS_API: CaseDocumentsAPIApi,
        TagValues.ATTORNEY_ANALYTICS_API: AttorneyAnalyticsAPIApi,
        TagValues.LAW_FIRM_ANALYTICS_API: LawFirmAnalyticsAPIApi,
        TagValues.JUDGE_ANALYTICS_API: JudgeAnalyticsAPIApi,
        TagValues.PARTY_ANALYTICS_API: PartyAnalyticsAPIApi,
        TagValues.AUTHENTICATION_API: AuthenticationAPIApi,
        TagValues.CASE_TRACKING_API: CaseTrackingAPIApi,
        TagValues.PACER_CREDENTIAL_API: PACERCredentialAPIApi,
        TagValues.USAGE_API: UsageAPIApi,
        TagValues.CASE_EXPORT_API: CaseExportAPIApi,
        TagValues.CASE_UPDATE_API: CaseUpdateAPIApi,
        TagValues.CASE_SEARCH_API: CaseSearchAPIApi,
        TagValues.COURT_AVAILABILITY_API: CourtAvailabilityAPIApi,
        TagValues.CALLBACK_API: CallbackAPIApi,
        TagValues.WEBHOOK_API: WebhookAPIApi,
        TagValues.COMPANY_DATA_API: CompanyDataAPIApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COURT_STANDARDS_API: CourtStandardsAPIApi,
        TagValues.CASE_ANALYTICS_API: CaseAnalyticsAPIApi,
        TagValues.CASE_DOCKET_API: CaseDocketAPIApi,
        TagValues.PACER_API: PACERAPIApi,
        TagValues.CASE_DOCUMENTS_API: CaseDocumentsAPIApi,
        TagValues.ATTORNEY_ANALYTICS_API: AttorneyAnalyticsAPIApi,
        TagValues.LAW_FIRM_ANALYTICS_API: LawFirmAnalyticsAPIApi,
        TagValues.JUDGE_ANALYTICS_API: JudgeAnalyticsAPIApi,
        TagValues.PARTY_ANALYTICS_API: PartyAnalyticsAPIApi,
        TagValues.AUTHENTICATION_API: AuthenticationAPIApi,
        TagValues.CASE_TRACKING_API: CaseTrackingAPIApi,
        TagValues.PACER_CREDENTIAL_API: PACERCredentialAPIApi,
        TagValues.USAGE_API: UsageAPIApi,
        TagValues.CASE_EXPORT_API: CaseExportAPIApi,
        TagValues.CASE_UPDATE_API: CaseUpdateAPIApi,
        TagValues.CASE_SEARCH_API: CaseSearchAPIApi,
        TagValues.COURT_AVAILABILITY_API: CourtAvailabilityAPIApi,
        TagValues.CALLBACK_API: CallbackAPIApi,
        TagValues.WEBHOOK_API: WebhookAPIApi,
        TagValues.COMPANY_DATA_API: CompanyDataAPIApi,
    }
)
