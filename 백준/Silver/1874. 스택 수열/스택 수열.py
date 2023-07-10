n = int(input())
stack_seq = []
answer = []
cnt = 1
check = True

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack_seq.append(cnt)
        answer.append("+")
        cnt +=1
    
    if stack_seq[-1] == num:
        stack_seq.pop()
        answer.append("-")
    else:
        check = False
        break;

if check == False:
    print("NO")
else:
    for a in answer:
        print(a)