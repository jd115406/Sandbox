# import random
#
# side_length = int(input("Length: "))
# width = random.randint(1 , side_length)
# area = side_length * width
# print(f"Area of {side_length} x {width} is {area}")

# def print_grid(number_of_rows, number_of_columns):
#     #version 3
#     print(f"{'*' * number_of_columns}\n" * number_of_rows)

# version 1
# for i in range(number_of_rows):
#     print("*" * number_of_columns)

# version 2
# for i in range(number_of_rows):
#     for j in range(number_of_columns):
#         print("*", end="")
#     print()

# print_grid(3, 7)

# def get_limits():
#     low = int(input("Low: "))
#     high = int(input("High: "))
#     return low, high
#
#
# def run_tests():
#     low, high   = get_limits()
#     print(low, high)
#     print(type(low))
# """
# Main Menu:
# -Get valid name
# -Print greeting
# -Print Secret name
# """
# import random
#
#
# def main():
#     name = "Jonathon Bramich"
#     print("Menu: ")
#     choice = input("> ").upper()
#     while choice != "Q":
#         if choice == "N":
#             name = get_valid_name()
#         elif choice == "G":
#             print_greeting(name)
#         elif choice == "S":
#             print_secret_name(name)
#         else:
#             print("Invalid choice")
#         print("Menu: ")
#         choice = input("> ").upper()
#     print("Goodbye")
#
#
# def print_greeting(name):
#     length = len(name)
#     print_line(length)
#     print(f"Hello, {name}")
#     print_line(length)
#
#
# def get_valid_name():
#     name = input("Enter your name: ")
#     while len(name) == 0:
#         print("Invalid name: ")
#         name = input("Enter your name: ")
#     return name
#
#
# def print_line(length):
#     print("-" * length)
#
#
# def print_secret_name(name):
#     letters = list(name)
#     random.shuffle(letters)
#     print("".join(letters))
#
#
# main()

#Password stars
password = input("Enter password: ")

while password == "":
    print("Please enter a password")
    password = input("Enter password: ")
print("*" * len(password))


