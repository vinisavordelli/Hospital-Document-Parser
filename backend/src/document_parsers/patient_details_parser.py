from src.document_parsers.generic_parser import GenericParser


class PatientDetailsParser(GenericParser):
    def __init__(self, text):
        self.text = text
        self.patterns = {
            "issue_date": r"[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}",
            "patient_name": r"(?<=Birth Date\s).*?\s(?:(?!"
            + r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b)\S)+",
            "patient_birth_date": r"[a-zA-Z]{3}\s[0-1]?[1-9]\s[1-9]{4}",
            "patient_phone_number": r"\([1-9]{3}\)\s?.{7,8}",
            "patient_address": r"Weight.+?[\r\n](.*)Height",
            "patient_weight": r"Weight.+?\r?\n[^\r\n]+\s+(\S+)\r?\n",
            "patient_height": r"^.*Height.*?(\d{2,3})",
            "emergency_contact": r"(?:.mergency.)([\s\S]*?)"
            + r"(?=Gener.+ Medi.+ His.+ )",
            "chicken_pox": r"Meas.es:[^\n]*\n(?:.*\n)*?.*?\s?"
            + r"(IMMUNE|NOT IMMUNE)",
            "measles": r"Meas.es:[^\n]*\n(?:.*\n)*?.*?\s+.*?\s"
            + r"(IMMUNE|NOT IMMUNE)",
            "hepatitis_b_vaccitation": r"Hepa.+\?\s+\n?.+\s?.?\s?"
            + r"(Yes|yes|No|no|Positive|positive|Negative|negative)",
            "medical_problems": r"Medical Problems.*?\n(?:.*\n)*?.*?\s?"
            + r"(.*)(?:.ame o.)",
            "has_insurance": r".nsurance.+\?\s+\n?.+\s?.?\s?"
            + r"(Yes|yes|No|no|Positive|positive|Negative|negative)",
            "insurance_provider": r"(?:.ompany.)([\s\S\n]*?)(?=.o.icy)",
            "insurance_policy_number": r".o.icy.+:\s*(\d{10})",
            "allergies": r"(?:a..ergies.)([\s\S]*?)(?=.ist)",
            "regular_medications": r"(?:medica.ion\s?(?:\w+\s\w+.\s)?)"
            + r"([\s\S]*?)(?=\d)",
            "clinic_address": r"(?:regu.ar..\D+)(.+)(?=.xpiry .a.e)",
            "Expiry_date": r"(?:.xpiry .a.e.?)(.+)",
        }
        self.data = self.parse()

    def parse(self):
        return {
            "issue_date": self.get_from_text(self.patterns["issue_date"]),
            "patient_name": self.get_from_text(
                self.patterns["patient_name"], 1
            ),
            "patient_birth_date": self.get_from_text(
                self.patterns["patient_birth_date"], 1
            ),
            "patient_phone_number": self.get_from_text(
                self.patterns["patient_phone_number"], 1
            ),
            "patient_address": self.get_from_text(
                self.patterns["patient_address"], 1
            ),
            "patient_weight": self.get_from_text(
                self.patterns["patient_weight"], 1
            ),
            "patient_height": self.get_from_text(
                self.patterns["patient_height"], 1
            ),
            "emergency_contact": self.get_from_text(
                self.patterns["emergency_contact"], 1
            ),
            "chicken_pox": self.get_from_text(self.patterns["chicken_pox"], 1),
            "measles": self.get_from_text(self.patterns["measles"], 1),
            "hepatitis_b_vaccitation": self.get_from_text(
                self.patterns["hepatitis_b_vaccitation"], 1
            ),
            "medical_problems": self.get_from_text(
                self.patterns["medical_problems"], 1
            ),
            "has_insurance": self.get_from_text(
                self.patterns["has_insurance"], 1
            ),
            "insurance_provider": self.get_from_text(
                self.patterns["insurance_provider"], 1
            ),
            "insurance_policy_number": self.get_from_text(
                self.patterns["insurance_policy_number"], 1
            ),
            "allergies": self.get_from_text(self.patterns["allergies"], 1),
            "regular_medications": self.get_from_text(
                self.patterns["regular_medications"], 1
            ),
            "clinic_address": self.get_from_text(
                self.patterns["clinic_address"], 1
            ),
            "Expiry_date": self.get_from_text(self.patterns["Expiry_date"], 1),
        }


if __name__ == "__main__":
    test = """"""

    pd = PatientDetailsParser(test)
    print(pd.parse())
