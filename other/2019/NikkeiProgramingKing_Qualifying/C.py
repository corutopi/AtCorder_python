# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, AB):
    takahashi = 0
    aoki = 0
    for ab in AB:
        ab.append(sum(ab))
    AB.sort(key=lambda x: x[2], reverse=True)
    for i in range(N):
        if i % 2 == 0:
            takahashi += AB[i][0]
        else:
            aoki += AB[i][1]
    print(takahashi - aoki)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, AB)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
