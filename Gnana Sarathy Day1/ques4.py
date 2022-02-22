sentence = "welcome to sirius india team"
maximum = 0
word = ''
for i in sentence.split():
    length = len(i)
    if length > maximum:
        maximum = length
        word = i

print(word, maximum)
