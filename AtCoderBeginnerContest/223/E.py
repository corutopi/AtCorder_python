# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def upperround(x, y):
    a, b = divmod(x, y)
    return a + bool(b)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(X, Y, A, B, C):
    # 縦3つ
    if upperround(A, X) + upperround(B, X) + upperround(C, X) <= Y:
        print('Yes')
        return
    # 横3つ
    if upperround(A, Y) + upperround(B, Y) + upperround(C, Y) <= X:
        print('Yes')
        return
    # ┣, ┳
    for l, m, n in ([A, B, C], [B, C, A], [C, A, B]):
        t = upperround(l, Y)
        if X - t <= 0: continue
        u = upperround(m, (X - t))
        if Y - u <= 0: continue
        if (X - t) * (Y - u) >= n:
            print('Yes')
            return
        t = upperround(l, X)
        if Y - t <= 0: continue
        u = upperround(m, (Y - t))
        if X - u <= 0: continue
        if (Y - t) * (X - u) >= n:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    X, Y, A, B, C = map(int, input().split())
    solve(X, Y, A, B, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
