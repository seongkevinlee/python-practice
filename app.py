name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello " + name)

if age > 18:
    print(name + ", You are a legal adult.")
elif age < 18:
    print(name + ", You are not yet a legal adult.")
else:
    print(name + ", You old..")
