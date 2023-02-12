# 解説を参考に作成


def solve(N, X, Y):
    ans = [0] * (N)

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            k = min(abs(j - i), abs(X - i) + 1 + abs(Y - j))
            ans[k] += 1

    for i in ans[1:]:
        print(i)


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    solve(N, X, Y)
