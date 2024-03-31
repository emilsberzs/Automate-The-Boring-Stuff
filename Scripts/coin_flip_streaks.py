import random
number_of_streaks = 0
for experiment_number in range(10000):
    #Code that creates list of 100 random Heads or Tails values
    toss_list = []
    for toss in range(100):
        choices = ['H', 'T']
        toss_list.append(random.choice(choices))

    #Code that check if there is a streak of 6 Heads or Tails in a row
    streak_count = 0
    for i in range(len(toss_list) -5):
        if ''.join(toss_list[i:i+6]) == 'H' * 6 or ''.join(toss_list[i:i+6]) == 'T' * 6:
            streak_count += 1
    number_of_streaks += streak_count
        

print('Chance of streak: %s%%' % (number_of_streaks / (100 * 10000)))
