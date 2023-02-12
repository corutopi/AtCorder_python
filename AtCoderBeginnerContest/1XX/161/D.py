def solve(K):
    lun = [0]

    def nextLunlun(arr, d=0):
        arr[d] += 1
        if arr[d] == 10:
            if d + 1 == len(arr):
                arr.append(1)
                arr[d] = 0
                return arr
            else:
                arr = nextLunlun(arr, d + 1)
                arr[d] = arr[d + 1] - 1 if arr[d + 1] > 0 else 0
                return arr
        if d + 1 != len(arr):
            if abs(arr[d] - arr[d + 1]) > 1:
                if arr[d] < arr[d + 1]:
                    arr[d] = arr[d + 1] - 1
                    return arr
                else:
                    arr = nextLunlun(arr, d + 1)
                    arr[d] = arr[d + 1] - 1 if arr[d + 1] > 0 else 0
                    return arr
        return arr

    for _ in range(K):
        lun = nextLunlun(lun)

    ans = 0
    for i in range(len(lun)):
        ans += lun[i] * (10 ** i)

    print(ans)


if __name__ == '__main__':
    K = int(input())
    solve(K)
