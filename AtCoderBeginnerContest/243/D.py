# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X, S):
    T = deque()
    for s in S:
        if len(T) == 0:
            T.append(s)
        else:
            if s == 'U' and T[-1] != 'U':
                T.pop()
            else:
                T.append(s)
    ans = X
    for t in T:
        if t == 'U':
            ans //= 2
        elif t == 'L':
            ans *= 2
        elif t == 'R':
            ans = ans * 2 + 1
    print(ans)


if __name__ == '__main__':
    N, X = map(int, input().split())
    S = input()
    solve(N, X, S)

    # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 10 ** 6
    # X = 10 ** 18
    # S = 'R' * (N // 2) + 'U' * (N // 2)
    # solve(N, X, S)
