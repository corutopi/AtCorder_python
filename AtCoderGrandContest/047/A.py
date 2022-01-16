# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
import datetime
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    map_25 = [[0] * 20 for _ in range(45)]
    same_ok_num = 0
    A_25 = []
    for a in A:
        t = a
        num_2 = 0
        cnt = 0
        while t % 2 == 0 and t > 0:
            num_2 += 1
            t //= 2
            cnt += 1
        t = a
        num_5 = 0
        cnt = 0
        while t % 5 == 0 and t > 0:
            num_5 += 1
            t //= 5
            cnt += 1
        if a == 0:
            num_2, num_5 = 19, 19  # 0の場合強制的にすべての組み合わせでOKとなる
        if num_2 * 2 >= 18 and num_5 * 2 >= 18:
            same_ok_num += 1
        map_25[num_2][num_5] += 1
        A_25.append([num_2, num_5])

    map_25_cs = [[0] * 21 for _ in range(46)]
    for i in range(1, 46):
        for j in range(1, 21):
            map_25_cs[i][j] = map_25[i - 1][j - 1] + \
                              map_25_cs[i][j - 1] + map_25_cs[i - 1][j] - \
                              map_25_cs[i - 1][j - 1]

    ans = 0
    for n2, n5 in A_25:
        t2, t5 = max(0, 18 - n2), max(0, 18 - n5)
        ans += map_25_cs[-1][-1] - \
               map_25_cs[-1][t5] - map_25_cs[t2][-1] + \
               map_25_cs[t2][t5]
    print((ans - same_ok_num) // 2)


if __name__ == '__main__':
    N = int(input())
    A = [round(float(input()) * 10 ** 9) for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 2 * 10 ** 5
    # A = random_ints(N, 0, 10 ** 4)
    # A = [a * 10 ** 9 for a in A]
    # solve(N, A)

    # for i in range(20):
    #     a = float('0.' + str(i).zfill(9))
    #     print('{:.9f}'.format(a), round(a * 10 ** 9))
