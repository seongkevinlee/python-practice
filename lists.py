# names = ["Kevin", "John", "Sarah", "Maddie", "Mary"]
# names[0] = 'Kev'
# print(names)

#! PROGRAM TO FIND THE LARGEST NUMBER IN A LIST
list = [34, 64, 83, 13, 47, 463, 473, 457]
max = list[0]
for number in list:
    if number > max:
        max = number
print(max)
