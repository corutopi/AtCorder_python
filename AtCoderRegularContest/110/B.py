# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import math
# from decorator import stop_watch
#
#
# @stop_watch

body = 10 ** 10


def solve(N, T):
    if N == 1:
        if T == '1':
            return body * 2
        else:
            return body
    s = -1
    if T[:2] == '11':
        s = 0
    elif T[:2] == '10':
        s = 1
        T = '1' + T
    elif T[:2] == '01':
        s = 2
        T = '11' + T
    c1 = 0
    c0 = 1
    for t in T:
        if t == '1':
            c1 += 1
            c0 = 0
        if t == '0':
            c0 += 1
            if c1 != 2:
                s = -1
                break
            c1 = 0
        if c1 > 2 or c0 > 1:
            s = -1
            break
    if s < 0:
        return 0
    else:
        x = (s + N) // 3 + (1 if (s + N) % 3 > 0 else 0)
        return body - x + 1


def test(N, T):
    S = '110' * body
    ans = 0
    start = 0
    while True:
        s = S.find(T, start)
        if s >= 0:
            ans += 1
            start = s + 1
        else:
            break
    return ans


if __name__ == '__main__':
    N = int(input())
    T = input()
    print(solve(N, T))

    # # test
    # from random import randint
    # from func import random_str, random_ints
    #
    # while True:
    #     N = randint(1, 8)
    #     T = random_str(N, '10')
    #     if solve(N, T) != test(N, T):
    #         print(N)
    #         print(T)
    #         print(solve(N, T))
    #         print(test(N, T))
    #         break
