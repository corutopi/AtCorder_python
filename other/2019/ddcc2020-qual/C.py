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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, K, s):
    dq = deque([[0, H - 1, 0, W - 1, 1]])
    cake = [[0] * W for _ in range(H)]
    n_cnt = 1
    while dq:
        t, b, l, r, n = dq.popleft()
        ichigo = []
        for h, w in ((h, w) for h in range(t, b + 1) for w in range(l, r + 1)):
            cake[h][w] = n
            if s[h][w] == '#':
                ichigo.append((h, w))
        if len(ichigo) > 1:
            i1, i2 = ichigo[len(ichigo) // 2 - 1], ichigo[len(ichigo) // 2]
            n_cnt += 1
            if i1[0] == i2[0]:
                dq.append([t, b, l, min(i1[1], i2[1]), n])
                dq.append([t, b, min(i1[1], i2[1]) + 1, r, n_cnt])
            else:
                dq.append([t, min(i1[0], i2[0]), l, r, n])
                dq.append([min(i1[0], i2[0]) + 1, b, l, r, n_cnt])
    [print(' '.join([str(i) for i in c])) for c in cake]
    # return cake


if __name__ == '__main__':
    H, W, K = map(int, input().split())
    s = [input() for _ in range(H)]
    solve(H, W, K, s)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints

    # testcnt = 0
    # while True:
    #     H, W, K = 300, 300, randint(1, 100)
    #     s = [['.'] * W for _ in range(H)]
    #     cnt = 0
    #     while cnt < K:
    #         h, w = randint(0, H - 1), randint(0, W - 1)
    #         if s[h][w] == '.':
    #             s[h][w] = '#'
    #             cnt += 1
    #     s = [''.join(ss) for ss in s]
    #     ans = solve(H, W, K, s)
    #     if sum([sum([1 if a == 0 else 0 for a in aa]) for aa in ans]) > 0:
    #         print('--cake----')
    #         [print(ss) for ss in s]
    #         print('--cat-----')
    #         [print(a) for a in ans]
    #         break
    #     testcnt += 1
    #     if testcnt % 10 == 0:
    #         print(testcnt)

    # H, W, K = 300, 300, randint(1, 100)
    # s = [['#'] * W for _ in range(H)]
    # solve(H, W, K, s)
