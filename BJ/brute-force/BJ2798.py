n, m = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

#print(num)

largest = 0

for i in range (n-2):
    sum = 0
    for j in range (i+1,n-1):
        for k in range(j+1,n):
            #print(i, j , k)
            sum = num[i] + num[j] + num[k] 
            if sum > m : 
                break
            elif sum > largest:
                largest = sum
            
print(largest)