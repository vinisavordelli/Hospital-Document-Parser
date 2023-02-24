prescription_mock1 = """Dr John Smith, M.D
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

expected_output1 = {
    "doctor_info": "John Smith, M.D\n2 Non-Important Street,\nNew York, Phone (000)-111-2222",
    "patient_name": "Marta Sharapova",
    "address": "9 tennis court, new Russia, DC",
    "prescription": "K\n\n \n\nPrednisone 20 mg\nLialda 2.4 gram",
    "directions": "Prednisone, Taper 5 mg every 3 days,\n\nFinish in 2.45 weeks |\nLtalda - take 2 pill everyday for 1 month",
    "refill": "2 times",
}

prescription_mock2 = """Dr John Smith, M.D

2 Non-Important street,
New York, Phone (900)-221-2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

K

‘Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times"""

expected1 = {
    "doctor_info": "John Smith, M.D\n2 Non-Important Street,\nNew York, Phone (000)-111-2222",
    "patient_name": "Marta Sharapova",
    "address": "9 tennis court, new Russia, DC",
    "prescription": "Prednisone 20 mg\nLialda 2.4 gram",
    "directions": "Prednisone, Taper 5 mg every 3 days,\nFinish in 2.45 weeks |\nLtalda - take 2 pill everyday for 1 month",
    "refill": "2 times",
}

expected2 = {
    "doctor_info": "John Smith, M.D\n2 Non-Important street,\nNew York, Phone (900)-221-2222",
    "patient_name": "Virat Kohli",
    "address": "2 cricket blvd, New Delhi",
    "prescription": "‘Omeprazole 40 mg",
    "directions": "Use two tablets daily for three months",
    "refill": "3 times",
}

keys = expected1.keys()
expected3 = {}
for key in keys:
    expected3[key] = "Not Found"
