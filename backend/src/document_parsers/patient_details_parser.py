from sr.document_parsers.generic_parser import GenericParser


class PatientDetailsParser(GenericParser):
    def __init__(self, text):
        self.text = text
        self.patterns = {
            "issue_date": "^(.*)\n",
            "patient_name": "Birth Date.*?\n(?:.*\n)*?(.+)(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)",
            "patient_birth_date": "[a-zA-Z]{3}\s[0-1]?[1-9]\s[1-9]{4}",
            "patient_phone_number": "\([1-9]{3}\)\s?.{7,8}",
            "patient_address": "Weight.+?[\r\n](.*)Height",
            "patient_weight": "Weight.+?\r?\n[^\r\n]+\s+(\S+)\r?\n",
            "patient_height": "^.*Height.*?(\d{2,3})",
            "emergency_contact": "(?<=Emergency\s..)[\s\S]*?(?=Gener.+ Medi.+ His.+ )",
            "chicken_pox": "Meas.es:[^\n]*\n(?:.*\n)*?.*?\s?(IMMUNE|NOT IMMUNE)",
            "measles": "Meas.es:[^\n]*\n(?:.*\n)*?.*?\s+.*?\s(IMMUNE|NOT IMMUNE)",
            "hepatitis_b_vaccitation": "Hepa.+\?\s+\n?.+\s?.?\s?(Yes|yes|No|no|Positive|positive|Negative|negative)",
            "medical_problems": "Medical Problems.*?\n(?:.*\n)*?.*?\s?(.*)",
        }

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
        }


# Months = Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec
if __name__ == "__main__":
    test = """17/12/2020

 

Patient Medical Record

 

 

Patient Information Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight’
9264 Ash Dr 95
New York City, 10005 '
United States Height:
190
In Casc of Emergency
a _
Simeone Crawford 9266 Ash Dr
H New York City, New York, 10005
ome phone United States
(990) 375-4621
Work phone
Genera! Medical History
LT

nn
ch LT a

Chicken Pox (Varicella): Measies:

IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):

Migraine"""

    test2 = """17/12/2020

Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 . Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gn
170

In Case of Emergency
meee

Joe Lucas 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone . United States
Work phone

General Medical History

 

Chicken Pox (Varicelia): Measles:

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

_ Yes

List any Medical Problems (asthma, seizures, headaches):
N/A"""

    pd = PatientDetailsParser(test2)
    print(pd.parse())
