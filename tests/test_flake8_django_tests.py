#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `flake8_django_tests` package."""


import unittest

from flake8_django_tests.flake8_django_tests import check_compliance


class TestFlake8_django_tests(unittest.TestCase):

    def test_docstring_is_compliant_if_none(self):
        """Non-existent doc strings are compliant"""
        self.assertTrue(check_compliance(None))

    def test_docstring_is_noncompliant_if_startswith_test(self):
        """Doc string is non-compliant if it starts with Test"""
        self.assertFalse(check_compliance("Test that....."))

    def test_docstring_is_noncompliant_if_startswith_ensure(self):
        """Doc string is non-compliant if it starts with ensure"""
        self.assertFalse(check_compliance("ensure that....."))
