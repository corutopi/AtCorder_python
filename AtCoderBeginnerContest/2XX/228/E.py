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
def solve(N, K, M):
    if M % mod2 == 0:
        print(0)
    else:
        x = pow(K, N, mod2 - 1)
        print(pow(M, x, mod2))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K, M = map(int, input().split())
    solve(N, K, M)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
