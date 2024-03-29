# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from unicourt_python_sdk.paths.norm_law_firm_norm_law_firm_id_associated_norm_judges.get import GetAssociatedNormJudges
from unicourt_python_sdk.paths.norm_law_firm_norm_law_firm_id.get import GetNormLawFirmById
from unicourt_python_sdk.paths.norm_law_firm_search_norm_law_firm_search_id.get import GetNormLawFirmSearchResultById
from unicourt_python_sdk.paths.norm_law_firm_norm_law_firm_id_associated_norm_attorneys.get import ListAssociatedNormAttorneys
from unicourt_python_sdk.paths.norm_law_firm_norm_law_firm_id_associated_norm_parties.get import ListAssociatedNormParties
from unicourt_python_sdk.paths.norm_law_firm_search.get import SearchLawFirms
from unicourt_python_sdk.apis.tags.law_firm_analytics_api_api_raw import LawFirmAnalyticsAPIApiRaw


class LawFirmAnalyticsAPIApi(
    GetAssociatedNormJudges,
    GetNormLawFirmById,
    GetNormLawFirmSearchResultById,
    ListAssociatedNormAttorneys,
    ListAssociatedNormParties,
    SearchLawFirms,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LawFirmAnalyticsAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LawFirmAnalyticsAPIApiRaw(api_client)
