t = int(input())

def solution(s):
    matching = {')' : '('}
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            # 괄호끼리 맞는 짝이 아닌 경우 NO 반환
            if not stack or stack[len(stack) - 1] != matching[c]:
                return 'NO'
            stack.pop()
        # 스택에 남은 괄호가 있다면 NO, 모든 괄호가 다 사라졌으면 짝이 맞으므로 YES
    if stack:
        return 'NO'
    else:
        return 'YES'

for _ in range(t):
    print(solution(input()))