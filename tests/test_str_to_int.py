import pytest
from ..src.str_to_int import StrToInt

@pytest.fixture
def str_to_int_fixture():
    data = ['hello', 'world', 'python']
    return StrToInt(data)

class TestStrToInt:

    def test_char_to_int_mapping_assigns_unique_integer_to_each_character(self, str_to_int_fixture):
        char_to_int = str_to_int_fixture.char_to_int
        # Ensure all values are unique by checking the length of the set of values against the dictionary length
        unique_values = set(char_to_int.values())
        assert len(unique_values) == len(char_to_int), "Each character should be mapped to a unique integer."
        # Further check to ensure each character from the input data is in the char_to_int mapping
        all_input_chars = set(''.join(['hello', 'world', 'python']))
        assert all_input_chars == char_to_int.keys(), "Every character in the input data should have a unique integer assigned."

    def test_int_to_char_mapping_is_accurate_reverse_of_char_to_int_mapping(self, str_to_int_fixture):
        # Generate reverse mapping from the instance to ensure accuracy
        expected_mapping = {v: k for k, v in str_to_int_fixture.char_to_int.items()}
        assert str_to_int_fixture.int_to_char == expected_mapping, "Integer to character mapping should accurately reverse the character to integer mapping."

    def test_encoded_data_matches_lengths_of_original_strings(self, str_to_int_fixture):
        # Verify that the length of each encoded sequence matches the original string's length
        data = ['hello', 'world', 'python']
        expected_encoded = str_to_int_fixture.encoded_data
        for original, encoded in zip(data, expected_encoded):
            assert len(encoded) == len(original), "Encoded sequence length should match the original string length."

    def test_max_length_matches_longest_string_in_data_set(self, str_to_int_fixture):
        # Compute expected maximum length from the data
        data = ['hello', 'world', 'python']
        expected_max_length = max(len(word) for word in data)
        assert str_to_int_fixture.max_length == expected_max_length, "Maximum length should match the length of the longest string in the data set."

    def test_decoded_data_restores_original_strings(self, str_to_int_fixture):
        # Verify that decoding the encoded data restores the original strings
        expected_data = ['hello', 'world', 'python']
        decoded_data = str_to_int_fixture.decode_data(str_to_int_fixture.encoded_data)
        assert decoded_data == expected_data, "Decoded data should accurately restore the original strings from encoded data."