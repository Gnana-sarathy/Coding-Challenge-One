def sorting_function(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            short = arr[i] if len(arr[i]) < len(arr[j]) else arr[j]
            k = 0
            while k < len(short):
                if arr[i][k].lower() == arr[j][k].lower():
                    k += 1
                    continue
                else:
                    if arr[i][k].lower() > arr[j][k].lower():
                        arr[i], arr[j] = arr[j], arr[i]
                    break
    return arr


sentence = "welcome to sirius india team"
sentence_list = sentence.split()

# Alternate method
# sentence_list.sort()
# print(*sentence_list)
#
new_list = sorting_function(sentence_list)
print(*new_list)