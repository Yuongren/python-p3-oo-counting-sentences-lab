#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        # Ensure the initial value is a string; otherwise, default to an empty string
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ''
        else:
            self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # Print error message if the new value is not a string
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        """
        Counts the number of sentences in the string.
        A sentence is defined as text ending with '.', '!', or '?'.
        """
        sentences = re.split(r'[.!?]', self._value)
        non_empty_sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(non_empty_sentences)

