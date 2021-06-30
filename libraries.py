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
