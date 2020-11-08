# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    ans = -1
    all_sum = sum([int(i) for i in list(str(N))])
    keta = len(str(N))
    for i in range(0, 2 ** keta - 1):
        s = bin(i)
        tmp_sum = all_sum
        tmp_cnt = bin(i).count('1')
        for j in range(len(s) - 2):
            if i >> j & 1:
                tmp_sum -= (N // (10 ** j)) % 10
        if tmp_sum % 3 == 0:
            if ans == -1:
                ans = tmp_cnt
            ans = min(ans, tmp_cnt)
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
