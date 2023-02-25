# Hospital Documents Processing / Processamento de Documentos de Hospitais

## For an english readme, click the dropbox below

<details>
<Summary><h2>What does it do?</h3></Summary>

This project aims to simulate a hospital program that receives images and pdf files from photos their patient's or an employee sends them.

Let's assume 2 test cases, one for a prescription and one for a form with the patient's information.

The prescription should look like this:

![pre_1](https://user-images.githubusercontent.com/77638347/221332475-7632bb62-4f37-415d-a0e5-bf4170273b2f.jpg)

The output should be something like this:

```sh
{
    "doctor_info": "John Smith, M.D\n2 Non-Important Street,\nNew York, Phone (000)-111-2222",
    "patient_name": "Marta Sharapova",
    "address": "9 tennis court, new Russia, DC",
    "prescription": "Prednisone 20 mg\nLialda 2.4 gram",
    "directions": "Prednisone, Taper 5 mg every 3 days,\nFinish in 2.45 weeks |\nLtalda - take 2 pill everyday for 1 month",
    "refill": "2 times"
}
```

The patient details form should look like this:

![pd_1-1](https://user-images.githubusercontent.com/77638347/221332474-c256f5ef-0dfa-4111-94a0-ba6eaa1a23be.jpg)
![pd_1-2](https://user-images.githubusercontent.com/77638347/221332472-72ec8724-ac21-4f8a-b355-7988ee975d26.jpg))

And the result should be:

```sh
{
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
    "Expiry_date": "30 December 2020"
}
```

Keep in mind those keys could be more segmented, but it is just an idea.

<details>
<Summary>How does it Work?</Summary>

For a satisfactory result the process takes multiple steps:

1. The first step requires the user to provide the file path and the type of the document.
   This can be done by running the proper files or you can use one my scripts, which we will talk about later.

2. If the file is a pdf, the second step will be transforming this pdf into an image(or images).

3. With the images ready, the program will reprocess the image as it can have shadows, blurs and other things that can make it hard to read the image.
   The result from the prescription I showed earlier should look like this:
   ![processed_pre_1](https://user-images.githubusercontent.com/77638347/221332470-0c4b8e53-6743-43c6-9c0d-f5a513a6caab.png)

4. With that done, it's time to get the text from that image.

5. The information is not usefull as it is now, so we will arrange it in an object and remove any noise from it. As the result comes a little dirty like in the text below (taken from the patient details showed early)

```py
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
30 December 2020
```

6. Done, the Program Should have extracted all the useful data.

</details>

<details>
<Summary>How Can You test it?</Summary>
It is quite simple, first you need to clone this repository:

```sh
git clone git@github.com:vinisavordelli/Hospital-Document-Parser.git
```

After that, open the repository you just cloned.

```sh
code ./Hospital-Document-Parser
```

Install the necessery packages

```sh
make install
```

You're all set. I left three make commands ready

```sh
make test # Runs all project tests
make start #Starts the API in a localserver
make run #Starts the application through the terminal
```

Running the Project with `make run`:

![run](https://user-images.githubusercontent.com/77638347/221332468-e48ebe1d-bd1d-48c2-aab4-939ada9d1cd5.gif)

Using it with make start and postman:

![start](https://user-images.githubusercontent.com/77638347/221332466-6e601c6e-335c-4783-8109-35bd7890b79b.gif)

</details>
