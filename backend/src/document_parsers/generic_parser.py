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
            for line in result.split("\n"):
                line.strip()
                print(result)
                print(line)
                noise = [
                    *re.findall(
                        r"^[a-zA-Z]{1,2}\s?(?:\s|\n|[^a-zA-Z0-9])",
                        line,
                        re.DOTALL,
                    ),
                    *re.findall(r"^[a-zA-Z]{1,2}$", line, re.DOTALL),
                ]

                print(noise)
                for n in noise:
                    if n.lower() == "no":
                        continue
                    result = result.replace(n, "").strip()
            return re.sub("\n\n+", "\n", result)
        except IndexError:
            return "Not Found"

    @abc.abstractmethod
    def parse(self):
        pass
