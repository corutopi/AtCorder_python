"""
todo:
    ダイクストラ法のスニペット
    ワーシャルフロイド法のスニペット
    ベルマンフォード法のスニペット
    有向グラフに閉路が含まれることを検出するスニペット(できれば再帰を使わないで)
"""


class UnionFind:
    """
    下記から拝借
    https://note.nkmk.me/python-union-find/
    """

    def __init__(self, n):
        """
        make lonely group 0 to (n - 1).
        :param n:
        """
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
        """
        return True if x is the same group as y else False.
        :param x:
        :param y:
        :return:
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        return members of the same group as x.
        :param x:
        :return:
        """
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


def warshall_floyd(N, ABT, start=0):
    """
    ワーシャルフロイド法を実行する.
    ノードは0始まりとする.
    計算量 O(max(N**3, len(ABT)).
    :param N: node num
    :param ABT: double list [[nodeA, nodeB, cost], ...]
    :param start: @todo 1始まりを許容できるようにすべきか検討
    :return:
    """
    inf = float('inf')
    re = [[0 if p == q else inf for p in range(N)] for q in range(N)]

    for a, b, t in ABT:
        re[a][b] = min(re[a][b], t)
        re[b][a] = min(re[b][a], t)

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                re[j][k] = min(re[j][k], re[j][i] + re[i][k])

    return re


def minimum_load(tree_map, start, end):
    """
    グラフの start から end までの最短の道順を検索する
    :param tree_map: [[], [1と行き来できるノード], [2と行き来できるノード], ...]
    :param start:
    :param end:
    :return: node_list[start, a1, a2, ... , end]
    """
    from collections import deque
    node_num = len(tree_map)
    parent_map = [-1] * node_num
    # make parent_map
    dq = deque([[end, -1]])
    while dq:
        now, parent = dq.popleft()
        parent_map[now] = parent
        if now == start:
            break
        for t in tree_map[now]:
            if t == parent:
                continue
            dq.append([t, now])
    # make load
    re = []
    now = start
    while True:
        re.append(now)
        if now == end:
            break
        now = parent_map[now]
    return re


if __name__ == '__main__':
    import tool.testcase as tc

    print(minimum_load([[], [2, 3], [1, 4], [1, 5], [2], [3]], 4, 4))
