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
def solve(S1, S2):
    print('No' if S1[0] == S2[1] == '.' or S1[1] == S2[0] == '.' else 'Yes')


if __name__ == '__main__':
    S1, S2 = input(), input()

    solve(S1, S2)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
