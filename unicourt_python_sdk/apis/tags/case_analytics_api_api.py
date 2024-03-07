# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from unicourt_python_sdk.paths.case_count_analytics_by_case_class.get import GetCaseCountAnalyticsByCaseClass
from unicourt_python_sdk.paths.case_count_analytics_by_case_filed_date.get import GetCaseCountAnalyticsByCaseFiledDate
from unicourt_python_sdk.paths.case_count_analytics_by_case_type_group.get import GetCaseCountAnalyticsByCaseTypeGroup
from unicourt_python_sdk.paths.case_count_analytics_by_court.get import GetCaseCountAnalyticsByCourt
from unicourt_python_sdk.paths.case_count_analytics_by_court_location.get import GetCaseCountAnalyticsByCourtLocation
from unicourt_python_sdk.paths.case_count_analytics_by_court_system.get import GetCaseCountAnalyticsByCourtSystem
from unicourt_python_sdk.paths.case_count_analytics_by_court_type.get import GetCaseCountAnalyticsByCourtType
from unicourt_python_sdk.paths.case_count_analytics_by_jurisdiction_geo.get import GetCaseCountAnalyticsByJurisdictionGeo
from unicourt_python_sdk.paths.case_count_analytics_by_norm_attorney.get import GetCaseCountAnalyticsByNormAttorney
from unicourt_python_sdk.paths.case_count_analytics_by_norm_judge.get import GetCaseCountAnalyticsByNormJudge
from unicourt_python_sdk.paths.case_count_analytics_by_norm_law_firm.get import GetCaseCountAnalyticsByNormLawFirm
from unicourt_python_sdk.paths.case_count_analytics_by_norm_party.get import GetCaseCountAnalyticsByNormParty
from unicourt_python_sdk.paths.norm_attorney_norm_attorney_id_case_count_analytics_by_opposing_norm_attorney.get import GetCaseCountAnalyticsByOpposingNormAttorneyForNormAttorney
from unicourt_python_sdk.paths.norm_law_firm_norm_law_firm_id_case_count_analytics_by_opposing_norm_law_firm.get import GetCaseCountAnalyticsByOpposingNormLawFirmForANormLawFirm
from unicourt_python_sdk.paths.norm_party_norm_party_id_case_count_analytics_by_opposing_norm_party.get import GetCaseCountAnalyticsByOpposingNormPartyForANormParty
from unicourt_python_sdk.paths.case_count_analytics_by_party_role.get import GetCaseCountAnalyticsByPartyRole
from unicourt_python_sdk.paths.case_count_analytics_by_party_role_group.get import GetCaseCountAnalyticsByPartyRoleGroup
from unicourt_python_sdk.paths.case_count_analytics_by_area_of_law.get import GetCaseCountByAreaOfLaw
from unicourt_python_sdk.paths.case_count_analytics_by_case_type.get import GetCaseCountByCaseType
from unicourt_python_sdk.apis.tags.case_analytics_api_api_raw import CaseAnalyticsAPIApiRaw


class CaseAnalyticsAPIApi(
    GetCaseCountAnalyticsByCaseClass,
    GetCaseCountAnalyticsByCaseFiledDate,
    GetCaseCountAnalyticsByCaseTypeGroup,
    GetCaseCountAnalyticsByCourt,
    GetCaseCountAnalyticsByCourtLocation,
    GetCaseCountAnalyticsByCourtSystem,
    GetCaseCountAnalyticsByCourtType,
    GetCaseCountAnalyticsByJurisdictionGeo,
    GetCaseCountAnalyticsByNormAttorney,
    GetCaseCountAnalyticsByNormJudge,
    GetCaseCountAnalyticsByNormLawFirm,
    GetCaseCountAnalyticsByNormParty,
    GetCaseCountAnalyticsByOpposingNormAttorneyForNormAttorney,
    GetCaseCountAnalyticsByOpposingNormLawFirmForANormLawFirm,
    GetCaseCountAnalyticsByOpposingNormPartyForANormParty,
    GetCaseCountAnalyticsByPartyRole,
    GetCaseCountAnalyticsByPartyRoleGroup,
    GetCaseCountByAreaOfLaw,
    GetCaseCountByCaseType,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CaseAnalyticsAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CaseAnalyticsAPIApiRaw(api_client)
