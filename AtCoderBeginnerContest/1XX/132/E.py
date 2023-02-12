import func


def solve():
    N, M = map(int, input().split())
    G = [[int(i) for i in input().split()] for _ in range(M)]
    S, T = map(int, input().split())
    # 有向グラフをN倍化する
    G_ = double_directed_graph(G, 3)
    # func.ppprint(G_)
    # 幅優先探索
    start_map = [[] for _ in range(N + 1)]
    for g in G_:
        start_map[g[0]].append(g)
    count = 0
    queue = [(S, 0)]
    while True:
        if count >= len(queue):
            # 条件達成経路無し
            break
        tag = queue[count]
        if tag[1] > M:
            # 条件達成経路無し
            break
        if tag[0] == T:
            # 条件達成
            print(tag[1])
            return
        for smg in start_map[tag[0]]:
            queue.append((smg[1], tag[1] + 1))
        count += 1
    print(-1)


def double_directed_graph(edge, n):
    # argument check
    # if n < 2:
    #     raise ValueError('please set n >= 2')
    # main
    import copy
    max_node = 0
    for e in edge:
        max_node = max([max_node] + e)
    start_map = [[] for _ in range(max_node + 1)]
    result = copy.deepcopy(edge)
    for r in result:
        # r.append([[r[0], r[1]]])
        start_map[r[0]].append([r[0], r[1]])
    for i in range(n - 1):
        new_ver = []
        for r in result:
            # 終わりから始まる経路を抜き出す
            tag = start_map[r[1]]
            # tag = [vv for vv in edge if vv[0] == r[1]]
            # 経路の行先分だけ経路を複製する
            for t in tag:
                # print('tag', tag)
                v2 = r.copy()
                v2[1] = t[1]
                # v2[2].append(t.copy())
                new_ver.append(v2)
        result = new_ver
    return result


if __name__ == '__main__':
    solve()
