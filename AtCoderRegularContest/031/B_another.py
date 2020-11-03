# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(A):
    A = ['x' * 12] + ['x' + a + 'x' for a in A] + ['x' * 12]
    island_map = [[0] * 12 for _ in range(12)]
    earth_num = sum([a.count('o') for a in A])
    for i in range(1, 10 + 1):
        for j in range(1, 10 + 1):
            if A[i][j] == 'o': continue
            if island_map[i][j] != 0: continue
            island_map = [[0] * 12 for _ in range(12)]
            dq = deque([[i, j]])
            tmp_earth_num = 0
            while dq:
                ii, jj = dq.pop()
                for ik, jk in [[ii - 1, jj], [ii + 1, jj],
                               [ii, jj - 1], [ii, jj + 1]]:
                    if A[ik][jk] == 'o' and island_map[ik][jk] == 0:
                        dq.append([ik, jk])
                        island_map[ik][jk] = 1
                        tmp_earth_num += 1
            if tmp_earth_num == earth_num:
                print('YES')
                return
    print('NO')




if __name__ == '__main__':
    A = [input() for _ in range(10)]
    solve(A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
