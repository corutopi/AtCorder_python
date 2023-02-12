"""
解説とSさんの助言でコンテスト中のミスを修正して提出
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(r1, c1, r2, c2):
    ans = 3

    def isreach(r, c, rr, cc):
        re = False
        if r + c == rr + cc:
            re = True
        elif r - c == rr - cc:
            re = True
        elif abs(r - rr) + abs(c - cc) <= 3:
            re = True
        return re

    if r1 == r2 and c1 == c2:
        ans = 0
    elif isreach(r1, c1, r2, c2):
        ans = 1
    else:
        if (r1 + c1) % 2 == (r2 + c2) % 2:
            # 対角線沿いに行ける場合
            ans = 2
        else:
            # ダイヤの範囲で被っている場合
            flg = False
            for i in range(-3, 4):
                for j in range(-3, 4):
                    if abs(i) + abs(j) > 3:
                        continue
                    if isreach(r1 + i, c1 + j, r2, c2):
                        ans = 2
                        flg = True
                        break
                if flg:
                    break
            # クロスの範囲とダイヤの範囲がかぶっている場合
            flg = False
            for s in (-3, 4):
                for t in (-3, 4):
                    if abs(s) + abs(t) > 3:
                        continue
                    if r1 + s + c1 + t == r2 + c2:
                        ans = 2
                        flg = True
                    elif (r1 + s) - (c1 + t) == r2 - c2:
                        ans = 2
                        flg = True
                    if flg:
                        break
                if flg:
                    break
    print(ans)


if __name__ == '__main__':
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    solve(r1, c1, r2, c2)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
