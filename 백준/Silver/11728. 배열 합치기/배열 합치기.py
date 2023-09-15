n, m = map(int,input().split())
listN = list(map(int,input().split()))
listM = list(map(int,input().split()))
p1 = p2 = 0
nm = []
while p1<n and p2<m:
    if listN[p1] <= listM[p2]:
        nm.append(listN[p1])
        p1+=1
    else:
        nm.append(listM[p2])
        p2+=1
if p1<n:
    nm = nm+listN[p1:]
else:
    nm = nm+listM[p2:]
for x in nm:
    print(x, end = ' ')