# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    ans = 0
    ans_cnt = 0
    for i in range(2, max(A) + 1):
        tmp_cnt = 0
        for a in A:
            if a % i == 0:
                tmp_cnt += 1
        if tmp_cnt > ans_cnt:
            ans = i
            ans_cnt = tmp_cnt
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
