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
from unicourt_python_sdk.paths.master_data_court_service_status import get
from unicourt_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestMasterDataCourtServiceStatus(ApiTestMixin, unittest.TestCase):
    """
    MasterDataCourtServiceStatus unit test stubs
        Court Service Status Object.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
