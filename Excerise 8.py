"""
Exercise 8: Simple Search - 30 Marks
"""

"""
we made a list storing specific names and store the in a variable
the system will as the user from name to search and that input will be stored in variable
"""
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_term = input("Enter the name to search: ")

"""
the for loop will loop around name in the list to check. if the name is found inside the list
it will print out an message then break. if the name is not of the list it will send a message that
the name is not on the list
"""
for name in names:
    if name == search_term:
        print(f"Found {search_term} in the list.")
        break
else:
    print(f"{search_term} not found in the list.")