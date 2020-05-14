"""
2回目:
    kの考慮(ki, si1, ... と, k が最初に連携されてくること) が抜けていた

"""

def solve():
    N, M = map(int, input().split())
    S = [sum([2 ** (int(i) - 1) for i in input().split()][1:]) for _ in
              range(M)]
    P = [int(i) for i in input().split()]
    count = 0
    for i in range(2 ** N):
        for s, p in zip(S, P):
            if bin(s & i).count('1') % 2 != p:
                break
        else:
            count += 1
            # print(bin(i))

    print(count)


if __name__ == '__main__':
    solve()
