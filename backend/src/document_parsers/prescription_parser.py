from sr.document_parsers.generic_parser import GenericParser
import re


class PrescriptionParser(GenericParser):
    def __init__(self, text):
        self.text = text
        self.patterns = {
            "doctor_info": "Dr(.*)Name",
            "patient_name": "Name:(.*)Date",
            "address": "Address:(.*)",
            "prescription": "Address[^\n]*(.*)Directions",
            "directions": "Directions:(.*)Refill",
            "refill": "Refill:(.*)",
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
    test = """Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

 

Prednisone 20 mg
Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,

Finish in 2.45 weeks |
Ltalda - take 2 pill everyday for 1 month

Refill: 2 times"""
    pp = PrescriptionParser(test)
    print(pp.parse())
