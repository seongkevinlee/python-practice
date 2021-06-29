# names = ["Kevin", "John", "Sarah", "Maddie", "Mary"]
# names[0] = 'Kev'
# print(names)

#! PROGRAM TO FIND THE LARGEST NUMBER IN A LIST
# list = [34, 64, 83, 13, 47, 463, 473, 457]
# max = list[0]
# for number in list:
#     if number > max:
#         max = number
# print(max)

#! 2D Lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[1][1] = 20
# print(matrix)
# print(matrix[1][1])

# for row in matrix:
#     for item in row:
#         print(item)

#! LIST METHODS
numbers = [5, 2, 1, 7, 5, 4, 5]
# numbers.append(20)
# print(numbers)

# numbers.insert(0, 21)
# print(numbers)
# numbers.insert(3, 5000)
# print(numbers)

# numbers.remove(5000)
# print(numbers)
# numbers.remove(21)
# print(numbers)

# ? CLEAR ALL VALUES IN ARRAY
# numbers.clear()
# print(numbers)

# ? REMOVE LAST VALUE IN ARRAY
numbers.pop()
print(numbers)

print(numbers.index(7))
# print(numbers.index(21))

print(1 in numbers)
print(155 in numbers)

print(numbers.count(5))

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers2.reverse()
print("numbers: " + str(numbers))
print("numbers2: " + str(numbers2))

#!WRITE A PROGRAM TO REMOVE DUPLICATES IN A LIST
list = [1, 2, 3, 4, 4, 6, 6, 8, 9, 20]
uniques = []
for number in list:
    if number not in uniques:
        uniques.append(number)
print(uniques)
