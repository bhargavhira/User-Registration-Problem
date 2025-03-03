import re

# Use Case 1: Validate First Name
first_name = input("Enter a valid First Name: ")
while not (len(first_name) >= 3 and first_name[0].isupper()):
    print("Invalid first name. It should start with a capital letter and have at least 3 characters.")
    first_name = input("Enter a valid First Name: ")