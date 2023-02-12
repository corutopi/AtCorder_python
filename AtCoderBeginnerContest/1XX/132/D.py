

def solve():
    N, K = map(int, input().split())
    R = N - K  # 赤玉の数
    dp = []  # 青玉の分割数 と 赤玉の数 毎のパターン総数
    dp = [[0] * (R + 1) for _ in range(K + 1)] # 初期化
    dp[1] = [i + 1 for i in range(R + 1)]  # 赤玉の数が
    print('before')
    ppprint(dp)
    for r in range(0, R + 1):  # 赤玉の数
        for v in range(2, K + 1):  # 青玉の分割数
            if v > r + 1:
                break
            if v == r + 1:
                # 新たに計算する場合
                dp[v][r] = combinations_count(K - 1, r)
                break
            else:
                # 赤玉 - 1 の時の情報からパターン数を計算する
                # # 分割数 - 1 の時のパターンにさらに1か所分割を追加するパターン
                dp[v][r] += dp[v - 1][r - 1] * ((K - 1) - ((v - 1) - 1))
                # # 分割数が同じ時のパターンに、すでに赤玉がある場所に追加するパターン
                dp[v][r] += dp[v][r - 1] * (v - 1)  # 両端にも入れられる？
                pass
    print('after')
    ppprint(dp)
    for v in range(1, K + 1):
        print(dp[v][-1] % (10 ** 9 + 7))


def solve_commentary():
    N, K = map(int, input().split())
    R = N - K  # 赤玉の数
    MOD = 10 ** 9 + 7
    for i in range(1, K + 1):
        if N - K + 1 >= i:
            print((combinations_count(N - K + 1, i) * combinations_count(K - 1, i - 1)) % (MOD))
        else:
            print(0)
        pass
    pass


def combinations_count(n, r):
    import math
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def ppprint(itr_obj):
    for ite in itr_obj:
        print(ite)


if __name__ == '__main__':
    # solve()
    solve_commentary()
