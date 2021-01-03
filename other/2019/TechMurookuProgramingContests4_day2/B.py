
def solve():
    N, M = map(int, input().split())
    data_map = [[] for _ in range(N + 1)]
    for _ in range(N- 1):
        A, B = map(int, input().split())
        data_map[A].append(B)
        data_map[B].append(A)
    C = [int(i) for i in input().split()]

    new_map = [[] for _ in range(N + 1)]
    dfs(data_map, C[0], 0, C, 0, new_map)
    count = 0
    print(new_map)
    for nm in new_map:
        if len(nm) == 1:
            count += 1
    if len(C) == 1 or count == 2:
        print('YES')
    else:
        print('trumpet')


# 写真のある街だけをつなげた木をnew_mapに作る
def dfs(data_map, tag, parent, C, new_parent, new_map):
    np = new_parent
    if tag in C:
        if new_parent != 0:
            new_map[tag].append(new_parent)
            new_map[new_parent].append(tag)
        np = tag
    stack = []
    for i in data_map[tag]:
        if i != parent:
            stack.append(i)
    for i in stack:
        dfs(data_map, i, tag, C, np, new_map)


if __name__ == '__main__':
    solve()
