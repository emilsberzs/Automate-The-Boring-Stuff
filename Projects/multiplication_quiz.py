import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    #Pick two random integers
    first_number = random.randint(0,9)
    second_number = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (question_number + 1,first_number,second_number)

    try:
        #Correct answers are handled by allow_regexes
        #Incorrect answers are handled by block_regexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (first_number * second_number)],
                      blockRegexes=['.*', 'Incorrect'],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        #This block executes if no exceptions were raised
        print('Correct!')
        correct_answers += 1
    time.sleep(1) #1 second pause to let user see result
print('Score: %s / %s' % (correct_answers, number_of_questions))