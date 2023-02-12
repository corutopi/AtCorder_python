"""
Match Matching
提出 #4299735 を参考に作成
"""


def solve():
    # 初期値の設定
    num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    A.sort(reverse=True)
    # 丁度n本で作成できる最大桁数を格納する.
    # 初期値は -inf (丁度使い切ることは不可能) としておく
    dp = [-1 * float("inf")] * (N + 1)

    # 動的計画法で丁度n本のマッチを使うときに作れる最大桁数を計算する
    dp[0] = 0
    for n in range(1, N + 1):
        for a in A:
            if n - num[a] >= 0:
                # マッチがnum[a]本あるときにaが作れるなら,
                # n - num[a]本の時よりも1桁多く作れるはず.
                # これをすべてのAに対して行い、その中で最大となった桁数を求める.
                dp[n] = max(dp[n], dp[n - num[a]] + 1)
    # print('各本数丁度で作れる最大桁数')
    # print(dp)

    # 回答となる数値を算出
    ans = ''
    for i in range(dp[N]):  # dp[N]桁の数を上位の桁から決定していく
        for a in A:
            # num[a]本使って数を作ったとき,
            # N - num[a] 本で作れる桁数よりも N 本で作れる桁数のほうが1多い場合,
            # numを作っても最終的に作れる数の桁数は変わらない.
            # そのため dp[N] - 1 == dp[N - num[a]] を満たすような最大のAを作り,
            # 作成する数の上位桁に使用すればよい.
            # 同じ本数のマッチを使用する場合はより大きい数を採用する.
            # そのためAはあらかじめ降順にソートしておく.
            # 最初の条件で配列外アクセスを防ぐ
            if N - num[a] > -1 and dp[N] - 1 == dp[N - num[a]]:
                ans += str(a)
                N -= num[a]
                break
        # print('現在の残本数', N, '採用された数', a)

    print(ans)


if __name__ == '__main__':
    solve()
