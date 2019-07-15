"""
I - Coins

考え方:
    N 枚のコインを投げた時, n 枚表になる確率を求める.
    以下の二つの和で求められる(①).
        N - 1 枚投げた時に n - 1 枚表になり, さらに次に投げた時に表になる確率
        N - 1 枚投げた時に n 枚表になり, さらに次に投げた時に裏になる確率
    N を0から始めるとDPで求められる.
    0 <= n <= N / 2 となるすべての n の確立の和が, 表が半分以下となる確率 X.
    表が半分以上となる(裏より多くなる)確率は 1 - X.
    計算量は O(n^2) <- あってる？？
"""


def solve():
    N = int(input())
    P = [float(i) for i in input().split()]
    dp = [1 for i in range(int((N + 1) / 2))]  # i 枚表になる確率
    for i, p in enumerate(P, 1):
        for j in reversed(range(len(dp))):
            if i <= j:
                # コインの合計枚数が i 枚以下の場合は表にする.
                dp[j] *= p
            elif j == 0:
                # 表のコインの枚数が 0 枚の場合は普通に裏になる.
                dp[j] *= (1 - p)
            else:
                # N 枚のコインを投げて n 枚表になる(①の計算)
                dp[j] = dp[j] * (1 - p) + dp[j - 1] * p
    print(1 - sum(dp))


if __name__ == '__main__':
    solve()
