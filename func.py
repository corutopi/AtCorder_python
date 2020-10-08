"""
Common Function
"""

from decorator import stop_watch


class UnionFind():
    """
    下記から拝借
    https://note.nkmk.me/python-union-find/
    """

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(
            '{}: {}'.format(r, self.members(r)) for r in self.roots())


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


class SegTree:
    """
    セグメントツリー
    参考:
        https://algo-logic.info/segment-tree/#toc_id_1
        https://qiita.com/takayg1/items/c811bd07c21923d7ec69
    --イメージ--------
     1  1  1  1  1  1  1  1
     2  2  2  2  3  3  3  3
     4  4  5  5  6  6  7  7
     8  9 10 11 12 13 14 15  <- ここに配列の素の値が入る
    ------------------
    同じ番号の列すべての func 結果を配列に持つ
    """
    def __init__(self, elm, func, default):
        """
        :param elm: 配列
        :param func: 操作関数(f(x, y))
        :param default: 単位元
        """
        # create val
        self.num = 1 << (len(elm) - 1).bit_length()
        self.func = func
        self.tree = [default] * 2 * self.num
        self.default = default
        # update leaf
        for i in range(len(elm)):
            self.tree[self.num + i] = elm[i]
        # update nodes
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, k, x):
        k = self.num + k
        self.tree[k] = x
        while k > 1:
            k = k // 2
            self.tree[k] = self.func(self.tree[k * 2], self.tree[k * 2 + 1])

    def query(self, l, r):
        """
        [l, r) の結果を取得する
        :param l:
        :param r:
        :return:
        """
        res = self.default
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.func(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


# functions
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


def random_str(length, choice=''):
    """指定の長さのランダム英数文字列"""
    from random import randint, choices
    import string
    if choice == '':
        choice = string.ascii_letters + string.digits
    return ''.join(choices(choice, k=length))


def random_ints(num, min, max, duplicate=True, sort=False):
    import random
    import warnings
    ERROR_DOMAIN_NARROW = 'domain error: too narrow domain(min - max) and can\'t take a unique value.'
    WARN_MANY_ELEMENTS = 'too many elements warning: too many elements and it may take a lot of memory.'
    WARN_DOMAIN_NARROW = 'domain of narrow warning: too narrow domain(min - max) and it may take many time of process.'
    element_num = max - min + 1

    if duplicate:
        re = [random.randint(min, max) for _ in range(num)]
    else:
        if num > element_num:
            raise ValueError(ERROR_DOMAIN_NARROW)
        if element_num >= 10 ** 8:
            warnings.warn(WARN_MANY_ELEMENTS, stacklevel=2)
        if num >= 10 ** 6 and element_num / num < 2:
            warnings.warn(WARN_DOMAIN_NARROW, stacklevel=2)

        check = [0] * element_num
        cnt = 0
        re = []
        while cnt < num:
            tmp = random.randint(min, max)
            if check[tmp - min] == 0:
                check[tmp - min] = 1
                cnt += 1
                re.append(tmp)
    if sort:
        re.sort()
    return re


@stop_watch
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


def binary_search(ok, ng, solve):
    """2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid


if __name__ == '__main__':
    print(random_ints(int(10 ** 6 * 6), 1, 10 ** 7, duplicate=False))
