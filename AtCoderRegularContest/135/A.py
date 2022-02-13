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
def solve(X):
    d = dict()

    def dfs(x):
        if d.get(x, 0) != 0:
            return d[x]
        if x <= 4:
            return x
        a, b = divmod(x, 2)
        b += a
        r = (dfs(a) * dfs(b)) % mod2
        d[x] = r
        return r

    print(dfs(X))


if __name__ == '__main__':
    X = int(input())
    solve(X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
