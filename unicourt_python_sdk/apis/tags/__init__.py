# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from unicourt_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    COURT_STANDARDS_API = "Court Standards API"
    CASE_ANALYTICS_API = "Case Analytics API"
    CASE_DOCKET_API = "Case Docket API"
    PACER_API = "PACER API"
    CASE_DOCUMENTS_API = "Case Documents API"
    ATTORNEY_ANALYTICS_API = "Attorney Analytics API"
    LAW_FIRM_ANALYTICS_API = "Law Firm Analytics API"
    JUDGE_ANALYTICS_API = "Judge Analytics API"
    PARTY_ANALYTICS_API = "Party Analytics API"
    AUTHENTICATION_API = "Authentication API"
    CASE_TRACKING_API = "Case Tracking API"
    PACER_CREDENTIAL_API = "PACER Credential API"
    USAGE_API = "Usage API"
    CASE_EXPORT_API = "Case Export API"
    CASE_UPDATE_API = "Case Update API"
    CASE_SEARCH_API = "Case Search API"
    COURT_AVAILABILITY_API = "Court Availability API"
    CALLBACK_API = "Callback API"
    WEBHOOK_API = "Webhook API"
    COMPANY_DATA_API = "Company Data API"
