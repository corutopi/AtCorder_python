# 解説を参考に作成_解法2
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
    cake = [[0] * W for _ in range(H)]
    horizon = []
    ichigo_flg = False
    x = 0
    for h in range(H):
        if s[h].find('#') >= 0:
            if ichigo_flg:
                horizon.append((x, h))
                x = h
            else:
                ichigo_flg = True
    horizon.append((x, H))

    cnt = 1
    for t, b in horizon:
        ichigo_flg = False
        for w in range(W):
            if '#' in [s[h][w] for h in range(t, b)]:
                if ichigo_flg:
                    cnt += 1
                else:
                    ichigo_flg = True
            for h in range(t, b):
                cake[h][w] = cnt
        cnt += 1

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
