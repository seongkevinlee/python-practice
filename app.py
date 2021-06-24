import math

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


# high_income = False
# good_credit = False

# if high_income and good_credit:
#     print("You are eligible for a loan with a good rate.")
# elif high_income or good_credit:
#     print("You are eligible for a loan under circumstances")
# else:
#     print("You are not eligible for a loan.")


#! WEIGHT CONVERTER EXERCISE
# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)gs: ").upper()

# if unit == "K":
#     print("You weigh " + str(math.trunc(weight * 2.2)) + " Lbs.")
# else:
#     print("You weigh " + str(math.trunc(weight * 0.45)) + " Kgs.")


#! WHILE LOOPS
# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done.")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess a number: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You win!")
#         break
# else:
#     print("You lose!")


#!CAR GAME
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already on!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, unrecognized command.")

#!FOR LOOPS
for item in range(5, 10, 2):
    print(item)

# CALCULATE TOTAL COST OF ALL ITEMS IN A SHOPPING CARD
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
