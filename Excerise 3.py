"""
this while loop will ask repeatedly the user for their name, hometown, and age. Until they get
the valid input they provided
"""
while True:
    """
    this code asks question for the user for their input and then storing them in a variable which are
    name, hometown, and age from the user.
    """
    try:
        name = input("Enter your full name: ")
        hometown = input("Enter your hometown: ")
        age = int(input("Enter your age: "))
        """
        if the value of the imput provided is valid then it will break out of the loop
        """
        break
    except ValueError:
        print("Invalid input. Please enter a integer.")
"""
If the user answer an string on the question of the age and its not an integer, 
it will then print an error message
"""
print(name)
print(hometown)
print(age)

"""
prints the users information
"""