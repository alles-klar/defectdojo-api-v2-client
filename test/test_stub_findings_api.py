# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.stub_findings_api import StubFindingsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestStubFindingsApi(unittest.TestCase):
    """StubFindingsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.stub_findings_api.StubFindingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_stub_findings_create(self):
        """Test case for stub_findings_create

        """
        pass

    def test_stub_findings_list(self):
        """Test case for stub_findings_list

        """
        pass

    def test_stub_findings_partial_update(self):
        """Test case for stub_findings_partial_update

        """
        pass

    def test_stub_findings_read(self):
        """Test case for stub_findings_read

        """
        pass

    def test_stub_findings_update(self):
        """Test case for stub_findings_update

        """
        pass


if __name__ == '__main__':
    unittest.main()