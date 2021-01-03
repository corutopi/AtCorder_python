# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(T, NAB):
    mod = 10 ** 9 + 7
    for n, a, b in NAB:
        x4 = (n - a - b + 2) * (n - a - b + 1) // 2 if n - a - b >= 0 else 0
        x3 = x4 * 2
        x2 = (n - a + 1) * (n - b + 1) - x3
        x1 = x2 ** 2
        print(((n - a + 1) ** 2 * (n - b + 1) ** 2 - x1) % mod)


if __name__ == '__main__':
    # S = input()
    T = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    NAB = [[int(i) for i in input().split()] for _ in range(T)]
    solve(T, NAB)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
