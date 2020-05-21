# 解説を参考に作成


def solve():
    N, A, B, C = map(int, input().split())
    ls = [int(input()) for n in range(N)]

    def dfs(n=0, a=0, b=0, c=0, now_mp=0, min_mp=float('inf')):
        if n == N:
            if 0 in [a, b, c]:
                return min_mp
            else:
                return min(abs(A - a) + abs(B - b) + abs(C - c) - 30 + now_mp,
                           min_mp)
        result1 = dfs(n + 1, a, b, c, now_mp, min_mp)
        result2 = dfs(n + 1, a + ls[n], b, c, now_mp + 10, min_mp)
        result3 = dfs(n + 1, a, b + ls[n], c, now_mp + 10, min_mp)
        result4 = dfs(n + 1, a, b, c + ls[n], now_mp + 10, min_mp)
        return min(result1, result2, result3, result4)

    print(dfs())


if __name__ == '__main__':
    solve()
