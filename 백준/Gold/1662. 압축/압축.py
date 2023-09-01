S = input()
stack = []
length = 0
tmp = ''

for i in S:
    if i == '(':
        stack.append((tmp, length-1))
        length = 0
    elif i == ')':
        compressedNum, preLength = stack.pop()
        length = (int(compressedNum)*length)+preLength
    else:
        length += 1
        tmp = i

print(length)