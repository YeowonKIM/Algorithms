n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

cnt = {}
for card in cards:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1
        
for target in targets:
    answer = cnt.get(target)
    if answer == None:
        print(0, end=" ")
    else:
        print(answer, end=" ")