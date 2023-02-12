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
def solve(K, S, T):
    yama = [0] + [K] * 9
    tefuda_s = [0] * 10
    tefuda_t = [0] * 10
    for i in range(len(S) - 1):
        tefuda_s[int(S[i])] += 1
        yama[int(S[i])] -= 1
        tefuda_t[int(T[i])] += 1
        yama[int(T[i])] -= 1
    yama_mai = sum(yama)

    def score(x):
        return sum([i * 10 ** x[i] for i in range(10)])

    ans = 0
    for s, t in ((s, t) for s in range(1, 10) for t in range(1, 10)):
        yama[s] -= 1
        yama[t] -= 1
        if yama[t] < 0 or yama[s] < 0:
            yama[s] += 1
            yama[t] += 1
            continue
        yama[s] += 1
        yama[t] += 1

        tefuda_s[s] += 1
        tefuda_t[t] += 1
        sss = score(tefuda_s)
        ttt = score(tefuda_t)
        if score(tefuda_s) > score(tefuda_t):
            n = yama[s]
            yama[s] -= 1
            m = yama[t]
            yama[s] += 1
            ans += n * m
        tefuda_s[s] -= 1
        tefuda_t[t] -= 1

    print(ans / (yama_mai * (yama_mai - 1)))


if __name__ == '__main__':
    K = int(input())
    S, T = input(), input()
    solve(K, S, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
