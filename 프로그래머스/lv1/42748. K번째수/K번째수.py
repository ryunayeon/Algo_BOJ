def solution(array, commands):
    ans = []
    for lst in commands:
        i = lst[0]
        j = lst[1]
        k = lst[2]
        arr = array[i-1: j]
        arr.sort()
        ans.append(arr[k-1])
    return ans