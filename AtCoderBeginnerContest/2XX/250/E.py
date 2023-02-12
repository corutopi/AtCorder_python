# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def coordinate_compression(x, start=0):
    """整数のリストを座標圧縮したものを返す.デフォルトの最小値0.

    :param x: integer list
    :param start:
    :return:
    """
    xd = {v: i + start for i, v in enumerate(sorted(x))}
    return list(map(lambda d: xd[d], x))


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A, B, Q, XY):
    AB = A + B
    AB_hash = dict()
    AB_press = []
    i = 1
    for ab in AB:
        if AB_hash.get(ab, 0) == 0:
            AB_hash[ab] = i
            i += 1
        AB_press.append(AB_hash[ab])
    A = AB_press[:N]
    B = AB_press[N:]

    A_y_s = []
    tmp_max = 0
    tmp_yos = 0
    tmp_visited = [0] * (max(A) + 1)
    for a in A:
        if tmp_visited[a] == 0:
            tmp_visited[a] = 1
            tmp_yos += 1
            tmp_max = max(tmp_max, a)
        A_y_s.append([tmp_yos, tmp_max])
    B_y_s = []
    tmp_max = 0
    tmp_yos = 0
    tmp_visited = [0] * (max(B) + 1)
    for b in B:
        if tmp_visited[b] == 0:
            tmp_visited[b] = 1
            tmp_yos += 1
            tmp_max = max(tmp_max, b)
        B_y_s.append([tmp_yos, tmp_max])
    ans = []
    for x, y in XY:
        if A_y_s[x - 1][0] == B_y_s[y - 1][0] and \
                A_y_s[x - 1][1] == B_y_s[y - 1][1]:
            # print('Yes')
            ans.append('Yes')
        else:
            # print('No')
            ans.append('No')
    return ans


def solve_force(N, A, B, Q, XY):
    ans = []
    for x, y in XY:
        xy_set = set()
        for a in A[:x]:
            xy_set.add(a)
        y_set = set()
        for b in B[:y]:
            y_set.add(b)
        for ys in y_set:
            if ys in xy_set:
                xy_set.remove(ys)
            else:
                xy_set.add(ys)
        ans.append('Yes' if len(xy_set) == 0 else 'No')
    return ans


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    Q = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(Q)]
    [print(ans) for ans in solve(N, A, B, Q, XY)]

    # #####
    # N = 10
    # A = [7, 10, 2, 10, 8, 7, 9, 8, 6, 5]
    # B = [2, 10, 4, 9, 1, 4, 7, 6, 4, 3]
    # Q = 5
    # XY = [[4, 3], [2, 2], [3, 4], [3, 4], [1, 3]]
    # print(solve(N, A, B, Q, XY))
    # #####
    #
    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # while True:
    #     N = 10
    #     A = random_ints(N, 1, N)
    #     B = random_ints(N, 1, N)
    #     Q = 5
    #     XY = [random_ints(2, 1, 4) for _ in range(Q)]
    #     normal = solve(N, A, B, Q, XY)
    #     force = solve_force(N, A, B, Q, XY)
    #     for i in range(len(normal)):
    #         if normal[i] != force[i]:
    #             print(N)
    #             print(A)
    #             print(B)
    #             print(Q)
    #             print(XY)
    #             print(normal)
    #             print(force)
    #             break
    #     else: continue
    #     break
