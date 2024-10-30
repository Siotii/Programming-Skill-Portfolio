"""
ADVANCE Exercise 4: Primitive Quiz - 30 Marks 
"""
"""
this codes will store the questions in a variables, from question1 to question10.
We will also store the correct answers for the questions in an variables from 1 to 10
"""
question1 = "What is the capital of France? "
correct_answer1 = "Paris"
    
question2 = "What is the captial of Italy? "
correct_answer2 = "Rome"
    
question3 = "What is the captial of Germany? "
correct_answer3 = "Berlin"
    
question4 = "What is the captial of Netherland? "
correct_answer4 = "Amsterdam"
    
question5 = "What is the captial of Norway? "
correct_answer5 = "Oslo"
    
question6 = "What is the captial of Poland? "
correct_answer6 = "Warsaw"
    
question7 = "What is the captial of Spain? "
correct_answer7 = "Madrid"
    
question8 = "What is the captial of Serbia? "
correct_answer8 = "Moscow"
    
question9 = "What is the captial of Ireland? "
correct_answer9 = "Reykjavik"
    
question10 = "What is the captial of denmark? "
correct_answer10 = "Copenhagen"
    
"""
    this codes are just the same but has different value. 
    it works like the system will ask for input an it will 
    store it in a variable which is called user_answer, 
    it will the make the answer into lower capitalization 
    then using the if statement it will check if the user's answer
    is equal to the correct answer. if its equal then it will print 
    out correct but then using the else statement, if the user's answer 
    is not equal to the correct answer then it will print out incorrect. 
    This will carry out from question1 until to question10.
"""
    
user_answer1 = input(question1).strip().lower()
if user_answer1 == correct_answer1.lower():
        print("Correct! Paris is indeed the capital of France.")
else:
        print("Incorrect. The capital of France is Paris.")
    
user_answer2 = input(question2).strip().lower()
if user_answer2 == correct_answer2.lower():
        print("Correct! Rome is indeed the capital of Italy.")
else:
        print("Incorrect. The capital of Italy is Rome.")
        
user_answer3 = input(question3).strip().lower()
if user_answer3 == correct_answer3.lower():
        print("Correct! Berlin is indeed the capital of Germany.")
else:
        print("Incorrect. The capital of Germany is Berlin.")   
        
user_answer4 = input(question4).strip().lower()
if user_answer4 == correct_answer4.lower():
        print("Correct! Amsterdam is indeed the capital of Netherland.")
else:
        print("Incorrect. The capital of Netherland is Amsterdam.")
        
user_answer5 = input(question5).strip().lower()
if user_answer5 == correct_answer5.lower():
        print("Correct! Oslo is indeed the capital of Norway.")
else:
        print("Incorrect. The capital of Norway is Oslo.")
        
user_answer6 = input(question6).strip().lower()
if user_answer6 == correct_answer6.lower():
        print("Correct! Warsaw is indeed the capital of Poland.")
else:
        print("Incorrect. The capital of Poland is Warsaw.")
        
user_answer7 = input(question7).strip().lower()
if user_answer7 == correct_answer7.lower():
        print("Correct! Madrid is indeed the capital of Spain.")
else:
        print("Incorrect. The capital of Spain is Madrid.")
        
user_answer8 = input(question8).strip().lower()
if user_answer8 == correct_answer8.lower():
        print("Correct! Moscow is indeed the capital of Serbia.")
else:
        print("Incorrect. The capital of Serbia is Moscow.")
        
user_answer9 = input(question9).strip().lower()
if user_answer9 == correct_answer9.lower():
        print("Correct! Reykjavik is indeed the capital of Ireland.")
else:
        print("Incorrect. The capital of Ireland is Reykjavik.")
        
user_answer10 = input(question10).strip().lower()
if user_answer10 == correct_answer10.lower():
        print("Correct! Copenhagen is indeed the capital of Denmark.")
else:
        print("Incorrect. The capital of Denmark is Copenhagen.")
 