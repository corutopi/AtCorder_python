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
def solve(N,K,A):
    S = sorted(A)
    for k in range(K):
        tmp = dict()
        for i in range(k, N, K):
            tmp.setdefault(A[i], 0)
            tmp.setdefault(S[i], 0)
            tmp[A[i]] += 1
            tmp[S[i]] += -1
        for t in tmp.values():
            if t != 0:
                print('No')
                return
    print('Yes')


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N,K,A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2 * 10 ** 5
    # K = 200000 - 1
    # A = sorted([randint(1, 1000000) for _ in range(N)])
    # solve(N, K, A)
