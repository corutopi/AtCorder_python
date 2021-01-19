"""
解説を参考に作成
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
def solve(N, M):
    print(pow(10, N, M ** 2) // M % M)


if __name__ == '__main__':
    N, M = map(int, input().split())
    solve(N, M)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
