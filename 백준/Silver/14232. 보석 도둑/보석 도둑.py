n = int(input())
jewel = []

for i in range(2, int(n**0.5)+1):
    while n%i == 0:
        jewel.append(i)
        n //= i

if n != 1: jewel.append(n)

print(len(jewel))
print(*jewel)