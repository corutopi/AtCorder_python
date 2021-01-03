"""
解説を参考に作成
3の場合数でない場合に, 縦横どちらかに三等分するパターンが抜けていた. 2WA.
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W):
    ans = inf
    if H % 3 == 0 or W % 3 == 0:
        ans = 0
    else:
        a, b, c = (H // 3) * W, \
                  (H - (H // 3)) * (W // 2), \
                  (H - (H // 3)) * (W - W // 2)
        ans = min(ans, max(a, b, c) - min(a, b, c))
        a, b, c = (H // 3 + 1) * W, \
                  (H - (H // 3 + 1)) * (W // 2), \
                  (H - (H // 3 + 1)) * (W - W // 2)
        ans = min(ans, max(a, b, c) - min(a, b, c))
        a, b, c = (W // 3) * H, \
                  (W - (W // 3)) * (H // 2), \
                  (W - (W // 3)) * (H - H // 2)
        ans = min(ans, max(a, b, c) - min(a, b, c))
        a, b, c = (W // 3 + 1) * H, \
                  (W - (W // 3 + 1)) * (H // 2), \
                  (W - (W // 3 + 1)) * (H - H // 2)
        ans = min(ans, max(a, b, c) - min(a, b, c))
        a, b, c = H // 3, (H - H // 3) // 2, H - (H // 3) - ((H - H // 3) // 2)
        a, b, c = a * W, b * W, c * W
        ans = min(ans, max(a, b, c) - min(a, b, c))
        a, b, c = W // 3, (W - W // 3) // 2, W - (W // 3) - ((W - W // 3) // 2)
        a, b, c = a * H, b * H, c * H
        ans = min(ans, max(a, b, c) - min(a, b, c))

    print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    solve(H, W)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
