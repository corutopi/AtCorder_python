

def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    Amax = max(A)
    A2 = A.copy()
    A2.remove(Amax)
    Asecond = max(A2)
    for a in A:
        if a == Amax:
            print(Asecond)
        else:
            print(Amax)


if __name__ == '__main__':
    solve()
