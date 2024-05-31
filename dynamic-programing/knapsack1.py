# https://atcoder.jp/contests/dp/tasks/dp_d
# 6 15
# 6 5
# 5 6
# 6 4
# 6 6
# 3 5
# 7 2

weights = [6, 5, 6, 6, 3, 7]
costs = [5, 6, 4, 6, 5, 2]
W = 15
N = 6


def solve(N, W, weights, costs):  # -> Any:
    f = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if weights[i - 1] <= j:
                f[i][j] = max(f[i - 1][j], f[i - 1][j - weights[i - 1]] + costs[i - 1])
            else:
                f[i][j] = f[i - 1][j]

    return f[N][W]


res = solve(N, W, weights, costs)
print(res)
