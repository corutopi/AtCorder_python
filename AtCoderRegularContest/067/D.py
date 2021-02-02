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
def solve(N, A, B, X):
    ans = 0
    for i in range(N - 1):
        if abs(X[i] - X[i + 1]) * A <= B:
            ans += abs(X[i] - X[i + 1]) * A
        else:
            ans += B

    print(ans)


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    X = [int(i) for i in input().split()]
    solve(N, A, B, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
