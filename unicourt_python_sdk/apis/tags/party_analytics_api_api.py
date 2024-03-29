# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from unicourt_python_sdk.paths.norm_party_norm_party_id_associated_norm_attorneys.get import GetAssociatedNormAttorneys
from unicourt_python_sdk.paths.norm_party_norm_party_id.get import GetNormPartyDetails
from unicourt_python_sdk.paths.norm_party_search_norm_party_search_id.get import GetNormPartySearchResultsById
from unicourt_python_sdk.paths.norm_party_norm_party_id_associated_norm_law_firms.get import ListAssociatedNormLawFirms
from unicourt_python_sdk.paths.norm_party_norm_party_id_associated_norm_judges.get import ListJudgesAssociatedWithNormParty
from unicourt_python_sdk.paths.norm_party_search.get import SearchNormParties
from unicourt_python_sdk.apis.tags.party_analytics_api_api_raw import PartyAnalyticsAPIApiRaw


class PartyAnalyticsAPIApi(
    GetAssociatedNormAttorneys,
    GetNormPartyDetails,
    GetNormPartySearchResultsById,
    ListAssociatedNormLawFirms,
    ListJudgesAssociatedWithNormParty,
    SearchNormParties,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PartyAnalyticsAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PartyAnalyticsAPIApiRaw(api_client)
