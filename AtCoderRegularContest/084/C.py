# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A, B, C):
    AB_cmb = [0] * N
    point_a = 0
    point_b = 0
    A.sort()
    B.sort()
    C.sort()
    while point_b < N:
        while point_a != N and A[point_a] < B[point_b]:
            point_a += 1
        AB_cmb[point_b] = point_a
        point_b += 1

    AB_cmb_sum = [0]
    for cmb in AB_cmb:
        AB_cmb_sum.append(AB_cmb_sum[-1] + cmb)

    point_b = 0
    point_c = 0
    ans = 0
    while point_c < N:
        while point_b != N and B[point_b] < C[point_c]:
            point_b += 1
        ans += AB_cmb_sum[point_b]
        point_c += 1

    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    solve(N, A, B, C)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
