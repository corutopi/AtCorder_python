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
def solve(N, S, T):
    if S.count('0') != T.count('0'):
        print(-1)
        return
    s0, t0 = 0, 0
    ans = 0
    for i in range(N):
        if S[i] == '0' or T[i] == '0':
            if S[i] == T[i]:
                if s0 == t0 == 0:
                    continue
                else:
                    s0 += 1
                    t0 += 1
            else:
                s0 += int(not int(S[i]))
                t0 += int(not int(T[i]))
                if s0 == t0:
                    ans += s0
                    s0, t0 = 0, 0
    print(ans)


if __name__ == '__main__':
    N = int(input())
    S, T = input(), input()
    solve(N, S, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
