'''
Code a program that:
o	Opens a file called teams.txt
o	Imagine it’s the end of the financial year for the league the teams play in.
This means all the team’s values need to increase in accord with an inflation amount of 5%.

o	Read all the teams into memory as a collection of List objects.

o	Loop through the collection and increase each team’s value by 5%

o	Save the changes back into the teams.txt file.

o	Run the ReadTeams app and confirm the updates have been successful

'''

# With open file teams.txt as stream
with open('./teams.txt', 'r+') as stream:
    # Count of headers in the file
    header = 1  # representing header
    # Location in file (start of line), start with one
    loc = 0
    # for line in the file
    for line in stream.readlines():
        # Split the text into separated word list
        text = line.split(', ')
        # add the inflation to the team value
        text[2] = str(round(float(text[2]) * 1.05,2))
        # create an output line to write
        text_edited = ', '.join(text)
        stream.seek(loc)
        stream.writelines(text_edited)
        loc += len(text_edited)

