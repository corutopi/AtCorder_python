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

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Q, X, W, K):
    cumsum = [0]
    for w in W:
        cumsum.append(cumsum[-1] + w)
    L = []
    ichi = [-1] * N
    ichi[0] = 0
    now = 0
    while True:
        jaga = 0
        x = X
        if x > cumsum[-1] - cumsum[now]:
            jaga += N - now
            x -= cumsum[-1] - cumsum[now]
            now = 0
        if x > cumsum[-1]:
            aa, x = divmod(x, cumsum[-1])
            jaga += N * aa
        tmp = binary_search(N, 0, lambda l: cumsum[l] - cumsum[now] >= x)
        jaga += tmp - now
        now = tmp % N
        L.append(jaga)
        if ichi[now] == -1:
            ichi[now] = len(L)
        else:
            L_mae = L[:ichi[now]]
            L_loop = L[ichi[now]:]
            break
    for k in K:
        if k <= len(L_mae):
            print(L_mae[k - 1])
        else:
            k -= len(L_mae)
            print(L_loop[(k - 1) % len(L_loop)])


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, Q, X = map(int, input().split())
    W = [int(i) for i in input().split()]
    K = [int(input()) for _ in range(Q)]
    solve(N, Q, X, W, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
