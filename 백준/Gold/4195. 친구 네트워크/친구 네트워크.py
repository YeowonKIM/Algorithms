test_case = int(input())

# Find(x): 재귀적으로 함수를 호출하며, x의 Root노드를 반환
def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

# Union(x,y): x와 y의 Root노드를 찾고, y의 Root노드를 x로 한다.
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parents[y] = x
        child_num[x] += child_num[y]
    

for _ in range(test_case):
    relations = int(input())
    parents = dict()
    child_num = dict()
    
    for _ in range(relations):
        x, y = input().split()
        
        if x not in parents:
            parents[x] = x
            child_num[x] = 1
        if y not in parents:
            parents[y] = y
            child_num[y] = 1
        
        union(x, y)
        print(child_num[find(x)])