# 解説を参考に作成

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
def solve(L, Q, cx):
    import bisect
    import array
    a = array.array('i', [0, L])
    for c, x in cx:
        # print(a)
        if c == 1:
            # bisect.insort_left(a, x)
            a.insert(bisect.bisect(a, x), x)
        else:
            t = bisect.bisect(a, x)
            print(a[t] - a[t - 1])


if __name__ == '__main__':
    L, Q = map(int, input().split())
    cx = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(L, Q, cx)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # L, Q = 10, 10
    # while True:
    #     cx = [[randint(1, 2), randint(1, L - 1)] for _ in range(Q)]
    #     solve(L, Q, cx)
