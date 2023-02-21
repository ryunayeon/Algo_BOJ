def solution(common):
    answer = 0
    for i in range(1, len(common)-1):
        if 2 * common[i] == common[i-1] + common[i+1]:
            answer = int(common[-1] + (common[i] - common[i-1]))
        elif common[i] ** 2 == common[i-1] * common[i+1]:
            answer = int(common[-1] * (common[i]/common[i-1]))
    return answer