# 解説を参考に作成


def solve():
    N, M, Q = map(int, input().split())
    abcd = [[int(i) for i in input().split()] for _ in range(Q)]

    # AAs first is minmum M.
    def dfs(AA=[1], now_max=0):
        A = AA.copy()
        if len(A) == N + 1:
            new_max = 0
            for a, b, c, d in abcd:
                if A[b] - A[a] == c:
                    new_max += d
            now_max = max(now_max, new_max)
        else:
            for i in range(A[-1], M + 1):
                now_max = max(now_max, dfs(A + [i], now_max))
        return now_max

    print(dfs())


if __name__ == '__main__':
    solve()
