n, m = map(int, input().split())

def backtrack(list, depth):
    depth += 1 #새로운 아래의 트리로 들어왔기에 깊이를 추가해 준다
    #print("depth", depth)
    for i in range(1, n+1):
        if (i not in list):
            list.append(i)
        else:
            continue
        if(depth == m):
            for j in range(len(list)):
                print(list[j], end=" ")
            print()
        else:
            backtrack(list, depth)
        list.pop()
    depth -= 1

#for i in range(n):
list= []
depth = 0
backtrack(list, depth)
