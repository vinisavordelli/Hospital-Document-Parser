import abc
import re


class generic_parser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text

    def get_from_text(self, pattern, text, flags=0):
        return re.findall(pattern, text, flags)[0].strip()

    @abc.abstractmethod
    def parse(self):
        # Parse the document
        # Return a list of tuples (word, count)
        pass
