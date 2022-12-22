try:
    import myTimer

    try:
        myTimer.start_timer()
        lines = 0
        for row in open("wordlist10000.txt"):
            lines += 1

        myTimer.end_timer()
        print("Number of lines:", lines)
    except (TypeError, ValueError, FileNotFoundError) as err:
        print('Error occurred:', err.args[1])

    # Added for Exercise 11, should crash
    myTimer.end_timer()
except ModuleNotFoundError as err:
    print('No module named', err.name)
except SystemError as err:
    print('System error:', err.args[0])

# Now handle the exception


print("We are all done")
