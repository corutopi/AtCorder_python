from math import ceil, floor


# こっちは何かダメなパターンがあるらしいが、謎.
def solve(A, B, X):
    N = 0
    for i in range(1, 11):
        n2 = max(floor((X - B * i) / A), 0)
        # 桁があふれる場合は次へ
        if len(str(n2)) > i:
            N = 10 ** i - 1
            continue
        # 割り算による桁あふれ考慮
        if (n2 + 1) * A + len(str(n2 + 1)) * B <= X:
            n2 += 1
        # 計算済みの値より小さい場合は終了する
        if n2 <= N:
            break
        # 答えを更新
        N = n2
    # 最大 10 ** 9 までとする
    N = min(N, 10 ** 9)
    return N


def solve2(A, B, X):
    h = 10 ** 9
    l = 0

    buy = lambda n: A * n + B * len(str(n))

    if buy(h) <= X:
        return h

    ans = 0
    while True:
        # print(l, h)
        m = (h + l) // 2
        price = buy(m)
        if price < X:
            l = m
        else:
            h = m
        if abs(h - l) <= 1:
            price1 = buy(h)
            price2 = buy(l)
            ans = h if price1 <= X else l
            break
    return ans


if __name__ == '__main__':
    A, B, X = map(int, input().split())
    print(solve2(A, B, X))
    # for i in range(10000000):
    #     a = 2
    #     b = 2
    #     sol = solve(a, b, i)
    #     if (sol + 1) * a + len(str(sol + 1)) * 2 <= i:
    #         print(a, ',', b, ',' , i, '->', solve(a, b, i))
