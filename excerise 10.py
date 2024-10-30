"""
Exercise 10: Is it even? - 35 Marks

"""

"""
this will determine whether the number is even or odd.
it will take the number input from the user and then will be in a modulo operator
and check if the remainder divided by 2 is 0. it will return the string "even"if the number is even
or it will return the string "odd".

"""
def evenodd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
"""
this askes the user to enter an number and converts it into a int.
then will call on the evenodd the run its code. the it will print out the number and whether is 
a even or odd.
"""
def main():

    number = int(input("Enter a number: "))
    result = evenodd(number)
    print(f"The number {number} is {result}.")

if __name__ == "__main__":
    main()