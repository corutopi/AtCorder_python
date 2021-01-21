# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, D):
    time = [0] * 13
    time[0] += 1  # takahashi
    for d in D:
        time[d] += 1

    if 2 < max(time) or 1 < time[0] or 1 < time[12]:
        print(0)
        return

    ans = 0
    for i in range(2 ** 13):
        register = []
        for j in range(13):
            if j in [0, 12]:
                if 0 < time[j]:
                    register.append(j)
                continue
            if time[j] == 2:
                register += [j, 24 - j]
                continue
            if time[j] == 1:
                if i >> j & 1:
                    register.append(j)
                else:
                    register.append(24 - j)
        gene = ((a, b) for a in register for b in register if a != b)
        tmp = 12
        for a, b in gene:
            tmp = min(min(abs(a - b), abs(abs(a - b) - 24)), tmp)
        ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    N = int(input())
    D = [int(i) for i in input().split()]
    solve(N, D)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
