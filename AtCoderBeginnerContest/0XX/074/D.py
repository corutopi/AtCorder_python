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
def solve(N, A):
    ans = sum([sum(a) for a in A])
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j or j == k or k == i:
                    continue
                if A[i][j] == A[i][k] + A[k][j]:
                    ans -= A[i][j]
                    break
                if A[j][k] > A[j][i] + A[i][k]:
                    print(-1)
                    return
    print(ans // 2)


if __name__ == '__main__':
    N = int(input())
    A = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
