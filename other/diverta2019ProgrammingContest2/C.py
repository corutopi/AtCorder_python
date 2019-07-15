
def solve():
    N = int(input())
    As = [int(i) for i in input().split()]
    As.sort()
    maxA = As.pop()
    minA = As.pop(0)
    upper0A = [i for i in As if i >= 0]
    lower0A = [i for i in As if i < 0]
    # print('maxA:', maxA)
    # print('minA:', minA)
    # print('upper0A:', upper0A)
    # print('lower0A:', lower0A)
    result_load = []
    for uA in upper0A:
        result_load.append([minA, uA])
        minA = minA - uA
    for lA in lower0A:
        result_load.append([maxA, lA])
        maxA = maxA - lA
    result_load.append([maxA, minA])
    resultA = maxA - minA

    # export
    print(resultA)
    for x, y in result_load:
        print(x, y)


if __name__ == '__main__':
    solve()
