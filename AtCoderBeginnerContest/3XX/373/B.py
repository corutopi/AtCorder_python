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
def solve(A):
    push_key_list = 'BCDEFGHIJKLMNOPQRSTUVWXYZ'
    finger_position = A.find('A')
    cost = 0
    for p in push_key_list:
        next_finger_position = A.find(p)
        cost += abs(next_finger_position - finger_position)
        finger_position = next_finger_position
    print(cost)


if __name__ == '__main__':
    A = input()
    # N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
