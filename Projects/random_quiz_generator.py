#! python3
# random_quiz_generator.py - Creates quizzes with quiestions and answers in random order, 
# along with answer keys

'''
1.Create 35 different quizes
2.Create 50 multiple choice questions for each quiz in random order
3.Provide correct and three wrong answers for each question
4.Write quizes to 35 text files
5.Write answer keys to 35 text files
'''
import random

#The quiz data, with states as keys and capitals as values
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 
            'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 
            'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 
            'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 
            'Wyoming': 'Cheyenne'}

#Generate 35 quiz files
for quiz_num in range(35):
    # Create the quiz and answe key files:
    quiz_file = open(f'capitals_quiz{quiz_num + 1}.txt', 'w')
    answer_key_file = open(f'capitals_quiz_answers{quiz_num + 1}.txt', 'w')

    #Write out the header for the quiz
    quiz_file.write('Name:\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})')
    quiz_file.write('\n\n')

    #Shuffle order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    #Loop through all 50 states, making questions for each
    for question_num in range(50):
        #Get right and wrong answers:
        correct_answer = capitals[states[question_num]] #set correct answer from dictionary
        wrong_answers = list(capitals.values()) #assign all possible answers to wrong answers
        del wrong_answers[wrong_answers.index(correct_answer)] #delete correct answer
        wrong_answers = random.sample(wrong_answers, 3) #assign 3 of the wrong answers to wrong_answers
        answer_options = wrong_answers + [correct_answer] #assign 3 wrong ansers and the correct one to anwer_options variable
        random.shuffle(answer_options)

        #Write the questions and the answer options to quiz file
        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. { answer_options[i]}\n")
        quiz_file.write('\n')

        #Write answer key to a file
        answer_key_file.write(f"{question_num +1 }.
                              {'ABCD'[answer_options.index(correct_answer)]}")
    quiz_file.close()
    answer_key_file.close()




