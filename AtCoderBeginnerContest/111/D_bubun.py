# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, XY):
    tmp = 0
    for x, y in XY:
        tmp += (abs(x) + abs(y)) % 2
    if tmp % N != 0:
        print(-1)
        return
    m = 20 if tmp == 0 else 21
    d = [1] * m
    w = []
    for x, y in XY:
        mm = m
        ww = ''
        ww += ('R' if x >= 0 else 'L') * abs(x)
        ww += ('U' if y >= 0 else 'D') * abs(y)
        ww += 'RL' * ((mm - (abs(x) + abs(y))) // 2)
        w.append(ww)
    print(m)
    print(' '.join([str(di) for di in d]))
    [print(wi) for wi in w]


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, XY)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
