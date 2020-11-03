# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, P, C):
    P = [0] + P
    C = [0] + C
    # ループ毎にグループ化
    groups = []
    n_flg = [False] * (N + 1)
    for i in range(1, N + 1):
        if n_flg[i]:
            continue
        n_flg[i] = True
        tmp = i
        new_group = [C[tmp]]
        while P[tmp] != i:
            tmp = P[tmp]
            n_flg[tmp] = True
            new_group.append(C[tmp])
        groups.append(new_group)
    # グループ毎に最大値を計算
    ans = -(10 ** 10)
    for g in groups:
        # # メンバー数(num), 1ループ分の合計(all_sum), 1 ~ num回移動する場合のそれぞれの最大値(max[i]), を求める
        num = len(g)
        all_sum = sum(g)
        g += g
        tmp_sum = [0]
        for gg in g:
            tmp_sum.append(tmp_sum[-1] + gg)
        move_sum = [0]
        for i in range(1, num + 1):
            t = -(10 ** 10)
            for j in range(num):
                t = max(t, tmp_sum[j + i] - tmp_sum[j])
            move_sum.append(t)
        # # sum <= 0 の場合, max[i(1 <= i <= K)] の最大値
        tmp_ans = 0
        if all_sum <= 0:
            tmp_ans = max(move_sum[1:K + 1])
        else:
            d, m = divmod(K, num)
            tmp_ans += all_sum * d
            if d > 0:
                # # K >= num の場合, 可能な限りループ + 余りをnとして0 ～ n回移動する場合の最大値
                # # or 可能な限り-1ループ + max[i(0 <= i <= K)]の最大値
                tmp_ans = max(all_sum * d + max(move_sum[:m + 1]),
                              all_sum * (d - 1) + max(move_sum))
            else:
                # # K <= num の場合, max[i](1 <= i <= num) の最大値
                tmp_ans += max(move_sum[1:m + 1])
        # 各グループの計算結果の内最大のものが答え
        ans = max(ans, tmp_ans)
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    P = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    solve(N, K, P, C)

    # # test
    # from random import randint
    # from func import random_str, random_ints

    # # 最大値
    # N, K = 5000, 10 ** 9
    # P = [i for i in range(2, N + 1)] + [1]
    # # P = [i for i in range(1, N + 1)]
    # C = [randint(-10 ** 9, 10 ** 9) for i in range(N)]
    # # ループしない方が得するパターン
    # N, K = 3, 4
    # P = [2, 3, 1]
    # C = [-10, 5, 6]
    # print(P)
    # print(C, sum(C))

    # solve(N, K, P, C)
