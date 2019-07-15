def solve():
    H, W = map(int, input().split())
    mass = [[-1] * (W + 2) for _ in range(H + 2)]
    massT = [[-1] * (H + 2) for _ in range(W + 2)]
    import pprint
    pprint.pprint(mass)
    pprint.pprint(massT)
    for Hi in range(H):
        massHi = [0 if s == '.' else 1 for s in list(input())]
        print(massHi)
        for Wi in range(W):
            mass[Hi + 1][Wi + 1] = massHi[Wi]
            massT[Wi + 1][Hi + 1] = massHi[Wi]
    import pprint
    pprint.pprint(mass)
    pprint.pprint(massT)

    for Hi in range(1, H + 1):
        for Wi in range(1, W + 1):
            # Left
            L = 0
            for Li in reversed(list(range(0, Wi))):
                L += 1
                if mass[Hi][Li] == 1:
                    break
                elif mass[Hi][Li] == -1:
                    L = -1
                    break
            # Right
            R = 0
            for Ri in reversed(list(range(Wi + 1, W + 2))):
                R += 1
                if mass[Hi][Ri] == 1:
                    break
                elif mass[Hi][Ri] == -1:
                    R = -1
                    break
            # Up
            U = 0
            for Ui in reversed(list(range(Wi + 1, W + 2))):
                U += 1
                if mass[Hi][Ri] == 1:
                    break
                elif mass[Hi][Ri] == -1:
                    R = -1
                    break
            # Down
            pass


if __name__ == '__main__':
    solve()
