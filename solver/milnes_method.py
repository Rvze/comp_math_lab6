def solve(func, x0, y0, h, diff_func):
    # Готовим первые 3 точки по методу Рунге-Кутта
    x = []
    y = []
    x.append(x0)

    y.append(y0)
    print(x)
    print(y)
    data = [(x[0], y[0])]
    for i in range(0, 3):
        k1 = h * func(x[i], y[i])
        k2 = h * func(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * func(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * func(x[i] + h, y[i] + k3)
        y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        x.append(x[i] + h)

    i = 3
    y_predictor = []
    y_corrector = []
    for i in range(3, 10):
        y_predictor.append(y[i - 4] + (4 * h / 3) * (
                2 * func(x[i - 3], y[i - 3]) - func(x[i - 2], y[i - 2]) + 2 * func(x[i - 1], y[i - 1])))
        y_corrector.append(y[i - 2] + (h / 3) * (
                func(x[i - 2], y[i - 2]) + 4 * func(x[i - 1], y[i - 1]) + func(x[i], y_predictor[i - 3])))
        eps = (abs(diff_func(y[i - 3]) - y[i - 3]))
        if abs(y_corrector[i - 3] - y_predictor[i - 3]) > eps:
            y.append(y_corrector[i - 3])
        else:
            y.append(y_predictor[i - 3])
        x.append(x[i] + h)
        # i += 1
        data.append((x[i], y[i]))
    return data
