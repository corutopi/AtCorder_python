# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
# import string
from heapq import heappush, heappop
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A):
    rank_q = [deque([]) for _ in range(K)]
    invited_flg = dict()
    wait_frame = [N - max(0, min(N, K - i * N)) for i in range(K)]
    fixed_frame = [K // N + (1 if i < K % N else 0) for i in range(N)]
    substitute = 0
    for i in range(N):
        note = []
        # i回目の予選結果集計
        for j in range(K):
            Aij = A[i][j]
            if j < fixed_frame[i]:
                if invited_flg.get(Aij, 0) == 1:
                    substitute += 1
                else:
                    note.append(Aij)
                    invited_flg[Aij] = 1
            else:
                rank_q[j].append(Aij)
        # i回目終了時点での待機選手の繰り上げ確認
        s = substitute
        c = 0
        for k in range(K):
            if s == 0: break
            for l in range(wait_frame[k]):
                if s == 0: break
                s -= 1
                if rank_q[k]:
                    x = rank_q[k].popleft()
                    if invited_flg.get(x, 0) == 1:
                        s += 1  # 招待済みなので補欠枠を戻す
                    else:
                        note.append(x)
                        invited_flg[x] = 1
                        c += 1
                    wait_frame[k] -= 1
        substitute -= c
        print(*sorted(note))


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
