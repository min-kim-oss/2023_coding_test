upper_string = (input()).upper()
arr = list(upper_string)
alphabet = [0 for i in range (26)]
for i in range(len(arr)):
    alphabet[ord(arr[i])-ord('A')] += 1

max = 0
max_num = 0
for i in range(len(alphabet)):
    if (max < alphabet[i]):
        max = alphabet[i]
        max_num = i
check = 0
for i in range (len(alphabet)):
    if(max_num != i) and (max == alphabet[i]):
        check = 1
if(check == 1):
    print("?")
else:
    print(chr(max_num + ord('A')))