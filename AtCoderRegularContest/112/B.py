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
def solve(B, C):
    if B == 0:
        num_max = -(B - ((C - 1) // 2))
        num_min = B - (C // 2)
        print(num_max - num_min + 1)
        return
    elif B > 0:
        # 全部引く
        plus_min = B - (C // 2)
        # -1倍して引けるだけ引いて最後に-1倍
        plus_max = B if C < 4 else B + (C - 2) // 2
        # -1倍して全部引く
        minus_min = -B - ((C - 1) // 2)
        # 引けるだけ引いて最後に-1倍
        minus_max = -(B - ((C - 1) // 2))
        print(plus_max - minus_min + 1 if minus_max >= plus_min else
              plus_max - plus_min + 1 + minus_max - minus_min + 1)
    elif B < 0:
        # 全部引く
        minus_min = B - (C // 2)
        # -1倍して引けるだけ引いて最後に-1倍
        minus_max = B if C < 4 else B + (C - 2) // 2
        # -1倍して全部引く
        plus_min = -B - ((C - 1) // 2)
        # 引けるだけ引いて最後に-1倍
        plus_max = -(B - ((C - 1) // 2))
        print(plus_max - minus_min + 1 if minus_max >= plus_min else
              plus_max - plus_min + 1 + minus_max - minus_min + 1)


if __name__ == '__main__':
    B, C = map(int, input().split())
    solve(B, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
