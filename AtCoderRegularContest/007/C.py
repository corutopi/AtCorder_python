# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def loop_shift(n, s, digit=None):
    """
    n を 2進数表記で s だけ右方向にループさせた結果を返す.
    :param n:
    :param s:
    :param digit:
    :return:
    """
    if digit is None:
        digit = len(bin(n)) - 2
    for _ in range(s):
        d = n & 1
        n = n >> 1
        n += d * 2 ** (digit - 1)
    return n


# from decorator import stop_watch
#
#
# @stop_watch
def solve(c):
    N = len(c)
    c = int(c.replace('o', '0').replace('x', '1'), 2)
    c_loop = [loop_shift(c, i, N) for i in range(N)]

    ans = N
    for i in range(2 ** (N - 1)):
        tmp = bin(i).count('1') + 1
        tv = c

        for j in range(N):
            if i >> j & 1 == 1:
                tv = tv & c_loop[j + 1]

        if tv == 0:
            ans = min(ans, tmp)

    print(ans)


if __name__ == '__main__':
    c = input()
    solve(c)
    # print(loop_shift(5, 1))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
