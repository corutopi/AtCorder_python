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
def solve(p, q):
    length = [0,3,4,8,9,14,23]
    position = 'ABCDEFG'
    pp, qq = position.find(p), position.find(q)
    pp, qq = min(pp, qq), max(pp, qq)
    print(length[qq] - length[pp])


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    p, q = input().split()
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(p, q)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
