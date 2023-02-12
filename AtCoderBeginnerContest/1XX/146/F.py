# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, S):
    step = []
    cnt = 1
    for s in list(reversed(S))[1:]:
        if s == '0':
            step.append(cnt)
            cnt = 1
        else:
            cnt += 1

    if max(step) > M:
        print(-1)
        return
    cs_step = [0]
    for s in step:
        cs_step.append(cs_step[-1] + s)

    ans = []
    i = 0
    while i < len(cs_step) - 1:
        a = binary_search(i, len(cs_step),
                          lambda x: cs_step[x] - cs_step[i] <= M)
        ans.append(cs_step[a] - cs_step[i])
        i = a

    print(' '.join([str(a) for a in reversed(ans)]))


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = input()
    solve(N, M, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, M = 10 ** 5, randint(1, 10 ** 4)
    # S = random_str(N, '11111110')
    # solve(N, M, S)
    # solve(1, 1, '010')

