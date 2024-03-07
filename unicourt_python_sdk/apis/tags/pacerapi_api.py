# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from unicourt_python_sdk.paths.pacer_import_case_by_court_using_case_number.get import ImportPacerCaseByCourtUsingCaseNumberGet
from unicourt_python_sdk.paths.pacer_case_locator_case_search_all_courts.get import SearchAllCourtsCases
from unicourt_python_sdk.paths.pacer_case_locator_party_search_all_courts.get import SearchAllCourtsCases0
from unicourt_python_sdk.paths.pacer_case_locator_case_search_appeal_courts.get import SearchAppealCourtsCases
from unicourt_python_sdk.paths.pacer_case_locator_party_search_appeal_courts.get import SearchAppealCourtsCases0
from unicourt_python_sdk.paths.pacer_case_locator_case_search_bankruptcy_courts.get import SearchBankruptcyCases
from unicourt_python_sdk.paths.pacer_case_locator_party_search_bankruptcy_courts.get import SearchBankruptcyCourts
from unicourt_python_sdk.paths.pacer_case_locator_case_search_civil_courts.get import SearchCivilCases
from unicourt_python_sdk.paths.pacer_case_locator_party_search_civil_courts.get import SearchCivilCasesInCourts
from unicourt_python_sdk.paths.pacer_case_locator_case_search_criminal_courts.get import SearchCriminalCases
from unicourt_python_sdk.paths.pacer_case_locator_party_search_criminal_courts.get import SearchCriminalCases0
from unicourt_python_sdk.paths.pacer_case_locator_case_search_multi_district_courts.get import SearchMultiDistrictCourtCases
from unicourt_python_sdk.paths.pacer_case_locator_party_search_multi_district_courts.get import SearchMultiDistrictCourtCases0
from unicourt_python_sdk.apis.tags.pacerapi_api_raw import PACERAPIApiRaw


class PACERAPIApi(
    ImportPacerCaseByCourtUsingCaseNumberGet,
    SearchAllCourtsCases,
    SearchAllCourtsCases0,
    SearchAppealCourtsCases,
    SearchAppealCourtsCases0,
    SearchBankruptcyCases,
    SearchBankruptcyCourts,
    SearchCivilCases,
    SearchCivilCasesInCourts,
    SearchCriminalCases,
    SearchCriminalCases0,
    SearchMultiDistrictCourtCases,
    SearchMultiDistrictCourtCases0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PACERAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PACERAPIApiRaw(api_client)
