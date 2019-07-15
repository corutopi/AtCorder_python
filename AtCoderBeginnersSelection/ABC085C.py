"""
Otoshidama

考え方:
    作成できる金額は N * 10000 (R) が最大となる.
    そこから x 枚を5000円にした時の合計金額 M と申告金額 Y とが以下の条件を満たせばよい.
        M >= Y, (M - Y) / 4000 == 0, (M - Y) // 4000 < x
    差額が4000円で割り切れるなら, 所定の枚数を5000円→1000円に換えて操作終了.
    何枚5000円にするかの試行回数は 0 ～ N なので計算量 O(n)
"""


def solve():
    N, Y = map(int, input().split())
    Y = Y / 1000
    for i in range(N + 1):
        money = (N - i) * 10 + i * 5
        if money >= Y and (money - Y) % 4 == 0:
            n1 = int((money - Y) / 4)
            if n1 <= i:
                print(N - i, i - n1, n1)
                return
    print(-1, -1, -1)


if __name__ == '__main__':
    solve()
