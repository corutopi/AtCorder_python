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
def solve(N, A, K):
    A.sort(reverse=True)
    A.append(0)
    ans = 0
    for i in range(N):
        if A[i] == A[i + 1]:
            continue
        if K >= (A[i] - A[i + 1]) * (i + 1):
            ans += (A[i] + (A[i + 1] + 1)) * (A[i] - A[i + 1]) // 2 * (i + 1)
            K -= (A[i] - A[i + 1]) * (i + 1)
        else:
            kd, km = divmod(K, i + 1)
            ans += (A[i] + A[i] - kd + 1) * (A[i] - (A[i] - kd)) // 2 * (i + 1)
            ans += (A[i] - kd) * km
            break
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, A, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
