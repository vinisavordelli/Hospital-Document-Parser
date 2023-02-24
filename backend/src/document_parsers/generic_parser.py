import abc
import re


class GenericParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text
        self.patterns = {}

    def get_from_text(self, pattern, reDotall=0):
        try:
            if reDotall:
                result = re.findall(pattern, self.text, re.DOTALL)[0].strip()
            else:
                result = re.findall(pattern, self.text, reDotall)[0].strip()
            return result
        except IndexError:
            return "Not Found"

    @abc.abstractmethod
    def parse(self):
        pass
