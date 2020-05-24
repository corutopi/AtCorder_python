"""
Common Function
"""


def combinations_count(n, r):
    import math
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def ppprint(itr_obj):
    if len(itr_obj) == 0:
        print('non list', itr_obj)
    for ite in itr_obj:
        print(ite)


def make_test_graph_data(node, edge, is_directed=False):
    import random
    count = 0
    re = []
    while count < edge:
        new = [random.randint(1, node), random.randint(1, node)]
        if new[0] == new[1]:
            continue
        if not is_directed:
            new.sort()
        if new in re:
            continue
        re.append(new)
        count += 1
    return re


def inverse_comment(a, p):
    # b / a を計算する時の, mod p における b の逆元 x を拡張ユークリッド互除法で計算する.
    # b / a ≡ b * (1 / a) (mod p)
    # a ** -1 ≡ x (mod p)
    # ax ≡ 1 (mod p)
    # ax - 1 = py
    # ax + py = 1
    a_, p_ = a, p
    x, y = 1, 0
    # ここのループの仕組みがいまいち理解できていない.
    # ext_gcd で 解(x, y)を求める仕組みに似ているが, a, pの遡及の向きが逆になってない？
    # なぜこれで正しい解になるのかよくわからん
    while p_:
        t = a_ // p_
        a_ -= t * p_
        a_, p_ = p_, a_
        x -= t * y
        x, y = y, x
    # x, y = ext_gcd(a, p)  # これのほうがしっくりくる
    x %= p  # x が負の場合があるので, mod p して逆元にする
    return x


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


def ext_gcd(a, b, x=0, y=0):
    # ax + by = gcd(a, b) の整数解を決める.
    # a = ib + r とすると,
    # (ib + r)x + by = gcd(a, b) (= d)
    # b(ix + y) + rx = d (①)として, b と (a % b の) r の式に変形できる.
    # 変形後の式をさらに同様に変形していく.
    # 変形後の式を qx + ry = d と一般化し, q = d, r = 0 と なるまで変形する.
    # この時の解は明らかに x = 1, y = 0 なので, これを変形前の式に適用して変形前の式の解(x,y)を求める.
    # 変形後の式の解を x = s, y = t とすると, 変形前の式の解以下のようになる.
    # ①の形から,
    #     s = ix + y, t = x
    #     ===> x = t, y = s - ix
    #     ===> x = t, y = s - (a//b)x
    if b == 0:
        return 1, 0
    s, t = ext_gcd(b, a % b, x, y)
    return t, s - a // b * t


if __name__ == '__main__':
    a = 12345678900000 % (10 ** 9 + 7)
    print(a * inverse(100000, 10 ** 9 + 7) % (10 ** 9 + 7))
