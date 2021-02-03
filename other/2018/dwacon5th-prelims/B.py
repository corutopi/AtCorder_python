# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor, log2
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A):
    A_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)

    numbers = []
    max_n = 0
    for i, j in ((i, j) for i in range(N) for j in range(i + 1, N + 1)):
        numbers.append(A_sum[j] - A_sum[i])
        max_n = max(max_n, numbers[-1])

    cnd = numbers
    for k in range(ceil(log2(max_n)), -1, -1):
        new_cnd = []
        for c in cnd:
            if c >> k & 1:
                new_cnd.append(c)
        if len(new_cnd) >= K:
            cnd = new_cnd

    ans = cnd[0]
    for c in cnd:
        ans &= c
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 1000
    # K = randint(1, (N * (N + 1)) // 2)
    # A = [randint(1, 10 ** 9) for _ in range(N)]
    # solve(N, K, A)
