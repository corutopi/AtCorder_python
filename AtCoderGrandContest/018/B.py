# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, A):
    like = [0] * N
    hold = [1] * M
    ans = N
    for _ in range(M):
        join = [0] * M
        for i in range(N):
            while hold[A[i][like[i]]] == 0:
                like[i] += 1
            join[A[i][like[i]]] += 1
        tmp_ans = max(join)
        close = join.index(tmp_ans)
        ans = min(ans, tmp_ans)
        hold[close] = 0
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [[int(i) - 1 for i in input().split()] for _ in range(N)]
    solve(N, M, A)

    # # test
    # from random import randint, sample
    # from func import random_str, random_ints
    #
    # N, M = 6, 3
    # A = [sample([i for i in range(M)], M) for _ in range(N)]
    # # N, M = 6, 3
    # # A = [[2, 1, 0],
    # #      [2, 0, 1],
    # #      [0, 1, 2],
    # #      [2, 1, 0],
    # #      [0, 2, 1],
    # #      [2, 0, 1]]
    # print(N, M)
    # for a in A:
    #     print(a)
    # solve(N, M, A)
