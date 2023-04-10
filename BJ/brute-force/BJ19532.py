a, b, c ,d, e, f = map(int,input().split())

end = 0
for i in range(-999 , 1000):
    for j in range(-999, 1000):
        if ((a*i + b*j) == c):
            if ((d*i + e*j) == f):
                print(i, j)
                end = 1
                break
            else:
                continue
        else:
            continue
    if end == 1:
        break