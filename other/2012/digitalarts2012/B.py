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
def solve(C):
    alp = 'Xabcdefghijklmnopqrstuvwxyz'
    alp_dct = {alp[i]: i for i in range(1, len(alp))}
    C_num = [alp_dct[c] for c in C] + [0] * (20 - len(C))

    for i in range(len(C_num) - 1):
        if C_num[i] > 1 and 26 > C_num[i + 1]:
            C_num[i] -= 1
            C_num[i + 1] += 1
            print(''.join([alp[i] for i in C_num if i != 0]))
            return

    for i in range(len(C_num) - 1, 0, -1):
        low = 1
        if i == len(C_num) - 1 or C_num[i + 1] == 0:
            low = 0
        if C_num[i] > low and 26 > C_num[i - 1]:
            C_num[i] -= 1
            C_num[i - 1] += 1
            print(''.join([alp[i] for i in C_num if i != 0]))
            return

    print('NO')


if __name__ == '__main__':
    C = input()
    solve(C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
