# reduces lines
file = open('filename.txt', 'r')
outfile = ''
for line in range(10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()
file = open('filename.txt', 'w')
file.write(outfile)
file.close()

# Tips and tricks
fname = 'output.txt'
wholefile = open(fname).read()
neat_lines= open(fname).read().splitlines()
lines3 = open(fname).readlines()
print('whole file:', wholefile, '\nl2: ', neat_lines, '\nl3: ', lines3)

# this is not efficient
for line in open(fname).readlines():
    print(line, end="")

# instead use onject iterator:
for line in open(fname) :
    print(line, end="")

# reading with 'with' operator
with open(fname, 'r') as infile:
    for line in infile:
        print(line, end='')


# get current position with tell() method
fh = open('output.txt', 'rb')

index={}
while True:
    line = fh.readline()
    if not line: break
    fields = line.decode().split('\n')
    index[fields[0]] = fh.tell() - len(line)
    print(index)

key = input('Enter a country:')
fh.seek(index[key])
print(fh.readline().decode(), end="")


