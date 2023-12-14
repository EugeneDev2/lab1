# src/unittest/python/utils/test_string_operations.py

from unittest import TestCase
from src.main.python.utils.string_operations import StringOperations

class TestStringOperations(TestCase):

    def test_capitalize_first_letter(self):
        result = StringOperations.capitalize_first_letter("hello")
        self.assertEqual(result, "Hello")

    def test_add_strings(self):
        result = StringOperations.add_strings("Hello", " World")
        self.assertEqual(result, "Hello World")

    def test_subtract_strings(self):
        result = StringOperations.subtract_strings("Hello World", "Hello")
        self.assertEqual(result, " World")

    def test_string_length(self):
        result = StringOperations.string_length("Hello")
        self.assertEqual(result, 5)

    def test_join_strings(self):
        result = StringOperations.join_strings(["Hello", " ", "World"])
        self.assertEqual(result, "Hello World")

    def test_repeat_string(self):
        result = StringOperations.repeat_string("Hello", 3)
        self.assertEqual(result, "HelloHelloHello")
