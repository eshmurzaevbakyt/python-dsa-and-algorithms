def matrix(n):
    array = [[0] * n for _ in range(n)]
    array_value = 0
    l, r, t, b = 0, n - 1, 0, n - 1
    while array_value < n * n:
        for i in range(l, r + 1):
            array_value += 1
            array[t][i] = array_value
        t += 1

        for j in range(t, b + 1):
            array_value += 1
            array[j][r] = array_value
        r -= 1

        for i in range(r, l - 1, -1):
            array_value += 1
            array[b][i] = array_value
        b -= 1

        for j in range(b, t - 1, - 1):
            array_value += 1
            array[j][l] = array_value
        l += 1
    return array

n = 4
arr = matrix(n)
print(arr)
