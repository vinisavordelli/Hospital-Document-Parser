keys = [
    "issue_date",
    "patient_name",
    "patient_birth_date",
    "patient_phone_number",
    "patient_address",
    "patient_weight",
    "patient_height",
    "emergency_contact",
    "chicken_pox",
    "measles",
    "hepatitis_b_vaccitation",
    "medical_problems",
    "has_insurance",
    "insurance_provider",
    "insurance_policy_number",
    "allergies",
    "regular_medications",
    "clinic_address",
    "Expiry_date",
]


pd_mock1 = """
17/12/2020



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

Migraine






ff Name of Insurance Company:
fs Random insuarance Company
F . Policy Number:

7115207313

Do you have medical insurance?

Yes.

Medical Insurance Details

List any allergies:
Peanuts

List any medication taken regularly:

Triptans



4789 Bollinger Rd
Jersey City, New Jersey, 07030

Expiry Date:
30 December 2020"""

expected1 = {
    "issue_date": "17/12/2020",
    "patient_name": "Kathy Crawford",
    "patient_birth_date": "May 6 1972",
    "patient_phone_number": "(737) 988-0851",
    "patient_address": "9264 Ash Dr 95\nNew York City, 10005 '\nUnited States",
    "patient_weight": "95",
    "patient_height": "190",
    "emergency_contact": "Simeone Crawford 9266 Ash Dr\nNew York City, New York, 10005\nome phone United States\n(990) 375-4621\nWork phone",
    "chicken_pox": "IMMUNE",
    "measles": "IMMUNE",
    "hepatitis_b_vaccitation": "Yes",
    "medical_problems": "Migraine",
    "has_insurance": "Yes",
    "insurance_provider": "Random insuarance Company",
    "insurance_policy_number": "7115207313",
    "allergies": "Peanuts",
    "regular_medications": "Triptans",
    "clinic_address": "4789 Bollinger Rd\nJersey City, New Jersey, 07030",
    "Expiry_date": "30 December 2020",
}

pd_mock2 = """17/12/2020

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
N/A



_—

Name of Insurance Company:
Random Insuarance Company

Policy Number:
5638746258

Do you have medical insurance?

Yes

Medical Insurance Details

List any allergies:
N/A

List any medication taken regularly:

N/A

4218 Smeeler Ridge Dr
Buffalo, New York, 14206
United States

Expiry Date:
31 December 2020"""

expected2 = {
    "issue_date": "17/12/2020",
    "patient_name": "Jerry",
    "patient_birth_date": "May 2 1998",
    "patient_phone_number": "(279) 920-8204",
    "patient_address": "4218 Wheeler Ridge Dr 57\nBuffalo, New York, 14201",
    "patient_weight": "57",
    "patient_height": "170",
    "emergency_contact": "meee\nJoe Lucas 4218 Wheeler Ridge Dr\nBuffalo, New York, 14201\nHome phone . United States\nWork phone",
    "chicken_pox": "IMMUNE",
    "measles": "NOT IMMUNE",
    "hepatitis_b_vaccitation": "Yes",
    "medical_problems": "N/A\n_—",
    "has_insurance": "Yes",
    "insurance_provider": "Random Insuarance Company",
    "insurance_policy_number": "5638746258",
    "allergies": "N/A",
    "regular_medications": "N/A",
    "clinic_address": "4218 Smeeler Ridge Dr\nBuffalo, New York, 14206\nUnited States",
    "Expiry_date": "31 December 2020",
}

pd_mock3 = ""

expected3 = {}
for key in keys:
    expected3[key] = "Not Found"
