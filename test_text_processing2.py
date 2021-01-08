# -*- coding: utf8 -*-

import unittest
import random
import basic_math as bm


class TestTextProcessing(unittest.TestCase):
    def test_digits_to_words(self):
        test_str = ""
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "")

        test_str = "Zip Code: 19104"
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "one nine one zero four")

        test_str = "Pi is 3.1415..."
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "three one four one five")

        test_str = "There are 3 jellies."
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "three")

        test_str = "Your room number is 205."
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "two zero five")

        test_str = "1588-1588"
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "one five eight eight one five eight eight")

        test_str = "My number: 010-1234-5678"
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "zero one zero one two three four five six seven eight")

        test_str = "No digits"
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "")

        test_str = "No digits here too!?$%"
        pred = bm.digits_to_words(test_str)
        self.assertEqual(pred, "")

    def test_to_camel_case(self):
        test_str = "to_camel_case"
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "toCamelCase")

        test_str = "__EXAMPLE__NAME__"
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "exampleName")

        test_str = "alreadyCamel"
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "alreadycamel")

        test_str = "_______"
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "")

        test_str = ""
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "")

        test_str = "not_Camel_Yet"
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "notCamelYet")

        test_str = "NOT_CAMEL_Yet"
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "notCamelYet")

        test_str = "abc_def_ghi"
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "abcDefGhi")

        test_str = "     "
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, "     ")

        test_str = "....."
        pred = bm.to_camel_case(test_str)
        self.assertEqual(pred, ".....")
