'''
Write a Python script to list all the unused port numbers in the
/etc/services file between 1 and 200
•	Create a new file: UnusedPortNumbers.py
•	Become familiar with the input file - view it first
•	Write the main code to read the services file one line at a time
•	Use string functions or a regular expression to:
o	Ignore lines starting with a # comment character
o	Ignore lines that just consist of "white-space"
•	The /etc/services file has several columns separated by white-space
o	Use split or a regular expression to isolate the port/protocol field
o	Use another split or regular expression to isolate the port number
o	Don't forget to stop at port number 200!
o	Note that many port numbers have > 1 entry

On Windows the file is in 'C:\WINDOWS\system32\drivers\etc\services'
 or in 'C:\WINNT\system32\drivers\etc\services'.
On OSX the file has unused ports marked as 'Unassigned'. Therefore,
we have an additional requirement: ignore all lines that start with the
comment delimiter '#'.
Many port numbers have more than one entry in the file, but you may
assume they are in order.
Hints:
•	Open the file.
•	Read the file line-by-line using a for loop.
•	Consider using a set or a dictionary to hold the port numbers.
•	Be careful of comparing strings and int - you will have to convert the
 port number to an integer.

Cannot find the file location in Mac. Will need to do it on other PC.
'''
