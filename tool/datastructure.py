class BinaryIndexedTree:
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8] のlistを例とした場合、
    以下のような範囲での演算結果(sum)を配列に持つ。
        1: [1, 2, 3, 4, 5, 6, 7, 8]
        2: [1, 2, 3, 4]
        3: [1, 2]      [5, 6]
        4: [1]   [3]   [5]   [7]
    1 ～ r までの結果S(r)を、各層で必要な演算済みのデータを使うことで log(N) で計算できる.
    l ～ r までの結果は S(r) - S(l - 1) で同じくlog(N)計算できる.
    データ構造の作成は N*log(N).
    配列データは1始まりとして計算.
    長さ n + 1 (0 ~ n) の配列にデータを持ち, データ内の対象要素を l ~ r とすると, 配列の r 番目が格納先となる.
    また対象要素の数は r の LSB(Least Significant Bit) に一致する.

    転倒数の計算にも使える.
    """

    def __init__(self, n):
        """
        :param n: num of date.
        """
        self.num = n
        self.tree = [0] * (n + 1)

    def add(self, k, x):
        """
        :param k: [1, self.num]
        :param x: add num.
        :return: None
        """
        while k <= self.num:
            self.tree[k] += x
            k += k & -k

    def sum(self, k):
        """
        1 ～ k までの合計
        :param k:
        :return:
        """
        re = 0
        while k > 0:
            re += self.tree[k]
            k -= k & -k
        return re

    def sum_lr(self, l, r):
        """
        sum of form l to r
        :param l: 1 <= l <= r
        :param r: l <= r <= self.num
        :return:
        """
        return self.sum(r) - self.sum(l - 1)


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

    def element(self, k):
        """
        要素の取得
        :param k: elm の要素番号
        :return:
        """
        return self.tree[self.num + k]

    def update(self, k, x):
        """
        要素k の値を x に更新する
        :param k: elm の要素番号
        :param x:
        :return:
        """
        k = self.num + k
        self.tree[k] = x
        while k > 1:
            k = k // 2
            self.tree[k] = self.func(self.tree[k * 2], self.tree[k * 2 + 1])

    def query(self, l, r):
        """
        [l, r) の結果を取得する
        :param l: 0 始まりで指定する
        :param r:
        :return:
        """
        res_l = self.default
        res_r = self.default
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res_l = self.func(res_l, self.tree[l])
                l += 1
            if r & 1:
                res_r = self.func(self.tree[r - 1], res_r)
            l >>= 1
            r >>= 1
        return self.func(res_l, res_r)


class BinaryTrie:
    """
    遅いので改良する。
    数値の順序付き集合を管理するクラス。
    特定の数値より大きく最小の値/小さく最大の値等を高速に求められる(ようにしたい)。

    参考:
    https://kazuma8128.hatenablog.com/entry/2018/05/06/022654
    """

    def __init__(self, b):
        self.bit_size = b
        self.b_node = BinaryNode()

    def insert(self, x):
        """
        x を追加する
        :param x:
        :return:
        """
        self.b_node.add_node(x, self.bit_size)

    def delete(self, x):
        """
        x を削除する
        :param x:
        :return:
        """
        self.b_node.del_node(x, self.bit_size)

    def max_element(self):
        pass

    def min_element(self):
        pass

    def lower_bound(self, x):
        """
        x 以下で要素中最大の値の要素番号を返す。番号は1始まり。
        :param x:
        :return:
        """
        return self.b_node.lower_bound(x, self.bit_size)

    def upper_bound(self, x):
        """
        x 以上で要素中最小の値の要素番号を返す。番号は1始まり。
        :param x:
        :return:
        """
        return self.b_node.num - self.b_node.upper_bound(x, self.bit_size) + 1

    def kth_element(self, k):
        """
        k 番目の要素の値を返す。番号は1始まり。
        :param k:
        :return:
        """
        return self.b_node.kth_element(k, self.bit_size)


class BinaryNode:
    """
    BinaryTrie 内で使用するサブクラス。
    引数や戻り値の要素位置は1始まり。
    """

    def __init__(self):
        self.num = 0
        self.pointer = [None, None]

    def __add_pointer(self, x):
        self.pointer[x] = \
            BinaryNode() if self.pointer[x] is None else self.pointer[x]

    def __del_pointer(self, x):
        self.pointer[x] = None

    def add_node(self, x, b):
        """
        x をノードに追加する
        :param x: 追加する値
        :param b: 低から数えた時の深さ
        :return:
        """
        if b == -1:
            self.num += 1
            return self.num
        t = x >> b & 1
        self.__add_pointer(t)
        self.pointer[t].add_node(x, b - 1)
        self.num += 1

    def del_node(self, x, b):
        """
        x をノードから削除する
        :param x: 削除する値
        :param b: 低から数えた時の深さ
        :return:
        """
        if b == -1:
            self.num = 0
            return self.num
        t = x >> b & 1
        if self.pointer[t].del_node(x, b - 1) == 0:
            self.__del_pointer(t)
        self.num -= 1
        return self.num

    def upper_bound(self, x, b):
        """
        x 以上の値の要素の個数
        :param x: 検索値
        :param b: 低から数えた時の深さ
        :return:
        """
        if b == -1:
            return 1
        re = 0
        if x >> b & 1 == 1:
            if self.pointer[1] is not None:
                re += self.pointer[1].upper_bound(x, b - 1)
        else:
            if self.pointer[0] is not None:
                re += self.pointer[0].upper_bound(x, b - 1)
            if self.pointer[1] is not None:
                re += self.pointer[1].num
        return re

    def lower_bound(self, x, b):
        """
        x 以下の要素の個数
        :param x: 検索値
        :param b: 低から数えた時の深さ
        :return:
        """
        if b == -1:
            return 1
        re = 0
        if x >> b & 1 == 1:
            if self.pointer[0] is not None:
                re += self.pointer[0].num
            if self.pointer[1] is not None:
                re += self.pointer[1].lower_bound(x, b - 1)
        else:
            if self.pointer[0] is not None:
                re += self.pointer[0].lower_bound(x, b - 1)
        return re

    def kth_element(self, k, b):
        """
        k番目の要素の値
        :param k: 検索要素番号
        :param b: 低から数えた時の深さ
        :return:
        """
        if b == -1:
            return 0
        re = 0
        if self.pointer[0] is not None:
            if k <= self.pointer[0].num:
                re += self.pointer[0].kth_element(k, b - 1)
            else:
                re += 1 << b
                re += self.pointer[1].kth_element(k - self.pointer[0].num,
                                                  b - 1)
        else:
            re += 1 << b
            re += self.pointer[1].kth_element(k, b - 1)
        return re
