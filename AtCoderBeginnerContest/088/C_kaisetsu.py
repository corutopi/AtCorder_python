# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(C):
    a0 = 0
    b0, b1, b2 = C[0][0] - a0, C[0][1] - a0, C[0][2] - a0
    if (C[1][0] - b0 == C[1][1] - b1 == C[1][2] - b2) and (
            C[2][0] - b0 == C[2][1] - b1 == C[2][2] - b2):
        print('Yes')
        return
    print('No')


if __name__ == '__main__':
    C = [[int(i) for i in input().split()] for _ in range(3)]
    solve(C)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
