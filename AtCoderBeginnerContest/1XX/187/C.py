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
def solve(N, S):
    S = set(S)
    S = [s if s[0] != '!' else s[1:] for s in S]
    S.sort()
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            print(S[i])
            break
    else:
        print('satisfiable ')


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]
    solve(N, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2 * 10 ** 5
    # S = [('' if randint(0, 1) == 0 else '!') + random_str(3) for _ in range(N)]
    # solve(N, S)
