# name = input("What is your name? ")
# age = int(input("What is your age? "))

# print("Hello " + name)

# if age > 18:
#     print(name + ", You are a legal adult.")
# elif age < 18:
#     print(name + ", You are not yet a legal adult.")
# else:
#     print(name + ", You old..")


# price = 1000000
# buyer_credit = input("How is your credit? (Good or Bad?)").lower()

# if buyer_credit == "good":
#     down = 0.1
#     down_payment = str(price * down)
# else:
#     down = 0.2
#     down_payment = str(price * down)

# print("Your down payment will be " + down_payment)


high_income = False
good_credit = False

if high_income and good_credit:
    print("You are eligible for a loan with a good rate.")
elif high_income or good_credit:
    print("You are eligible for a loan under circumstances")
else:
    print("You are not eligible for a loan.")
