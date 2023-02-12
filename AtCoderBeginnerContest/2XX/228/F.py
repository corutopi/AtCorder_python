# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def slide_maximum(l, k):
    """スライド最大値のlistを返す

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
def solve(H, W, h1, w1, h2, w2, A):
    cs_A = [[0] * (W + 1) for _ in range(H + 1)]
    for h, w in ((h, w) for h in range(H) for w in range(W)):
        cs_A[h + 1][w + 1] = (A[h][w]
                              + cs_A[h][w + 1] + cs_A[h + 1][w]
                              - cs_A[h][w])
    h2, w2 = min(h1, h2), min(w1, w2)
    # 高橋君の各マスの手
    Taka = [[0] * W for _ in range(H)]
    for h, w in ((h, w) for h in range(H) for w in range(W)):
        HH, WW = min(H, h + h1), min(W, w + w1)
        Taka[h][w] = (cs_A[HH][WW] - cs_A[HH][w] - cs_A[h][WW] + cs_A[h][w])
    # 青木君の各マスの手
    Aoki = [[0] * W for _ in range(H)]
    for h, w in ((h, w) for h in range(H) for w in range(W)):
        HH, WW = min(H, h + h2), min(W, w + w2)
        Aoki[h][w] = (cs_A[HH][WW] - cs_A[HH][w] - cs_A[h][WW] + cs_A[h][w])
    # 青木君の各マスの手の区間最大値
    Aoki_max = [slide_maximum(a, w1 - w2) for a in Aoki]
    x = h1 - h2
    for w in range(W):
        dq = deque([])
        for i in range(x):
            while dq and Aoki_max[dq[-1]][w] < Aoki_max[i][w]:
                dq.pop()
            dq.append(i)
        for i in range(H):
            if i + x < H:
                while dq and Aoki_max[dq[-1]][w] < Aoki_max[i + x][w]:
                    dq.pop()
                dq.append(i + x)
            if dq[0] == i - 1:
                dq.popleft()
            Aoki_max[i][w] = Aoki_max[dq[0]][w]
    # 答え
    ans = 0
    for h, w in ((h, w) for h in range(H) for w in range(W)):
        ans = max(ans, Taka[h][w] - Aoki_max[h][w])
    print(ans)


if __name__ == '__main__':
    H, W, h1, w1, h2, w2 = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    solve(H, W, h1, w1, h2, w2, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # H, W = 1000, 1000
    # h1, w1, h2, w2 = randint(1, H), randint(1, W), randint(1, H), randint(1, W)
    # A = [[randint(1, 10 ** 9) for _ in range(W)] for _ in range(H)]
    # solve(H, W, h1, w1, h2, w2, A)
