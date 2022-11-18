'''
Assignment:
Create a timer function that times the start
and end of a function.
Function reads the words.txt file
'''

import os
# Define the global variable
start_time = 0


def start_timer():
    """
    registers the time at the start
    :return: int, time
    """
    # calculate total time it takes for the
    # CPU since the script started
    # change the global variable
    global start_time
    start_time = sum(os.times()[0:2])
    return


def end_timer():
    """
    takes the start time and subtracts
    that from time when this func. is called
    :return: int, time
    """
    total_time = sum(os.times()[0:2])
    print(total_time)
    end_time = total_time - start_time
    return "Function takes :" + format(end_time,'.3f') + " seconds."


lines = 0
for row in open("words.txt"):
    lines += 1

print(end_timer())
print("Number of lines: ", lines)
