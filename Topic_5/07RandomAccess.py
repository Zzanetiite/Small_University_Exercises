# get current position with tell() method
fh = open('output.txt', 'rb')

index = {}
while True:
    line = fh.readline()
    if not line: break
    fields = line.decode().split(',')
    index[fields[0]] = fh.tell() - len(line)

key = input('Enter a country ID, Q to quit:')

while key != 'Q':
    key = key.zfill(4)
    if key in index:
        fh.seek(index[key])
        print(fh.readline(), end="")
    else:
        print('Invalid key')
    key = input('\nEnter a country ID (Q to quit): ').upper()
