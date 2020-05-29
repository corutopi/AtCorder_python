from math import floor, ceil


def solve(A, B):
    candidates = set()
    for i in range(10):
        _A = A + i * 0.1
        x = _A / 0.08
        candidates.add(floor(x))
        candidates.add(ceil(x))
    # print(candidates)

    for i in range(10):
        _B = B + i * 0.1
        x = _B / 0.1
        candidates.add(floor(x))
        candidates.add(ceil(x))
    # print(candidates)

    ans = -1
    for c in candidates:
        if floor(c * 0.08) == A and floor(c * 0.1) == B:
            ans = min(ans, c) if ans != -1 else c

    print(ans)


if __name__ == '__main__':
    A, B = map(int, input().split())
    solve(A, B)
