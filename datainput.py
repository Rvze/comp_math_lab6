from colorama import Fore, Style
import math


def getfunc(func_id):
    if func_id == 1:
        return lambda x, y: (3 * (x ** 2) * y) + (x ** 2 * (math.exp(x ** 3))), \
               lambda x: (x ** 3 * (math.exp(x ** 3))) / 3, \
               0, \
               1, \
               0
    elif func_id == 2:
        return lambda x, y: math.cos(x) - y, \
               lambda x: math.sin(x), \
               0, \
               0.1, \
               0.5
    elif func_id == 3:
        return lambda x, y: y + (1 + x) * y ** 2,\

    else:
        return None


def input_data():
    data = {}
    print("Выберите метод дифферинцирования:")
    print("1 - Метод Эйлера")
    print("2 - Метод Милна")
    method_choise = None
    while method_choise != 1 and method_choise != 2:
        method_choise = int(input(Fore.GREEN + "   >>>" + Style.RESET_ALL))
    data["method"] = method_choise

    print("Выберите уравнение:")
    print(Fore.GREEN + "   1 -" + Style.RESET_ALL, "y'=3*x^2 * y+x^2 * e^(x^3)\n   x∈[0;1]\n   y(0) = 0")
    print("\n", Fore.CYAN + 50 * "-" + Style.RESET_ALL, "\n")
    print(Fore.GREEN + "   2 -" + Style.RESET_ALL, "y'=cos(x) - y \n   x∈[0;0,1]\n   y(0) = 1/2")
    while True:
        try:
            func_id = int(input("   >>>"))
            func, differentiated_func, a, b, y0 = getfunc(func_id)
            if func is None:
                raise AttributeError
            break
        except AttributeError:
            print("Выберите либо 1, либо 2")
    data["func"] = func
    data["differentiated_func"] = differentiated_func
    data["a"] = a
    data["b"] = b
    data["y0"] = y0

    print("\nВведите шаг точек.")
    while True:
        try:
            h = float(input("Шаг точек: "))
            if h <= 0:
                raise ArithmeticError
            break
        except (ValueError, ArithmeticError):
            print("Шаг точек должен быть положительным числом.")
    data['h'] = h
    return data
