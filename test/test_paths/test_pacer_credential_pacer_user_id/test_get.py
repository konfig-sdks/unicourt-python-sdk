# coding: utf-8

"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button> 

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import unicourt_python_sdk
from unicourt_python_sdk.paths.pacer_credential_pacer_user_id import get
from unicourt_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPacerCredentialPacerUserId(ApiTestMixin, unittest.TestCase):
    """
    PacerCredentialPacerUserId unit test stubs
        Get Pacer Credential for a requested pacer User Id.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
