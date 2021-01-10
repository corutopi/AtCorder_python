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
def solve(X, Y):
    if X >= Y:
        print(X - Y)
        return
    func_map = {}

    def func(y):
        re = func_map.get(y)
        if re is not None:
            return re

        if X >= y:
            re = X - y
        elif y % 2 == 1:
            re = min(abs(X - y),
                     func((y + 1) // 2) + 2,
                     func((y - 1) // 2) + 2)
        else:
            re = min(abs(X - y), func(y // 2) + 1)
        func_map[y] = re
        return re

    print(func(Y))


def checker(X, Y):
    dp = [0] * (Y + 3)
    for i in range(X):
        dp[i] = abs(X - i)
    for i in range(X + 1, Y + 3):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
            dp[i - 1] = min(dp[i - 1], dp[i] + 1)
    # print(dp[Y])
    return dp[Y]


if __name__ == '__main__':
    X, Y = map(int, input().split())
    solve(X, Y)
    # solve(1, 10 ** 18)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # flg = False
    # for i in range(1, 100000):
    #     for j in range(1, i):
    #         solve(j, i)
    #         # if solve(j, i) != checker(j, i):
    #         #     print(j, i)
    #         #     print(solve(j, i))
    #         #     print(checker(j, i))
    #         #     flg = True
    #         #     break
    #     if flg:
    #         break
    # solve()
