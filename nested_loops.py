# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

numbers = [5, 5, 5, 5, 5]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        if count == 2:
            output += " "
        else:
            output += "x"
    print(output)

    