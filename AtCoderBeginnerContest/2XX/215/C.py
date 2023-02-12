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
def solve(S, K):
    selected = [0] * len(S)
    dicts = []

    def dfs(s, depth=0):
        if depth == len(S):
            dicts.append(s)
            return
        for i in range(len(S)):
            if selected[i] == 0:
                selected[i] = 1
                dfs(s + S[i], depth + 1)
                selected[i] = 0

    dfs("")
    dicts = list(set(dicts))
    dicts.sort()
    print(dicts[K - 1])


if __name__ == '__main__':
    S, K = input().split()
    K = int(K)
    solve(S, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
