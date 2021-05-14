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
def solve(S):
    if len(S) == 1:
        print(0)
    elif len(S) % 2 == 1:
        print(10 ** (len(S) // 2) - 1)
    else:
        if len(S) % 2 == 0:
            N1, N2 = int(S[:len(S) // 2]), int(S[len(S) // 2:])
            if N1 > N2:
                print(N1 - 1)
            else:
                print(N1)


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # for i in range(1, 10 ** 4):
    #     print('({})'.format(i))
    #     solve(str(i))
