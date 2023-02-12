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
def solve(N, A):
    stack = [[0, 0]]
    cnt = 0
    for a in A:
        cnt += 1
        if a == stack[-1][0]:
            stack[-1][1] += 1
        else:
            stack.append([a, 1])
        if stack[-1][0] == stack[-1][1]:
            cnt -= stack[-1][1]
            stack.pop()
        print(cnt)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2 * 10 ** 5
    # A = random_ints(N, 1, 10)
    # solve(N, A)
