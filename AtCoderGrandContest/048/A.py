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
def solve(T, S):
    for s in S:
        if 'atcoder' < s:
            print(0)
            continue
        if s.count('a') == len(s):
            print(-1)
            continue
        x = 0
        while s[x] == 'a':
            x += 1
        if 't' < s[x]:
            print(x - 1)
        else:
            print(x)


if __name__ == '__main__':
    T = int(input())
    S = [input() for _ in range(T)]
    solve(T, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
