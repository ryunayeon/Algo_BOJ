import sys
input = sys.stdin.readline

while(True):
    s = input()
    if s == '.\n':
        break

    def solution(s):
        matching = {')' : '(', ']' : '['}
        stack = []
        for c in s:
            if c == '(' or c == '[':
                stack.append(c)
            elif c == ')' or c == ']':
                if not stack or stack[len(stack) - 1] != matching[c]:
                    return 'no'
                stack.pop()
        if stack:
            return 'no'
        else:
            return 'yes'

    print(solution(s))