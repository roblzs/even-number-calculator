#calculate the list of all even numbers under 1000

import time
import sys

def check_if_even(all_numbers):
    even_numbers = []

    for i in all_numbers:
        correct = i / 2

        correct = str(round(correct, 1))

        if int(correct[(len(correct) -1)]) == 0:
            even_numbers.append(i)

    return even_numbers


def run(i, max_num, time_the_calculation):
    if time_the_calculation:
        start_time = time.time()

    all_numbers = []

    i += 1

    while i < max_num:
        i += 1

        all_numbers.append(i)
    
    even_numbers = check_if_even(all_numbers)

    if time_the_calculation:
        end_time = time.time()

        time_spent = end_time - start_time

    print("Even numbers:")
    print("")
    print(even_numbers)
    print("")
    print("There are", len(even_numbers), "even numbers in this list")
    print("")
    if time_the_calculation:
        print("Time spent calculating:", time_spent, "seconds")
        print("")

#1. to calculate the list of even numbers from 1 to x, first prop should be -1
#2. on the second prop You can specify to whitch number the calculations should run
#3. to get the time it takes to calculate the even numbers, the third prop should be True

try:
    run(i=-1, max_num=1000, time_the_calculation=True)
except Exception:
    print("Calculation crashed")
    sys.exit()

#PS
#It's best to stick to small numbers on the second prop ;)
#or Your computer will start freezing