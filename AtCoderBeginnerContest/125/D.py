def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    absA = [abs(Ai) for Ai in A]
    rA = [-1 if Ai < 0 else 1 for Ai in A]
    # すべてひっくり返せるか, 端だけ負になるかを検索する
    for i in range(N - 1):
        if rA[i] < 0:
            rA[i] *= -1
            rA[i + 1] *= -1
    # すべてひっくり返せるならすべての合計
    if rA[-1] == 1:
        result = sum(absA)
    else:
        # 無理なら一番小さい値を引いた数
        result = sum(absA) - (min(absA) * 2)
    print(result)


if __name__ == '__main__':
    solve()
