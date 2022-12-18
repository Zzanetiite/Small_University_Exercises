'''
Code a program that:

Opens a file called teams.txt
o	Reads one row at a time and outputs the
details of the teams as separate rows on the console.

o	Tidy up the output so the data is shown in columns
where strings are left justified and numbers right justified
and showing a currency sign for team values.

o	Print a set of appropriate column headings before the team data.

'''

# With open file teams.txt as stream
with open('./teams.txt', 'r') as stream:
    # Count of headers in the file
    header = 1  # representing header
    # spacing of the text columns
    n = 20
    # for line in the file
    for line in stream.readlines():
        # Split the text into separated word list
        text = line.split(', ')
        # Header rows to look different from normal rows
        if header != 0:
            print('%-*s %-*s %-*s %-*s %-*s' % (8, 'Team ID'.rjust(7), n, 'Team name'.ljust(2), 1, 'Team value'.ljust(14), 5, 'Year established '.rjust(n), n, 'Strip colour'.ljust(2)))
            header -= 1
        # Other rows as per conditions of the task
        print('%-*s %-*s %-*s %-*s %-*s' % (8, text[0].rjust(7), n, text[1].ljust(2), 1, f"£ {text[2]}".ljust(14), 5, text[3].rjust(n), n, text[4].ljust(4)))