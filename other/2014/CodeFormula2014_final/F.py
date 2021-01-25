"""
以下を参考に作成
    https://kmjp.hatenablog.jp/entry/2014/10/08/1000
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
def solve():
    ans = [[0, 0] for _ in range(101)]
    for i in range(1, 25 + 1):
        x = (i - 1) % 5 + 1
        y = (i - 1) // 5 + 1
        l, u, r, d = 300 * (x - 1), 300 * y, 300 * x, 300 * (y - 1)
        ans[i] = [l + i, d + i]
        ans[51 - i] = [r - (51 - i), u - (51 - i)]
        ans[50 + i] = [r - (50 + i), d + (50 + i)]
        ans[101 - i] = [l + (101 - i), u - (101 - i)]
    [print(a[0], a[1]) for a in ans[1:]]


if __name__ == '__main__':
    solve()

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
