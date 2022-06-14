def solve(f, a, b, y0, h):
    dots_arr = [(a, y0)]
    print(dots_arr)
    n = int((b - a) / h) + 1
    for i in range(1, n):
        dots_arr.append((dots_arr[i - 1][0] + h,
                         dots_arr[i - 1][1] + h * f(dots_arr[i - 1][0], dots_arr[i - 1][1])))
    return dots_arr
