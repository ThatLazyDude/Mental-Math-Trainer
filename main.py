import random
import operator
import time
import readline #Allows using arrow keys to go back and forth in the input field. S: https://stackoverflow.com/questions/45772230/arrow-keys-not-working-while-entering-data-for-input-function

# System steps:
# 1. Pick calculation type at random
# 2. Pick two random numbers, depending on calculation type
# 3. Display calculation
# 4. Receive input from user
# 5. Check input vs. result of calculation
# 5.a If correct, add 1 round to round counter and show next calculation
# 5.b If wrong
#   add 1 to wrong_answer counter
#   display message 'Wrong answers: {wrong_answer}' 
#   'go back' to 3.
# Display stats: rounds, wrong answers, time

# Possible refinement steps for later: 
# Pick rounds or time with default settings
# Pick difficulty

operator_functions = { # Alt: ['+', '-', '*', '/']. Use in combination with answer = eval(question). 
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '+': operator.add,
} # S: https://stackoverflow.com/questions/30926323/how-to-do-a-calculation-on-python-with-a-random-operator

def operation():
    sign, calculation = random.choice(list(operator_functions.items())) 
        # How to random pick from a dictionary https://bobbyhadz.com/blog/python-get-random-key-value-from-dictionary
        # .items() to get key and value pair. keys() or values() otherwise
    if calculation == operator.add:
        number_1, number_2 = random.randint(1,1000), random.randint(1,1000)
    elif calculation == operator.truediv:
        a = random.randint(1,50)
        b = random.randint(1,50)
        number_1 = a*b 
        number_2 = random.choice([a, b])
    else: 
        number_1, number_2 = random.randint(1,100), random.randint(1,100) 
    result = operator_functions[sign](number_1, number_2)
    return result, number_1, number_2, sign

def get_answer(number_1, number_2, sign):
    answer = int(input(f'\n{number_1}{sign}{number_2}=')) 
    return answer

def success(answer, result):
    return True if answer == result else False

def math_trainer(rounds):
    start = time.time()
    wrong_answers, i = 0, 0
    for i in range(rounds):
        result, number_1, number_2, sign = operation()
        answer = get_answer(number_1, number_2, sign)
        while True: # S: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
            if not success(answer, result):
                wrong_answers += 1
                print(f'\nWrong answers: {wrong_answers}. Try again!\n')
                answer = get_answer(number_1, number_2, sign)
            else: 
                i += 1 # Add 1 round
                print(f'\nGreat! Round: {i}/{rounds}\n')
                break
    end = time.time() 
    duration = round((end-start)/60, 1)
    print(f'\nFinished!\nRounds: {rounds}\nDuration: {duration} minutes\nWrong answers: {wrong_answers}\n')

math_trainer(10) 






