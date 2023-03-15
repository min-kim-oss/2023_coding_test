word_num = int(input())

word_arr = []

for i in range (word_num):
    new_word = input()
    if ([len(new_word), new_word] not in word_arr):
        word_arr.append([len(new_word),new_word])

word_arr.sort()

# for i in range (len(word_arr)):
#     for j in range(len(word_arr)-i-1):
#         if(len(word_arr[j+1]) < len(word_arr[j])):
#             temp = word_arr[j]
#             word_arr[j] = word_arr[j+1]
#             word_arr[j+1] = temp
#         elif (len(word_arr[j + 1]) == len(word_arr[j])):
#             if (word_arr[j + 1] < word_arr[j]):
#                 temp = word_arr[j]
#                 word_arr[j] = word_arr[j + 1]
#                 word_arr[j + 1] = temp

for i in range(len(word_arr)):
    print(word_arr[i][1])
