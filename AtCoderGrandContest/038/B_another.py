# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def slide_minimum(l, k):
    """スライド最小値のlistを返す

    :param l: list
    :param k: min(l[i] ... l[i + k])
    :return:
    """
    from collections import deque
    dq = deque([])
    for i in range(k):
        while dq and l[dq[-1]] > l[i]:
            dq.pop()
        dq.append(i)
    re = []
    for i in range(len(l)):
        if i + k < len(l):
            while dq and l[dq[-1]] > l[i + k]:
                dq.pop()
            dq.append(i + k)
        if dq[0] == i - 1:
            dq.popleft()
        re.append(l[dq[0]])
    return re


def slide_maximum(l, k):
    """スライド最大値のlistを返す.
    O(len(l))

    :param l: list
    :param k: min(l[i] ... l[i + k])
    :return:
    """
    from collections import deque
    dq = deque([])
    for i in range(k):
        while dq and l[dq[-1]] < l[i]:
            dq.pop()
        dq.append(i)
    re = []
    for i in range(len(l)):
        if i + k < len(l):
            while dq and l[dq[-1]] < l[i + k]:
                dq.pop()
            dq.append(i + k)
        if dq[0] == i - 1:
            dq.popleft()
        re.append(l[dq[0]])
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, P):
    if N == K:
        print(1)
        return
    # 連続したK個が既に昇順になっていることの前計算
    isbig = [1 if P[i] > P[i + 1] else 0 for i in range(N - 1)]
    isbig_cs = [0]
    for ib in isbig:
        isbig_cs.append(isbig_cs[-1] + ib)
    smin = slide_minimum(P, K)
    smax = slide_maximum(P, K)
    ans = 1
    default_flg = 1 if isbig_cs[K - 1] - isbig_cs[0] == 0 else 0
    for i in range(N - K):
        if smin[i] == P[i] and smax[i] == P[i + K]:
            continue
        if isbig_cs[i + K] - isbig_cs[i + 1] == 0 and default_flg == 0:
            ans += 1
            default_flg = 1
        elif isbig_cs[i + K] - isbig_cs[i + 1] > 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    P = [int(i) + 1 for i in input().split()]
    solve(N, K, P)
    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
