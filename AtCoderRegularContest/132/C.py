"""
解説AC
変則dp
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

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
def solve(N, D, A):
    A = [i for i in range(D)] + [a + D - 1 if a != -1 else a for a in A] + \
        [N + D + i for i in range(D)]
    used = [0] * len(A)
    for a in A:
        used[a] = 1 if a != -1 else used[a]
    dp = [0] * 2 ** (2 * D + 1)
    dp[(1 << (D + 1)) - 1] = 1
    for i in range(D, N + D):
        dp_new = [0] * 2 ** (2 * D + 1)
        for j in range(2 ** (2 * D + 1)):
            # i - D - 1 が使用されていないケースはスキップ
            # ここで枝刈りしておかないとpythonだと間に合わない
            if not j & 1: continue
            if A[i] != -1:
                # 数字が固定されている場合
                if not (j >> (A[i] - i + D + 1) & 1):
                    tmp = j >> 1 | 1 << (A[i] - i + D)
                    dp_new[tmp] += dp[j]
                    dp_new[tmp] %= mod2
            else:
                # 固定されていない(-1)の場合
                for k in range(2 * D + 1):
                    if used[i + k - D]: continue  # 使用済みの数字は使えない
                    if not (j >> (k + 1)) & 1:
                        tmp = j >> 1 | 1 << k
                        dp_new[tmp] += dp[j]
                        dp_new[tmp] %= mod2
        dp = dp_new
    print(sum(dp))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, D = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, D, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
