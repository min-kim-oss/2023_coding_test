arr = list(input())

sum = 0
for i in range (len(arr)):
    num = ord(arr[i])
    
    if (ord('A') <= num) and (num <= ord('C')):
        sum += 3
    elif (ord('D') <= num) and (num <= ord('F')):
        sum += 4
    elif (ord('G') <= num) and (num <= ord('I')):
        sum += 5
    elif (ord('J') <= num) and (num <= ord('L')):
        sum += 6
    elif (ord('M') <= num) and (num <= ord('O')):
        sum += 7
    elif (ord('P') <= num) and (num <= ord('S')):
        sum += 8
    elif (ord('T') <= num) and (num <= ord('V')):
        sum += 9
    elif (ord('W') <= num) and (num <= ord('Z')):
        sum += 10
    else:
        sum += 11
print(sum)