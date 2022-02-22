string = "a2b3c4d86"

n = 0
length = len(string)
c = string[0]
for i in range(1, length):
    if i == length-1:
        n *= 10
        n += int(string[i])
        print(c * n)
    elif string[i].isnumeric():
        n *= 10
        n += int(string[i])
    else:
        print(c*n, end='')
        n = 0
        c = string[i]



