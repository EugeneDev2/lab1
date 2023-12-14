# src/main/python/utils/string_operations.py

class StringOperations:

    @staticmethod
    def capitalize_first_letter(s):
        return s.capitalize()

    @staticmethod
    def add_strings(str1, str2):
        return str1 + str2

    @staticmethod
    def subtract_strings(str1, str2):
        # Assuming str2 is always shorter or equal in length to str1
        return str1[len(str2):]

    @staticmethod
    def string_length(s):
        return len(s)

    @staticmethod
    def join_strings(strings):
        return ''.join(strings)

    @staticmethod
    def repeat_string(s, n):
        return s * n
