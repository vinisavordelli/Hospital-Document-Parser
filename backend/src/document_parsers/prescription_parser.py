from generic_parser import generic_parser
import re


class PrescriptionParser(generic_parser):
    def __init__(self, text):
        self.text = text

    def get_doctor_info(self):
        return self.get_from_text("Dr(.*)Name", re.DOTALL)

    def get_patient_name(self):
        return self.get_from_text("Name:(.*)Date")

    def get_address(self):
        return self.get_from_text("Address[^\n]")

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
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 9/11/2022
Address: 9 tennis court, new Russia, DC
Prednisone 20 mig
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month >

Refill: 2 times"""
    pp = PrescriptionParser(test)
    print(pp.parse())
