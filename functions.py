def greet_user(first_name, total_age):
    print(f'Hi {name}!')
    print(f'You are {age} years old!')


def calculate_cost(total, shipping, discount):
    final = (total + shipping) * discount
    print("\nThe total cost with your discount is ${:0.2f}\n".format(final))


# name = input('What is your name? ')
# age = input("How old are you? ")


# greet_user(total_age=age, first_name=name)


calculate_cost(total=50, shipping=5, discount=0.1)
