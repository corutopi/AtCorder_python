from heapq import heappop, heappush
from collections import deque


def solve():
    N, M = map(int, input().split())
    loadmap = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        loadmap[A].append(B)
        loadmap[B].append(A)

    dbrmap = [[float('inf'), -1, 0] for _ in range(N + 1)]  # 部屋の深度, しるべ, 予約状態

    # rooms = [[0, 1, 0]]  # [移動前の部屋, 移動後(現在)の部屋, 深度]
    rooms = deque()
    rooms.append([0, 1, 0])
    dbrmap[1][2] = 1
    while rooms:
        # br, r, d = heappop(rooms)
        br, r, d = rooms.popleft()
        if d <= dbrmap[r][0]:
            # update room data
            dbrmap[r][0] = d
            dbrmap[r][1] = br
            # add new room data
            for load in loadmap[r]:
                # heappush(rooms, [r, l, d + 1])
                if dbrmap[load][2] == 0:
                    rooms.append([r, load, d + 1])
                    dbrmap[load][2] = 1

    if min([db[1] for db in dbrmap[1:]]) <= -1:
        print('No')
    else:
        print('Yes')
        for db in dbrmap[2:]:
            print(db[1])


if __name__ == '__main__':
    solve()
