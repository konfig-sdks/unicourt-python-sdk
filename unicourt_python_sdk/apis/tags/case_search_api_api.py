# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from unicourt_python_sdk.paths.case_search_case_search_id.get import GetSearchResultsByCaseSearchId
from unicourt_python_sdk.paths.case_search.get import SearchByKeywordExpressions
from unicourt_python_sdk.apis.tags.case_search_api_api_raw import CaseSearchAPIApiRaw


class CaseSearchAPIApi(
    GetSearchResultsByCaseSearchId,
    SearchByKeywordExpressions,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CaseSearchAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CaseSearchAPIApiRaw(api_client)