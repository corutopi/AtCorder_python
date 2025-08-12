# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, S):
    ans = []
    flg = False
    # 縦
    for h in range(H - 4):
        for w in range(W):
            snuke = ''
            for i in range(5):
                snuke += S[h + i][w]
            if snuke == 'snuke':
                for i in range(5):
                    ans.append([h + i + 1, w + 1])
                flg = True
                break
            elif snuke[::-1] == 'snuke':
                for i in range(5):
                    ans.append([h + 4 - i + 1, w + 1])
                flg = True
                break
        else:
            continue
        break

    # 横
    if flg:
        pass
    else:
        for h in range(H):
            for w in range(W - 4):
                snuke = ''
                for i in range(5):
                    snuke += S[h][w + i]
                if snuke == 'snuke':
                    for i in range(5):
                        ans.append([h + 1, w + i + 1])
                    flg = True
                    break
                elif snuke[::-1] == 'snuke':
                    for i in range(5):
                        ans.append([h + 1, w + 4 - i + 1])
                    flg = True
                    break
            else:
                continue
            break

    # 斜め＼
    if flg:
        pass
    else:
        for h in range(H - 4):
            for w in range(W - 4):
                snuke = ''
                for i in range(5):
                    snuke += S[h + i][w + i]
                if snuke == 'snuke':
                    for i in range(5):
                        ans.append([h + i + 1, w + i + 1])
                    flg = True
                    break
                elif snuke[::-1] == 'snuke':
                    for i in range(5):
                        ans.append([h + 4 - i + 1, w + 4 - i + 1])
                    flg = True
                    break
            else:
                continue
            break

    # 斜め／
    if flg:
        pass
    else:
        for h in range(H - 4):
            for w in range(4, W):
                snuke = ''
                for i in range(5):
                    snuke += S[h + i][w - i]
                if snuke == 'snuke':
                    for i in range(5):
                        ans.append([h + i + 1, w - i + 1])
                    flg = True
                    break
                elif snuke[::-1] == 'snuke':
                    for i in range(5):
                        ans.append([h + 4 - i + 1, w - 4 + i + 1])
                    flg = True
                    break
            else:
                continue
            break

    for a in ans:
        print(*a)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    H, W = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    S = [input() for _ in range(H)]
    # P = [int(input()) for _ in range(N)]
    solve(H, W, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
