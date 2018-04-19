#!/usr/bin/env python
# encoding: utf-8


from unittest import TestCase

from virshdumpparser import parser


class CitellusTest(TestCase):
    def test(self):

        VXMLP = parser.VirshXMLParser('')
        assert VXMLP
