# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor, log2

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


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
def solve(N, A):
    A.sort()
    cnt_A = [[a, 0] for a in A]
    two_f = [2 ** i for i in range(32)]
    ans = 0
    for i in range(N - 1, -1, -1):
        if cnt_A[i][1] == 1: continue
        key = two_f[floor(log2(cnt_A[i][0])) + 1] - cnt_A[i][0]

        def solver(x):
            if cnt_A[x][0] == key:
                return True if cnt_A[x][1] == 0 else False
            else:
                return cnt_A[x][0] < key

        x = binary_search(0, i, solver)
        if cnt_A[x][0] == key and cnt_A[x][1] == 0 and x != i:
            ans += 1
            cnt_A[x][1] = 1
            cnt_A[i][1] = 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 4
    # A = [1,3,5,13]
    # solve(N, A)
