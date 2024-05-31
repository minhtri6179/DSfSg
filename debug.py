colors = input()
neededTime = list(map(int, input().split()))


def solve(colors, neededTime):
    res = 0
    pre = None
    for i in range(1, len(colors)):
        if colors[i] == colors[i - 1]:
            if pre:
                res -= neededTime[pre]

            if neededTime[i] < neededTime[i - 1]:
                res += neededTime[i]
                pre = i
            else:
                res += neededTime[i - 1]
                pre = i - 1
        else:
            pre = None
    if pre:
        res += neededTime[pre]
    return res


res = solve(colors, neededTime)
print(res)
