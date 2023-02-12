# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, DD):
    count = 0
    for d1, d2 in DD:
        if d1 == d2:
            count += 1
        else:
            count = 0
        if count >= 3:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    DD = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, DD)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
