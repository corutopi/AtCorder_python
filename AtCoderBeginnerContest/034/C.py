# ↓を参考に作成
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#3-%E5%89%B2%E3%82%8A%E7%AE%97-a--b


def solve():
    import math
    mod = 10 ** 9 + 7

    W, H = map(lambda x: int(x) - 1, input().split())

    # 分子の計算
    ans = 1
    for i in range(1, W + H + 1):
        ans = (ans * i) % mod
    # 分母の計算
    for i in range(1, W + 1):
        ans = ans * inverse(i, mod) % mod
    for i in range(1, H + 1):
        ans = ans * inverse(i, mod) % mod
    print(ans % mod)


def inverse(a, p):
    a_, p_ = a, p
    x, y = 1, 0
    while p_:
        t = a_ // p_
        a_ -= t * p_
        a_, p_ = p_, a_
        x -= t * y
        x, y = y, x
    x %= p
    return x


if __name__ == '__main__':
    solve()
