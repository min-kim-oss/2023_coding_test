import sys
sys.setrecursionlimit(10**6)

parent = {}

def find_parent(node):
    parent_node = node
    if parent_node != parent.get(parent_node):
        parent[parent_node] = find_parent(parent.get(parent_node))
    else:
        return parent.get(parent_node)
    return parent.get(parent_node)

n , m = map(int, sys.stdin.readline().split())

for i in range (m):
    opp, a, b = map(int, sys.stdin.readline().split())
    if opp == 0:
        if a not in parent:
            parent[a] = a
        if b not in parent:
            parent[b] = b

        parent_a = find_parent(a)
        parent_b = find_parent(b)

        if parent_a >= parent_b:
            parent[parent_b] = parent_a
            #print("b", parent.get(b))
        else:
            parent[parent_a] = parent_b
            #print("a", parent.get(a))
        #print(parent)

    elif opp == 1:
        parent_a = a
        parent_b = b
        if parent_a in parent:
            parent_a = find_parent(parent_a)
        if parent_b in parent:
            parent_b = find_parent(parent_b)
        #print("a", parent_a)
        #print("b", parent_b)
        if (parent_a == parent_b):
            print("YES")
        else:
            print("NO")
