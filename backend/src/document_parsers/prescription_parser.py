from src.document_parsers.generic_parser import GenericParser


class PrescriptionParser(GenericParser):
    def __init__(self, text):
        self.text = text
        self.patterns = {
            "doctor_info": r"Dr(.*)Name",
            "patient_name": r"Name:(.*)Date",
            "address": r"Address:(.*)",
            "prescription": r"Address[^\n]*(.*)Directions",
            "directions": r"Directions:(.*)Refill",
            "refill": r"Refill:(.*)",
        }

    def parse(self):
        return {
            "doctor_info": self.get_from_text(self.patterns["doctor_info"], 1),
            "patient_name": self.get_from_text(self.patterns["patient_name"]),
            "address": self.get_from_text(self.patterns["address"]),
            "prescription": self.get_from_text(
                self.patterns["prescription"], 1
            ),
            "directions": self.get_from_text(self.patterns["directions"], 1),
            "refill": self.get_from_text(self.patterns["refill"]),
        }


if __name__ == "__main__":
    test = """"""
    pp = PrescriptionParser(test)
    print(pp.parse())
