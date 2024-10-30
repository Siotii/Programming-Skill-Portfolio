"""
ADVANCE Exercise 6: Brute Force Attack - 30 Marks
"""

"""
we will stored the correct password in variable and then the attempts.
"""
correct_password = "12345"
attempts = 5

"""
We made a while loop which the system will ask an question until the user answers
correct password it will the stop or until the user runs out of attempts.

using the if statement if the answer from the user is equal to the correct password
it will then grant access for the user. If the user answers wrong it will the say incorrect password, 
it will remove 1 attempt from the user then will ask the user the question again. if the user fail to
give the correct answer after the last attempt it will stop the console then say maximum attepets has been reached.
"""
while True:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Password correct. Access granted.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect password. {attempts} attempts remaining.")
        else:
            print("Maximum attempts reached. Authorities alerted.")
            break