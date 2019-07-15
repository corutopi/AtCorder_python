"""
解説と提出 #5739708をもとに作成
"""

import sys
sys.setrecursionlimit(10 ** 6)


def solve():
    N = int(input())
    result = [-1] * N
    uvw_map = [[] for _ in range(N)]
    '''枝毎の距離相関図を作る'''
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        uvw_map[u].append([v, w])
        uvw_map[v].append([u, w])
    # 木の頂点を求める
    # -> 任意の場所で良い. 1 とする.
    # 頂点から順に塗っていく
    result[0] = False
    result = paint(uvw_map, 0, result)
    for i in result:
        print(int(i))


def paint(uvw_map, num, result):
    # num に紐づくノードの一覧を取得する
    num_map = uvw_map[num]
    # num との距離に応じて色を決定する
    nums = []
    for v, w in num_map:
        if result[v] != -1:
            continue
        result[v] = result[num] if w % 2 == 0 else not(result[num])
        # # 色分けを行ったものについてのみ記録しておく(num')
        nums.append(v)
    # num' すべてに対して同様の操作を行う
    for n in nums:
        result = paint(uvw_map, n, result)
    return result


if __name__ == '__main__':
    solve()
