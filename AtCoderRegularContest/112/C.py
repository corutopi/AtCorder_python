"""
解説を参考に作成.
stackリソースの問題でwindows上だと制約 10 ** 5 での動作不可(再帰数最大の場合).
"""
import sys
sys.setrecursionlimit(10 ** 6)
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
def solve(n, p):
    tree = [[] for _ in range(n + 1)]
    for i in range(len(p)):
        tree[p[i]].append(i + 2)

    def f(top):
        if len(tree[top]) == 0:
            return 1, 0, 1

        tree_size = 1
        sente_coin = 1
        gote_coin = 0
        yusen = []
        atode = []
        saisho = []
        for t in tree[top]:
            sente, gote, size = f(t)
            tree_size += size
            if size % 2 == 0:
                if sente - gote <= 0:
                    yusen.append((sente, gote, size))
                else:
                    atode.append((sente, gote, size))
            else:
                saisho.append((sente, gote, size))

        saisho.sort(key=lambda x: x[0] - x[1])
        sente_turn = False
        for y in yusen:
            sente_coin += y[0]
            gote_coin += y[1]
        for s in saisho:
            if sente_turn:
                gote_coin += s[0]
                sente_coin += s[1]
            else:
                sente_coin += s[0]
                gote_coin += s[1]
            sente_turn = not sente_turn
        for a in atode:
            if sente_turn:
                gote_coin += a[0]
                sente_coin += a[1]
            else:
                sente_coin += a[0]
                gote_coin += a[1]

        return sente_coin, gote_coin, tree_size

    print(f(1)[0])


if __name__ == '__main__':
    n = int(input())
    p = [int(i) for i in input().split()]
    solve(n, p)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # n = 10 ** 5
    # p = [i + 1 for i in range(n - 1)]
    # solve(n, p)
