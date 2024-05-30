# https://atcoder.jp/contests/dp/tasks/dp_a
n = int(input())
heights = list(map(int, input().strip().split()))


def solve(heights, n):
    f = [0] * (n + 1)
    f[1] = 0
    f[2] = abs(heights[1] - heights[0])
    for i in range(3, n + 1):
        f[i] = min(
            f[i - 1] + abs(heights[i - 1] - heights[i - 2]),
            f[i - 2] + abs(heights[i - 1] - heights[i - 3]),
        )

    return f[n]


res = solve(heights, n)

print(res)
