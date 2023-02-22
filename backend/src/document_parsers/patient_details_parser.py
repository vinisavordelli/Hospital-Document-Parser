from generic_parser import GenericParser
import re


class PatientDetailsParser(GenericParser):
    def __init__(self, text):
        self.text = text

    def get_issue_date(self):
        return self.get_from_text(
            "^(.*)\n",
        )

    def get_patient_name(self):
        return re.sub(
            r"\s+\w+\s+\d{1,2}\s+\d{4}$",
            "",
            self.get_from_text(
                "Birth Date[\r\n]+([^\r\n]+)",
                flags=re.DOTALL,
            ),
        )

    def get_patient_birth_date(self):
        return self.get_from_text(
            "[a-zA-Z]{3}\s[0-1]?[1-9]\s[1-9]{4}",
        )

    def get_patient_phone_number(self):
        return self.get_from_text(
            "\([1-9]{3}\)\s?.{7,8}",
        )

    def get_patient_address(self):
        return self.get_from_text(
            "Weight.+?[\r\n](.*)Height",
            flags=re.DOTALL,
        )

    def get_patient_weight(self):
        return self.get_from_text(
            "Weight.+?\r?\n[^\r\n]+\s+(\S+)\r?\n",
            flags=re.DOTALL,
        )

    def get_patient_height(self):
        return self.get_from_text(
            "^.*Height.*?(\d{2,3})",
            flags=re.DOTALL,
        )

    def get_emergency_contact(self):
        return self.get_from_text(
            "Emergency[\s\S]*?(?=Gener.+ Medi.+ His.+ )",
            flags=re.DOTALL,
        )

    def get_chicken_pox(self):
        return self.get_from_text(
            "Meas.es:[^\n]*\n(?:.*\n)*?.*?\s?(IMMUNE|NOT IMMUNE)",
            flags=re.DOTALL,
        )

    def get_measles(self):
        return self.get_from_text(
            "Meas.es:[^\n]*\n(?:.*\n)*?.*?\s+.*?\s(IMMUNE|NOT IMMUNE)",
            flags=re.DOTALL,
        )

    def get_hepatitis_b_vaccination(self):
        return self.get_from_text(
            "Hepatitis B vaccination\?\s+(Yes|No)",
            flags=re.DOTALL,
        )

    def get_medical_problem(self):
        return self.get_from_text(
            "Medical Problems.*?\n(?:.*\n)*?.*?\s?(.*)",
            flags=re.DOTALL,
        )

    def parse(self):
        return {
            "issue_date": self.get_issue_date(),
            "patient_name": self.get_patient_name(),
            "patient_birth_date": self.get_patient_birth_date(),
            "patient_phone_number": self.get_patient_phone_number(),
            "patient_address": self.get_patient_address(),
            "patient_weight": self.get_patient_weight(),
            "patient_height": self.get_patient_height(),
            "emergency_contact": self.get_emergency_contact(),
            "chicken_pox": self.get_chicken_pox(),
            "measles": self.get_measles(),
            "hepatitis_b_vaccination": self.get_hepatitis_b_vaccination(),
            "medical_problem": self.get_medical_problem(),
        }


# Months = Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec
if __name__ == "__main__":
    test = """17/12/2020

 

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 ;

United States Height
190

 

 

In Casc of Emergency .
ee J
Simeone Crawford 9266 Ash Dr
H New York City, New York, 10005
ome phone United States
(990) 375-4621
Work phone
Genera! Medical History
i
Chicken Pox (Varicella): Measies:
NOT IMMUNE

NOT IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):

Migraine"""

    test2 = """17/12/2020

Patient Medical Record

Patient Information Birth Date
Jerry Lucas May 2 1998
(279) 920-8204 Weight:
4218 Wheeler Ridge Dr 57

ouited ee 14201 Height:

In Case of Emergency
meee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

 

Chicken Pox (Varicelia): Measles:

IMMUNE NOT IMMUNE
Have you had the Hepatitis B vaccination?
Yes |

List any Medical Problems (asthma, seizures, headaches):
N/A"""

    pd = PatientDetailsParser(test2)
    print(pd.parse())
