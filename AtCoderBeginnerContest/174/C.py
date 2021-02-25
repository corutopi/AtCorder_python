"""
解説を参考に作成
"""
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
def solve(K):
    visited = [0] * (K + 1)
    cnt = 0
    x = 0
    while True:
        cnt += 1
        x = (x * 10 + 7) % K
        if x == 0:
            print(cnt)
            break
        if visited[x] > 0:
            print(-1)
            break
        visited[x] = 1


if __name__ == '__main__':
    K = int(input())
    solve(K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
