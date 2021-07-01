customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer.get("birthdate"))
customer["birthdate"] = "02/21/89"

#! SECOND ARGUMENT IS DEFAULT VALUE IF VALUE OF FIRST ARGUMENT DOESN'T EXIST
print(customer.get("birthdate"))
print(customer)

#! EXERCISE THAT OUTPUTS A LIST OF NUMBERS INTO TEXT
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)
