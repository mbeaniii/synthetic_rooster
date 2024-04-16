class StrToInt:
    def __init__(self, data):
        self.char_to_int, self.int_to_char = self._create_char_encoding(data)
        self.encoded_data = self.encode_data(data)
        self.max_length = max(len(s) for s in data)  # To use in the model input shape

    def _create_char_encoding(self, data):
        unique_chars = set(''.join(data))
        char_to_int = {char: i+1 for i, char in enumerate(unique_chars)}  # Start from 1; reserve 0 for padding
        int_to_char = {i: char for char, i in char_to_int.items()}
        return char_to_int, int_to_char

    def encode_data(self, data):
        encoded_data = [[self.char_to_int[char] for char in string] for string in data]
        return encoded_data

    def decode_data(self, encoded_data):
        return [''.join(self.int_to_char[i] for i in string if i != 0) for string in encoded_data]
    