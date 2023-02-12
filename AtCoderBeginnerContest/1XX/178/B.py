# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(a, b, c, d):
    print(max(a * c, a * d, b * c, b * d))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    a, b, c, d = map(int, input().split())
    # Ai = [int(i) for i in input().split()]
    # Bi = [int(i) for i in input().split()]
    # ABi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(a, b, c, d)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
