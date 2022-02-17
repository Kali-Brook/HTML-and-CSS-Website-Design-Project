# Scenario to be simulated with if, elif, else, etc. conditional statements on python:
# Persons live in a street, having houses in line. Consider the following:

# 1.	A lives in the corner’s house
# 2.	C is between E and G
# 3.	There is 1 house between D and F
# 4.	F is neighbor of G
# 5.	There are two houses between A and G

# Your simulation should be interactive and should help answer the following questions:
# Who lives in the second corner?
# Who lives in the middle?
# Who lives between B and G?
# Who is the neighbor of A?
# How many houses are there between B and E?

# Answers: (D)(G) (F)(E)(3)

start = input("Please carefully read the following scenario and if you wish to continue enter Yes or Y. "
              "If you wish to quit enter No or N. \n\n"
              "Persons live in a street, having houses in line. Consider the following: \n"
              "1.	A lives in the corner’s house \n"
              "2.	C is between E and G \n"
              "3.	There is 1 house between D and F \n"
              "4.	F is neighbor of G \n"
              "5.	There are two houses between A and G\n\n"
              "Do you wish to continue: ")

if start == "Y" or start == "y" or start == "Yes" or start == "yes":
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    print("You have started to work on the Scenario. Welcome " + first_name + " " + last_name + ".\n")
    question_1 = input(" Q1. If A lives in the corner's house, Who lives in the second corner?\n"
                       "Answer: ")
    if question_1 == 'D' or question_1 == 'd':
        print("Correct answer, D lives in the second corner. Please proceed to the next question.")
    else:
        print("Incorrect answer, please try again.")
    question_2 = input(" Q2. C is between E and G, Who lives in the middle?\n"
                       "Answer: ")
    if question_2 == 'G' or question_2 == 'g':
        print("Correct answer, G lives in the middle. Please proceed to the next question.")
    else:
        print("Incorrect answer, please try again.")
    question_3 = input(" Q3. There is 1 house between D and F, Who lives between B and G?\n"
                       "Answer: ")
    if question_3 == 'F' or question_3 == 'f':
        print("Correct answer, F lives between B and G. Please proceed to the next question.")
    else:
        print("Incorrect answer, please try again.")
    question_4 = input(" Q4. F is neighbor of G, Who is the neighbour of A?\n"
                       "Answer: ")
    if question_4 == 'E' or question_4 == 'e':
        print("Correct answer, E is the neighbour of A. Please proceed to the last question of this scenario.")
    else:
        print("Incorrect answer, Please try again.")
    question_5 = input(" Q5. There are two houses between A and G, How many houses are there between B and E?\n"
                       "Answer: ")
    if question_5 == '3' or question_5 == 'Three' or question_5 == 'three':
        print("Correct answer, There are 3(Three) houses between B and E.\n\n"
              "Thank you for participating on the given scenario. Goodbye!")
elif start == 'N' or start == 'n' or start == 'No' or start == "no":
    print("Thank you!")
else:
    var = start != 'N' or start != 'n' or start != 'No' or start != 'no'
    print("Wrong input, Goodbye!")
    exit()
