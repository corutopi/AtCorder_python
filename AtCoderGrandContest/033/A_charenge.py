"""
解説と提出 #5747380を参考に作成
"""

from collections import deque


def solve():
    H, W = map(int, input().split())
    # mass = [[False] * W for _ in range(H)]
    # queue1 = deque([])
    # queue2 = deque([])
    queue1 = []
    queue2 = []
    mass = []
    mass.append([False] * (W + 2))  # 外枠
    for Hi in range(1, H + 1):
        mass.append([False] + [s == '.' for s in list(input())] + [False])  # else文は意外と時間を食う
        for Wi in range(1, W + 1):
            if not mass[Hi][Wi]:
                queue1.append((Hi, Wi))
    mass.append([False] * (W + 2))  # 外枠
    import datetime
    d = datetime.datetime.now()
    count = -1
    while True:
        # print('count: {}, queue:{}'.format(count, len(queue1)))
        if len(queue1) == 0:
            break
        for h, w in queue1:
            # left
            if mass[h][w - 1]:
                mass[h][w - 1] = False
                queue2.append((h, w - 1))
            # right
            if mass[h][w + 1]:
                mass[h][w + 1] = False
                queue2.append((h, w + 1))
            # top
            if mass[h + 1][w]:
                mass[h + 1][w] = False
                queue2.append((h + 1, w))
            # button
            if mass[h - 1][w]:
                mass[h - 1][w] = False
                queue2.append((h - 1, w))

        count += 1
        queue1 = queue2
        queue2 = []
    print(count)

    # print(datetime.datetime.now() - d)


if __name__ == '__main__':
    solve()
