from collections import Counter


def solve():
    N, M = map(int, input().split())
    XYZ = [[int(i) for i in input().split()] for _ in range(M)]
    cards = [1] * N
    magic = 0
    while True:
        XY = [i[0] for i in XYZ] + [i[1] for i in XYZ]
        if len(XY) == 0:
            break
        c = Counter(XY)
        most = c.most_common(1)[0][0]
        value = 0
        if cards[most] == 1:
            cards[most] = 0
            value += 1
        for xyz in XYZ:
            if xyz[0] == most or xyz[1] == most:
                target = xyz[0] if xyz[0] != most else xyz[1]
                if cards[xyz[0] - 1] == 1:
                    cards[xyz[0] - 1] = 0
                    value += 1
            XYZ.remove(xyz)
        magic += 1
        if value <= 1:
            break
    print(magic + sum(cards))


if __name__ == '__main__':
    solve()
