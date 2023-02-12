import math

def solve():
    N = int(input())
    S = input()
    R = []
    G = []
    B = []

    # color separate
    for i in range(len(S)):
        if S[i] == 'R':
            R.append(i)
        elif S[i] == 'G':
            G.append(i)
        elif S[i] == 'B':
            B.append(i)

    # after color map
    lR = len(R)
    lG = len(G)
    lB = len(B)
    RGBmap = []
    for i in range(len(S)):
        if S[i] == 'R':
            lR -= 1
        elif S[i] == 'G':
            lG -= 1
        elif S[i] == 'B':
            lB -= 1
        RGBmap.append([lR, lG, lB])

    # calculate
    sum = 0
    for i in range(len(S)):
        if S[i] == 'R':
            a1 = G
            a2 = B
            b1 = 2
            b2 = 1
            c1 = 'B'
            c2 = 'G'
        elif S[i] == 'G':
            a1 = R
            a2 = B
            b1 = 2
            b2 = 0
            c1 = 'B'
            c2 = 'R'
        else:
            a1 = G
            a2 = R
            b1 = 0
            b2 = 1
            c1 = 'R'
            c2 = 'G'
        for a in a1:
            if i < a:
                sumb = RGBmap[a][b1]
                if sumb == 0:
                    continue
                if a + (a - i) < len(S) and S[a + (a - i)] == c1:
                    sumb -= 1
                sum += sumb
        for a in a2:
            if i < a:
                sumb = RGBmap[a][b2]
                if sumb == 0:
                    continue
                if a + (a - i) < len(S) and S[a + (a - i)] == c2:
                    sumb -= 1
                sum += sumb
    print(sum)


if __name__ == '__main__':
    solve()
