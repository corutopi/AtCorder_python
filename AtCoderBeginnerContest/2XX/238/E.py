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
def solve(N, Q, lr):
    L, R = 0, 1
    map_l = [[] for _ in range(N + 1)]
    map_r = [[] for _ in range(N + 1)]
    for i in range(Q):
        l, r = lr[i]
        map_l[l].append(i)
        map_r[r].append(i)
    can_identify = [0] * (N + 1)
    can_identify[0] = 1
    dq = deque([0])
    while dq:
        now = dq.popleft()
        if now < N:
            for ml in map_l[now + 1]:
                l, r = lr[ml]
                if can_identify[r]: continue
                can_identify[r] = 1
                dq.append(r)
        for mr in map_r[now]:
            l, r = lr[mr]
            if can_identify[l - 1]: continue
            can_identify[l - 1] = 1
            dq.append(l - 1)
    print('Yes' if can_identify[N] else 'No')


if __name__ == '__main__':
    N, Q = map(int, input().split())
    lr = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, lr)

    # # test
    # from random import randint
    # # import string
    # # import tool.testcase as tt
    # # from tool.testcase import random_str, random_ints
    #
    # N = 2 * 10 ** 5
    # Q = 2 * 10 ** 5
    # lr = []
    # for _ in range(Q):
    #     l, r = randint(1, N), randint(1, N)
    #     lr.append([min(l, r), max(l, r)])
    # solve(N, Q, lr)
