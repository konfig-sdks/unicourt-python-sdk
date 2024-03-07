# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from unicourt_python_sdk.paths.case_export_callbacks_case_export_callback_id.get import GetCallbackById
from unicourt_python_sdk.paths.case_export_callbacks.get import GetCallbackListForRequestedDate
from unicourt_python_sdk.paths.case_export_case_id.get import GetCaseExportByCaseId
from unicourt_python_sdk.apis.tags.case_export_api_api_raw import CaseExportAPIApiRaw


class CaseExportAPIApi(
    GetCallbackById,
    GetCallbackListForRequestedDate,
    GetCaseExportByCaseId,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CaseExportAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CaseExportAPIApiRaw(api_client)
