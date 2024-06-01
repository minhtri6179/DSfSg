import random


def solve(colors, neededTime):
    res = 0
    pre = None
    for i in range(1, len(colors)):
        if colors[i] == colors[i - 1]:
            j = i - 1
            max_val = 0
            while j < len(colors) and colors[j] == colors[i]:
                max_val = max(max_val, neededTime[j])
                j += 1
            res += max_val

    return res


res = solve(colors, neededTime)
print(res)
