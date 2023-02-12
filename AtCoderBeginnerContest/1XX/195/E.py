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
def solve(N, S, X):
    S = list(reversed(S))
    X = list(reversed(X))
    mod_10_7 = 1
    ans = [1] + [0] * 6
    for i in range(N):
        s = int(S[i]) * mod_10_7 % 7
        # pattern add 0
        p_0 = ans
        # pattern add s
        p_s = [ans[(s + j) % 7] for j in range(7)]
        if X[i] == 'T':
            ans = [p_0[j] or p_s[j] for j in range(7)]
        else:
            ans = [p_0[j] and p_s[j] for j in range(7)]
        mod_10_7 = mod_10_7 * 10 % 7
    print('Takahashi' if ans[0] else 'Aoki')


if __name__ == '__main__':
    N = int(input())
    S = input()
    X = input()
    solve(N, S, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
