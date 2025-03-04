import re

# Use Case 2: Validate Last Name
last_name = input("Enter a valid Last Name: ")
while not (len(last_name) >= 3 and last_name[0].isupper()):
    print("Invalid last name. It should start with a capital letter and have at least 3 characters.")
    last_name = input("Enter a valid Last Name: ")