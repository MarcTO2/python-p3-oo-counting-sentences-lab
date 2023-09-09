import re
#!/usr/bin/env python3

class MyString:
    def __init__(self):
        self._value = ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        sentences = [s.strip() for s in re.split(r'[.!?]', self._value) if s.strip()]
        return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence()) 
print(string.is_question())  
print(string.is_exclamation())  
print(string.count_sentences())  

