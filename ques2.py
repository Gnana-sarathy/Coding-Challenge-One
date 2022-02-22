string = "aabbbcaaa"

i = 0
length = len(string)
while i < length:
    j = i
    count = 0
    while j < length:
        if string[i] == string[j]:
            count += 1
        else:
            break
        j += 1
    print(string[i], count, sep='', end ='')
    i = j
