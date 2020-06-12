# 解説を参考に作成
# 10170959 を参考に作成
# 一応出そうと思うけど遅すぎる.
# numpy じゃなきゃダメか？


# import sys
# sys.setrecursionlimit(10 ** 6)
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, As):
    As.sort()
    # print(As)
    ans = 0
    l = - 10 ** 18 + 1
    r = 10 ** 18 + 1
    while l <= r:
        m = (r + l) // 2
        c = 0
        # 答えが m 未満となる組み合わせを洗い出す
        for i in range(N):
            # すべての i に対して、i + 1 ～ N の間で2部探索
            ll = i + 1  # 下限を i + 1 とすることで重複をなくせる
            rr = N - 1
            cc = 0
            while ll <= rr:
                mm = (ll + rr) // 2
                if As[i] < 0:
                    # As[i] < 0 の場合、㎜ の増加で 単調減少する
                    # -> As[i] * As[mm] < m を満たす最小の mm を閾値に, mm 以上のすべてのが m 未満となる
                    if As[i] * As[mm] < m:
                        cc = N - mm
                        rr = mm - 1
                    else:
                        ll = mm + 1
                else:
                    # As[i] >= 0 の場合、㎜ の増加で 単調増加する
                    # -> As[i] * As[mm] < m を満たす最大の mm を閾値に, mm 以下のすべてのが m 未満となる
                    # ただし、重複を避けるため i + 1 ～ mm までの数のみを加算する
                    if As[i] * As[mm] < m:
                        cc = mm - i
                        ll = mm + 1
                    else:
                        rr = mm - 1
            # print('   ', i, mm, cc)
            c += cc
        # print(l, m, r, c, ans)
        # input()
        if c < K:
            # c < K を満たす最大の m が答えとなる.
            # ans となる K の値が複数ある場合, ans 超の場合は ans 自身をカウントするため c >= K となる.
            # よって収束の過程で必ず「c < K を満たす最大の m」がここで設定されることになる.
            ans = m
            l = m + 1
        else:
            r = m - 1

    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    As = [int(i) for i in input().split()]

    # N, K = 200000, 1000
    # As = [-200000 + i for i in range(200000)]
    # print(As[1], As[-1])
    solve(N, K, As)
