"""
解説を参考に作成

考え方:
    Sのi文字目までとTのj文字目までで,
    Si と Tj がペアになる場合のパターン数を解く (dp)
    -> Si != Tj の場合,そもそもペアにできないので 0.
    -> それ以外の場合は以下の2通りが考えられる.
        Sのi-1文字目までとTのj-1文字目までの全パターンに対して Si と Tjを追加したパターン
        Si と Tj のみのパターン
    よって Si と Tj までで作成できるパターンの総合計も同時に求めておく必要がある (dp_sum)
"""


def solve():
    mod = 10 ** 9 + 7
    N, M = map(int, input().split())
    S = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp_sum = [[0] * (M + 1) for _ in range(N + 1)]
    # ppprint(dp_sum)
    for i, Si in enumerate(S, 1):
        for j, Tj in enumerate(T, 1):
            if Si == Tj:
                # print(i, j)
                # print(dp_sum[i - 1])
                dp[i][j] = dp_sum[i - 1][j - 1] + 1
            dp_sum[i][j] = (dp_sum[i][j - 1] + dp_sum[i - 1][j] -
                            dp_sum[i - 1][j - 1] + dp[i][j]) % mod
    # print('include table')
    # ppprint(dp)
    # print('sum table')
    # ppprint(dp_sum)
    print((dp_sum[N][M] + 1) % mod)


def ppprint(itr_obj):
    for ite in itr_obj:
        print(ite)


if __name__ == '__main__':
    import datetime
    d = datetime.datetime.now()
    solve()
    # print(datetime.datetime.now() - d)
