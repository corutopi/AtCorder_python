# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(r1, c1, r2, c2):
    ans = 3

    def isreach(r, c, rr, cc):
        re = False
        # 移動A
        if r + c == rr + cc:
            re = True
        # 移動B
        elif r - c == rr - cc:
            re = True
        # 移動C
        elif abs(r - rr) + abs(c - cc) <= 3:
            re = True
        return re

    if r1 == r2 and c1 == c2:
        ans = 0
    elif isreach(r1, c1, r2, c2):
        ans = 1
    else:
        if (r1 + c1) % 2 == (r2 + c2) % 2:
            # 移動A + 移動B
            ans = 2
        elif abs(r1 - r2) + abs(c1 - c2) <= 6:
            # 移動C + 移動C
            ans = 2
        elif abs((r1 + c1) - (r2 + c2)) <= 3:
            # 移動A + 移動C
            ans = 2
        elif abs((r1 - c1) - (r2 - c2)) <= 3:
            # 移動B + 移動C
            ans = 2
    print(ans)


if __name__ == '__main__':
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    solve(r1, c1, r2, c2)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
