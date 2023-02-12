# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, K, A, UV):
    tree = [[] for _ in range(N + 1)]
    for i, uv in enumerate(UV):
        u, v = uv
        tree[u].append([i, v])
        tree[v].append([i, u])
    C = [0] * (N - 1)
    for i in range(M - 1):
        goal = A[i + 1]

        def dfs(p, n):
            if n == goal:
                return True
            for t in tree[n]:
                if t[1] == p: continue
                if dfs(n, t[1]):
                    C[t[0]] += 1
                    return True
            return False

        dfs(0, A[i])
    # print(C)
    S = sum(C)
    if (S + K) % 2 == 1 or S + K < 0:
        # R + B = S, R - B = K が成り立つ場合, S + K は偶数かつ0以上
        # -> これに当てはまらない場合, 条件を達成できない
        print(0)
        return
    tag = (S + K) // 2
    dp = [0] * (tag + 1)
    dp[0] = 1
    if C[0] <= tag: dp[C[0]] += 1
    for c in C[1:]:
        new_dp = [0] * (tag + 1)
        for j in range(tag + 1):
            new_dp[j] = (dp[j] + (dp[j - c] if j - c >= 0 else 0)) % mod2
        dp = new_dp
    print(dp[-1])


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    UV = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, M, K, A, UV)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
