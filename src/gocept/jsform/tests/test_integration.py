# -*- coding: utf-8 -*-
import unittest
import fanstatic


class IntegrationTests(unittest.TestCase):

    def setUp(self):
        super(IntegrationTests, self).setUp()
        fanstatic.init_needed()

    def test_resources_are_all_available(self):
        from gocept.jsform import jsform
        jsform.need()
