import os

from extractor import extact_info

print(
    """
    Welcome to My Project\n\n

    It's goal is to make a hospital system where you can upload your medical
    documents and the program returns the useful info\n\n

    This can be used for storing the info in a database or for other
    purposes\n\n
    Let's get started!\n\n
"""
)

print("please provide the file path to the document you want to parse")
file_path = input()

file_path_validation = os.path.isfile(file_path)

while not file_path:
    print("please provide a valid file path")
    file_path = input()
    file_path_validation = os.path.isfile(file_path)

options = ["patient_details", "prescription"]
user_input = ""
input_msg = "Now please provide the type of document you want to parse\n"

for option in options:
    input_msg += f"{option}\n"


while user_input.lower() not in options:
    user_input = input(input_msg)

print(
    "\nvery well, if everything is correct"
    + "the program will deliver the results in a few seconds"
)

try:
    result = extact_info(file_path, user_input)
    print("Here is the result:")
    for key in result.keys():
        print(f"\n\n{key}: {result[key]}")
except Exception as e:
    print(e)
