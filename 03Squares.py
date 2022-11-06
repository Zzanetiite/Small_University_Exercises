# for a number from 1 to 100
for num in range(1, 100 + 1):
    # print number and it's square
    print('Number ' + str(num) + ' square is ' + str(num * num))
    if num * num > 2000:
        break
