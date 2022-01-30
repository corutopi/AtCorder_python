# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N ,S):
    # ans = str(N)
    dq = deque([N])
    for i in range(N - 1, -1, -1):
        if S[i] == 'L':
            # ans = ans + str(i)
            dq.append(i)
        else:
            # ans = str(i) + ans
            dq.appendleft(i)
    print(*list(dq))


if __name__ == '__main__':
    N = int(input())
    S = input()
    solve(N, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 5 * 10 ** 5
    # S = random_str(N, 'LR')
    # solve(N, S)
