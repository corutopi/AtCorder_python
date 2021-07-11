"""
解説を参考に作成.
実装は解説通りになっているはずだが, pypyでもTLEになっちゃう...
@todo コンテスト終了後に他の人のソースを見てみる
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
import math

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


def declination(x, y, center_x=0, center_y=0):
    """偏角(degrees)"""
    from math import atan2, degrees
    return degrees(atan2(y - center_y, x - center_x)) % 360


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, XY):
    ans = 0
    for b in range(N):
        # sort
        vec = []
        for i in range(N):
            if i == b: continue
            vec.append(declination(XY[i][0], XY[i][1], XY[b][0], XY[b][1]))
        vec.sort()

        # binary search
        for a in range(N):
            if a == b: continue
            a_vec = declination(XY[a][0], XY[a][1], XY[b][0], XY[b][1])
            target = (a_vec + 180) % 360
            near1 = binary_search(0, len(vec), lambda x: vec[x] <= target)
            near2 = (near1 + 1) % len(vec)
            ans = max(ans,
                      min(abs(a_vec - vec[near1]),
                          360 - abs(a_vec - vec[near1])),
                      min(abs(a_vec - vec[near2]),
                          360 - abs(a_vec - vec[near2])))

    print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, XY)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2000
    # XY = [[randint(1, 10 ** 9) for _ in range(2)] for _ in range(N)]
    # solve(N, XY)
