import sys

n , m = map(int, sys.stdin.readline().split())

pok_name ={}
pok_id = {}
for i in range (n):
    name = sys.stdin.readline().strip()
    pok_id[name] = i + 1
    pok_name[i + 1] = name

for i in range (m):
    income = sys.stdin.readline().strip()
    if (income.isdigit()):
        income = int(income)
        find_name = pok_name.get(income)
        print(find_name)
    else:
        find_id = pok_id.get(income)
        print(find_id)




