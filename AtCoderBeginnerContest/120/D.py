"""
D - Decayed Bridges
"""


def solve():
    N, M = map(int, input().split())
    island = [[n for n in range(1, N + 1)]]
    bridge = [list(map(int, input().split())) for i in range(M)]
    for m in range(M):
        lost_bridge = bridge.pop(0)
        # 崩壊した橋のある島グループを探す
        is_group = [island.pop(i) for i in range(len(island)) if
                    lost_bridge[0] in island[i]][0]
        # 島グループの検索を行い, 必要に応じて分断する
        group_1 = break_up_island(is_group[0], bridge)
        group_2 = [i for i in is_group if i not in group_1]

        # 島グループから不便さを求める
        # ただし島グループが一つのみの場合は0とする


def break_up_island(island, bridge):
    target = [island]
    for b in [b[1] for b in bridge if b[0] == island]:
        target += break_up_island(b, bridge)
    return target


if __name__ == '__main__':
    solve()
