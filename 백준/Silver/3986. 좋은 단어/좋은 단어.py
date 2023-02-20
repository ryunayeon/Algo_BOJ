def erase(s):
    stack = []
    stack.append(s[0])
    global cnt
    for i in range(1, len(s)):
        if stack:
            if stack[-1] != s[i]:
                # print(stack)
                stack.append(s[i])
            else:
                stack.pop()
        else:
            stack.append(s[i])
    if len(stack) == 0:
        cnt += 1
    return cnt


cnt = 0

t = int(input())
for _ in range(t):
    word = input()
    erase(word)
print(cnt)
