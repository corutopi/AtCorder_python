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
def solve(T, AS):
    for a, s in AS:
        if a > s:
            print('No')
            continue
        move_up = 0
        for i in range(61):
            ax = a >> i & 1
            sx = s >> i & 1
            if ax == 0 and sx == 0:
                pass
            elif ax == 0 and sx == 1:
                move_up = 0
            elif ax == 1 and sx == 0:
                if move_up == 1:
                    print('No')
                    break
                else:
                    move_up = 1
            elif ax == 1 and sx == 1:
                if move_up == 0:
                    print('No')
                    break
        else:
            print('Yes')


def solve_sub(a, s):
    if a > s:
        return 'No'
    move_up = 0
    for i in range(61):
        ax = a >> i & 1
        sx = s >> i & 1
        if ax == 0 and sx == 0:
            pass
        elif ax == 0 and sx == 1:
            move_up = 0
        elif ax == 1 and sx == 0:
            if move_up == 1:
                break
            else:
                move_up = 1
        elif ax == 1 and sx == 1:
            if move_up == 0:
                break
    else:
        return 'Yes'
    return 'No'


def solve_force(a, s):
    for i, j in ((i, j) for i in range(s + 1) for j in range(s + 1)):
        if i & j == a and i + j == s:
            break
    else:
        return 'No'
    return 'Yes'


if __name__ == '__main__':
    T = int(input())
    AS = [[int(i) for i in input().split()] for _ in range(T)]
    solve(T, AS)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # while True:
    #     a, s = random_ints(2, 0, 50)
    #     if solve_sub(a, s) != solve_force(a, s):
    #         print(a, s)
    #         break
