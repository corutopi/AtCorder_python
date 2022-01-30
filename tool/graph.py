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
        self._n = n
        self._parents = [-1] * n
        self._group_count = n

    def find(self, x):
        """
        return the number of representatives of the group to which x belongs.

        :param x:
        :return:
        """
        if self._parents[x] < 0:
            return x
        else:
            self._parents[x] = self.find(self._parents[x])
            return self._parents[x]

    def union(self, x, y):
        """
        join the group to which x belongs and the group to which y belongs.

        :param x:
        :param y:
        :return:
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self._parents[x] > self._parents[y]:
            x, y = y, x

        self._parents[x] += self._parents[y]
        self._parents[y] = x
        self._group_count -= 1

    def size(self, x):
        """
        return member num of group to which x belongs.

        :param x:
        :return:
        """
        return -self._parents[self.find(x)]

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
        return [i for i in range(self._n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self._parents) if x < 0]

    def group_count(self):
        return self._group_count

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(
            '{}: {}'.format(r, self.members(r)) for r in self.roots())


def warshall_floyd(N, ABC):
    """
    ワーシャルフロイド法の実行結果を返す.
    ノードは0始まりとする.
    計算量 O(max(N**3, len(ABT)).
    :param N: node num
    :param ABC: double list [[nodeA, nodeB, cost], ...]
    :return:
    """
    inf = float('inf')
    re = [[0 if p == q else inf for p in range(N)] for q in range(N)]

    for a, b, c in ABC:
        re[a][b] = min(re[a][b], c)
        re[b][a] = min(re[b][a], c)

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                re[j][k] = min(re[j][k], re[j][i] + re[i][k])

    return re


def bellman_ford(N, ABC, start=0, isdirected=True):
    """
    ベルマンフォード法の実行結果を返す.
    ノードは0始まりとする.
    :param N: node num
    :param ABC: double list [[nodeA, nodeB, cost], ...]
    :param start: start node num
    :param isdirected: 'True' mean edge have directed
    :return: list [min cost of 'from start to 0', ...]
    """
    from collections import deque

    inf = float('inf')
    graph_map = [[] for _ in range(N)]
    re = [inf] * N
    for a, b, t in ABC:
        graph_map[a].append([b, t])
        if not isdirected:
            graph_map[b].append([a, t])
    re[start] = 0
    for _ in range(N - 1):
        dq = deque([start])
        while dq:
            now = dq.popleft()
            for n, t in graph_map[now]:
                if re[now] + t < re[n]:
                    re[n] = re[now] + t
                    dq.append(n)
    return re


def dijkstra(N, ABC, start=0):
    """
    ダイクストラ法の実行結果を返す.
    ノードは0始まりとする. 辺は有向なものとする.
    :param N: node num
    :param ABC: double list [[nodeA, nodeB, cost], ...]
    :param start: start node num
    :return: list [min cost of 'from start to 0', ...]
    """
    from heapq import heappush, heappop

    inf = float('inf')
    graph_map = [[] for _ in range(N)]
    re = [inf] * N
    for a, b, c in ABC:
        graph_map[a].append([b, c])
    re[start] = 0
    visited = [0] * N
    hq = [[0, start]]
    while hq:
        cost, now = heappop(hq)
        if visited[now]: continue
        visited[now] = 1
        for nxt, c in graph_map[now]:
            if re[now] + c < re[nxt]:
                re[nxt] = re[now] + c
                heappush(hq, [re[nxt], nxt])
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


def have_close_road(graph):
    """
    有向グラフに閉路が存在するかを判定する.
    - 終点のないノードを親ノードとする.
    - 親ノードをグラフから削除する.
      この操作によって新たに親ノードができた場合はその親ノードも削除する.
      これを親ノードがなくなるまで繰り返す.
    - ノードがすべて削除されれば閉路は存在しない(残っていれば存在する).
    todo: テストを作っておきたい

    :param graph: ノードiを始点とする枝jをまとめた2重list graph[i][j]
    :return: 閉路が存在する場合 Treu, それ以外は False.
    """
    node_num = len(graph)
    parent_num = [0] * node_num
    parent_flg = [1] * node_num
    for g in graph:
        for n in g:
            parent_num[n] += 1
            parent_flg[n] = 0

    remain_flg = [1] * node_num
    for i in range(node_num):
        if parent_flg[i] == 0:
            continue
        stack = [i]
        while stack:
            now = stack.pop(-1)
            remain_flg[now] = 0
            for j in graph[now]:
                parent_num[j] -= 1
                if parent_num[j] == 0:
                    stack.append(j)

    return False if sum(remain_flg) == 0 else True


if __name__ == '__main__':
    N = 6
    ABT = [[0, 1, 2],
           [0, 3, 4],
           [1, 2, 3],
           [2, 3, -2],
           [2, 5, 2],
           [3, 4, 2],
           [3, 5, 4],
           [4, 5, 1]]
    print(bellman_ford(N, ABT))
