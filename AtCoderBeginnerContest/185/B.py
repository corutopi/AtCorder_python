# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, T, AB):
    now = 0
    battery = N
    for a, b in AB:
        battery -= a - now
        if battery <= 0:
            print('No')
            return
        battery += b - a
        battery = min(battery, N)
        now = b
    battery -= T - now
    if battery <= 0:
        print('No')
        return
    print('Yes')


if __name__ == '__main__':
    N, M, T = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, T, AB)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
