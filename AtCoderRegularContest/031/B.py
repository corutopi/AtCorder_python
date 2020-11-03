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
    island_num = 0
    for i in range(1, 10 + 1):
        for j in range(1, 10 + 1):
            if A[i][j] == 'x': continue
            if island_map[i][j] != 0: continue
            island_num += 1
            dq = deque([[i, j]])
            while dq:
                ii, jj = dq.pop()
                island_map[ii][jj] = island_num
                for ik, jk in [[ii - 1, jj], [ii + 1, jj],
                               [ii, jj - 1], [ii, jj + 1]]:
                    if A[ik][jk] == 'o' and island_map[ik][jk] == 0:
                        dq.append([ik, jk])

    ans = 'NO'
    if island_num <= 4:
        lands = [i for i in range(0, island_num + 1)]
        for i in range(1, 10 + 1):
            for j in range(1, 10 + 1):
                if A[i][j] == 'o': continue
                tmp_lands = [0]
                tmp_lands.append(island_map[i - 1][j])
                tmp_lands.append(island_map[i + 1][j])
                tmp_lands.append(island_map[i][j - 1])
                tmp_lands.append(island_map[i][j + 1])
                tmp_lands = list(set(tmp_lands))
                tmp_lands.sort()
                if lands == tmp_lands:
                    ans = 'YES'
                    break

    print(ans)


if __name__ == '__main__':
    A = [input() for _ in range(10)]
    solve(A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
