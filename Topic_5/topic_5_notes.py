# To work with system files:
# os.path

# or new Python
from pathlib import Path

# Where am I?
cwd = Path.cwd()
print('\nCurrent working directory:\n' + str(cwd))

# Combine parts to create full path name file name
new_file = Path.joinpath(cwd, 'new_file.txt')
print('\nFull path:\n' + str(new_file))

# Does this exist?
print(new_file.exists())

# Get the parent directory
parent = cwd.parent

# Is this directory?
print(parent.is_dir())

# Is this a file?
print(parent.is_file())

# List child directories
for child in parent.iterdir():
    if child.is_dir():
        print(child)

# Get the file name, extension, folder, size
print(new_file.name)
print(new_file.suffix)
print(new_file.parent.name)
# print(new_file.stat().st_size)

# get file name
print('\nfile suffix: ' + new_file.suffix)

# stream = open(file_name, mode, buffer_size)
# modes : r, w, a, x (write, fail if file exists)
# r+ read/ write, w+ read/write and create or replace file
# a+ create & append file for read/write
# , +- (update), t(text), b(binary)

# Reading from a file
stream = open('demo.txt')

print(stream.readable())  # can we read?
print(stream.read(1))  # read the first character
print(stream.readline())  # read a line
stream.close()  # close the stream

# Writing to a file
stream = open('output.txt', 'wt')  # write text
stream.write('H')  # write a single string
stream.writelines(['ello', ' ', 'world'])  # write multiple string
stream.write('\n')  # write a new line
names = ['apple', 'susan']  # create a list of strings
stream.writelines(names)
stream.close()  # close the stream an flush data

# Managing the stream
stream = open('output.txt', 'wt')  # write text
stream.write('demo!')
stream.seek(0)  # Put the cursor back at the start (overwrites)
stream.write('cool')
stream.flush()  # write the data to the file
stream.close()  # flush & close the stream

# Working with files - read
stream = open('./output.txt', 'rt')
print('\nIs this readable? ' + str(stream.readable()))
print('\nRead one character : ' + stream.read(1))
print('\nRead the end of the line : ' + stream.readline())
print('\nRead all lines to end of file : \n' + str(stream.readlines()))
stream.close()

# Working with files - write
stream = open('./output.txt', 'wt')

stream.write('H')  # Write a single string
stream.writelines(['ello', ' ', 'world'])  # Write more strings
stream.write('\n')  # Write a new line
names = ['Susan', 'Christopher']
stream.writelines(names)
stream.write('\n')
stream.writelines('\n'.join(names))
stream.close()

# trying to open a file and if there are errors close it
try:
    stream = open('./output.txt', 'wt')
    stream.write('\n')  # Write a new line
finally:
    stream.close()

# Simplifying the above with 'with'
with open('./output.txt', 'wt') as stream:
    stream.write('\nnew line') # this overwrites the file

# with can be used with file streams that require closing


