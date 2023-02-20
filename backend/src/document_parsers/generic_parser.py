import abc
import re


class GenericParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text

    def get_from_text(self, pattern, flags=0):
        return re.findall(pattern, self.text, flags)[0].strip()

    @abc.abstractmethod
    def parse(self):
        pass
