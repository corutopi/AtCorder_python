# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(A):
    tree = [[] for _ in range(16)]
    # base = sum(2 ** i for i in range(16) if A[i // 4][i % 4] == 1)
    base = 0
    start = -1
    for i in range(16):
        if A[i // 4][i % 4] == 1:
            base += 2 ** i
            start = i
    ans = 0
    binary = base
    while binary < 2 ** 16:
        visited = [0] * 16
        dq = deque([start])
        mass = sum(binary >> i & 1 for i in range(16))
        # judge chain
        while dq:
            now = dq.popleft()
            visited[now] = 1
            # up
            if now >= 4:
                if binary >> (now - 4) & 1 == 1 and visited[now - 4] == 0:
                    dq.append(now - 4)
            # down
            if now < 12:
                if binary >> (now + 4) & 1 == 1 and visited[now + 4] == 0:
                    dq.append(now + 4)
            # left
            if now % 4 > 0:
                if binary >> (now - 1) & 1 == 1 and visited[now - 1] == 0:
                    dq.append(now - 1)
            # right
            if now % 4 < 3:
                if binary >> (now + 1) & 1 == 1 and visited[now + 1] == 0:
                    dq.append(now + 1)
        # ans += 1 if sum(visited) == mass else 0
        if sum(visited) == mass:
            # judge hole
            has_hole = False
            visited2 = [0] * 16
            for i in [5, 6, 9, 10]:
                if binary >> i & 1 == 1: continue
                visited2 = [0] * 16
                dq2 = deque([i])
                cnt = 0
                while dq2:
                    now2 = dq2.popleft()
                    visited2[now2] = 1
                    if now2 < 4 or 12 <= now2 or now2 % 4 == 0 or now2 % 4 == 3:
                        break
                    # up
                    if now2 >= 4:
                        if binary >> (now2 - 4) & 1 == 0 and visited2[now2 - 4] == 0:
                            dq2.append(now2 - 4)
                    # down
                    if now2 < 12:
                        if binary >> (now2 + 4) & 1 == 0 and visited2[now2 + 4] == 0:
                            dq2.append(now2 + 4)
                    # left
                    if now2 % 4 > 0:
                        if binary >> (now2 - 1) & 1 == 0 and visited2[now2 - 1] == 0:
                            dq2.append(now2 - 1)
                    # right
                    if now2 % 4 < 3:
                        if binary >> (now2 + 1) & 1 == 0 and visited2[now2 + 1] == 0:
                            dq2.append(now2 + 1)
                    cnt += 1
                    if cnt == 100:
                        pass
                else:
                    has_hole = True
            # if has_hole:
            #     x = [str(binary >> i & 1) for i in range(16)]
            #     [print(x[i * 4:(i + 1) * 4]) for i in range(4)]
            #     print()
            ans += 0 if has_hole else 1
        binary += 1
        binary |= base
    print(ans)


if __name__ == '__main__':
    A = [[int(i) for i in input().split()] for _ in range(4)]
    solve(A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
