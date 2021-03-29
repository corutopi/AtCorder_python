class FermatCmb:
    """フェルマー小定理を使用した順列, 組み合わせ計算
    max_num = 10 ** 6 で 0.58 sec
    """

    def __init__(self, max_num, mod):
        """
        :param max_num: max n of nCk
        :param mod: any prime number
        """
        self.max_num = max_num
        self.mod = mod
        self.fact = [0 for _ in range(max_num + 1)]
        self.factinv = [0 for _ in range(max_num + 1)]

        self.fact[0] = 1
        for i in range(1, max_num + 1):
            self.fact[i] = (i * self.fact[i - 1]) % self.mod

        self.factinv[-1] = pow(self.fact[-1], mod - 2, mod)
        for i in range(max_num, 0, -1):
            self.factinv[i - 1] = self.factinv[i] * i
            self.factinv[i - 1] %= self.mod

    def nCk(self, n, k):
        return (self.fact[n] * self.factinv[k] * self.factinv[n - k]) % self.mod

    def nPk(self, n, k):
        return (self.fact[n] * self.factinv[n - k]) % self.mod


def cmb(n, r):
    """組み合わせ"""
    import math
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def cmb2(n, r, mod):
    """組み合わせ(余り)"""
    if n < r:
        return 0
    re = 1
    for i in range(n - r + 1, n + 1):
        re = (re * i) % mod
    for i in range(1, r + 1):
        re = (re * inverse(i, mod)) % mod
    return re % mod


def inverse_comment(a, p):
    """逆元(コメント付き)"""
    # b / a を計算する時の, mod p における b の逆元 x を拡張ユークリッド互除法で計算する.
    # b / a ≡ b * (1 / a) (mod p)
    # a ** -1 ≡ x (mod p)
    # ax ≡ 1 (mod p)
    # ax - 1 = py
    # ax + py = 1
    a_, p_ = a, p
    x, y = 1, 0
    # todo: ここのループの仕組みがいまいち理解できていない.
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
    """逆元"""
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


def dev_mod(a, b, mod):
    """a(= A % mod) / b を mod で割った余り"""
    return (a * inverse(b, mod)) % mod


def ext_gcd(a, b, x=0, y=0):
    # ax + by = gcd(a, b) の整数解を決める.
    # a = ib + r とすると,
    # (ib + r)x + by = gcd(a, b) (= d)
    # b(ix + y) + rx = d (①)として, b と (a % b の) r の式に変形できる.
    # 変形後の式をさらに同様に変形していく.
    # 変形後の式を qx + ry = d と一般化し, q = d, r = 0 と なるまで変形する.
    # この時の解は明らかに x = 1, y = 0 なので, これを変形前の式に適用して変形前の式の解(x,y)を求める.
    # 変形後の式の解を x = s, y = t とすると, 変形前の式の解は以下のようになる.
    # ①の形から,
    #     s = ix + y, t = x
    #     ===> x = t, y = s - ix
    #     ===> x = t, y = s - (a//b)x
    if b == 0:
        return 1, 0
    s, t = ext_gcd(b, a % b, x, y)
    return t, s - a // b * t


def divisor(x):
    """約数"""
    from math import floor
    re = []
    _x = floor(x ** 0.5)
    for i in range(1, _x + 1):
        if x % i == 0:
            re.append(i)
            if x // i != i:
                re.append(x // i)
    re.sort()
    return re


def prime_factorization(x):
    """素因数分解"""
    import math
    re = []
    i = 2
    while x != 1:
        if x % i == 0:
            re.append(i)
            x //= i
        else:
            i += 1
            if i > math.sqrt(x):
                re.append(x)
                break
    return re


def lcm(a, b):
    """最小公倍数"""
    from math import gcd
    return (a * b) // gcd(a, b)


def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def prime_numbers(m):
    """m以下の素数リスト"""
    re = []
    first_prime = [0] * (m + 1)
    if m <= 1:
        return re
    for i in range(2, m + 1):
        if first_prime[i] > 0:
            continue
        re.append(i)
        for j in range(i * i, m + 1, i):
            first_prime[j] = i
    return re


def hadamard_matrix(k):
    """
    アダマール行列を生成する.
    シルベスターの生成法を採用.
    参考:
        https://ja.wikipedia.org/wiki/アダマール行列

    :param k: 次元を表す指数. 2 ** k 次元のアダマール行列が生成される.
    :return: 1, -1 で構成された2次元配列
    """
    if k == 0:
        return [[1]]
    if k == 1:
        return [[1, 1],
                [1, -1]]
    H = hadamard_matrix(k - 1)
    H_ = [[-i for i in h] for h in H]
    HH = [H[i] + H[i] for i in range(len(H))] + \
         [H[i] + H_[i] for i in range(len(H))]
    return HH


if __name__ == '__main__':
    print(len(prime_numbers(10 ** 5)))
