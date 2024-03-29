# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from unicourt_python_sdk.paths.generate_new_token.post import GenerateNewToken
from unicourt_python_sdk.paths.list_all_token_ids.put import GetAllTokenIds
from unicourt_python_sdk.paths.invalidate_token.put import InvalidateAccessToken
from unicourt_python_sdk.paths.invalidate_all_tokens.put import InvalidateAllTokens
from unicourt_python_sdk.apis.tags.authentication_api_api_raw import AuthenticationAPIApiRaw


class AuthenticationAPIApi(
    GenerateNewToken,
    GetAllTokenIds,
    InvalidateAccessToken,
    InvalidateAllTokens,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AuthenticationAPIApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AuthenticationAPIApiRaw(api_client)
