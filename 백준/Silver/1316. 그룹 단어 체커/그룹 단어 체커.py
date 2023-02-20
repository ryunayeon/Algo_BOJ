ans = []
n = int(input())
for _ in range(n):
    word = input()
    cnt = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            cnt += 1
    if cnt < len(set(word)):
        ans.append(word)
print(len(ans))