d = list(input())

arr = [-1 for i in range (26)]
for i in range (len(d)):
    if(arr[ord(d[i])-ord('a')] == -1):
        arr[ord(d[i])-ord('a')] = i
for i in range (len(arr)):
    print(arr[i],end = " ")