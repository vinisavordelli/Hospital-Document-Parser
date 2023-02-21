from src.document_parsers.generic_parser import GenericParser
import re


class PrescriptionParser(GenericParser):
    def __init__(self, text):
        self.text = text

    def get_doctor_info(self):
        return self.get_from_text("Dr(.*)Name", re.DOTALL)

    def get_patient_name(self):
        return self.get_from_text("Name:(.*)Date")

    def get_address(self):
        return self.get_from_text("Address:(.*)")

    def get_prescription(self):
        return self.get_from_text(
            "Address[^\n]*(.*)Directions", flags=re.DOTALL
        )

    def get_directions(self):
        return self.get_from_text("Directions:(.*)Refill", flags=re.DOTALL)

    def get_refill(self):
        return self.get_from_text("Refill:(.*)")

    def parse(self):
        return {
            "Doctor Info": self.get_doctor_info(),
            "Patient Name": self.get_patient_name(),
            "Address": self.get_address(),
            "Prescription": self.get_prescription(),
            "Directions": self.get_directions(),
            "Refill": self.get_refill(),
        }


if __name__ == "__main__":
    test = """Dr John Smith, M.D

2 Non-Important Street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 meg

 
   

Directions: Use two tablets daily for three months

Refill: 3 times"""
    pp = PrescriptionParser(test)
    print(pp.get_address())
