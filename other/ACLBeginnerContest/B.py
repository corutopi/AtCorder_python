# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(A,B,C,D):
    if C <= B <= D or A <= D <= B:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    A,B,C,D = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(A,B,C,D)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
