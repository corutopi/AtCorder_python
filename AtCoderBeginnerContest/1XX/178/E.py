# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, xyi):
    plus_max = - 10 ** 18
    plus_min = + 10 ** 18
    minus_max = - 10 ** 18
    minus_min = + 10 ** 18

    for x, y in xyi:
        plus_max = max(plus_max, x + y)
        plus_min = min(plus_min, x + y)
        minus_max = max(minus_max, x - y)
        minus_min = min(minus_min, x - y)
    ans = max(abs(plus_max - plus_min), abs(minus_max - minus_min))
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # Ai = [int(i) for i in input().split()]
    # Bi = [int(i) for i in input().split()]
    xyi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, xyi)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
