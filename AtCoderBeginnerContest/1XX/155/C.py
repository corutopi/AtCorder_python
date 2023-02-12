def solve(N, Ss):
    d = {}
    _max = 0
    for s in Ss:
        d.setdefault(s, 0)
        d[s] += 1
        _max = max(_max, d[s])

    d = [x[0] for x in d.items() if x[1] == _max]
    d.sort()
    for s in d:
        print(s)


if __name__ == '__main__':
    N = int(input())
    Ss = [input() for _ in range(N)]
    solve(N, Ss)
