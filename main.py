from colorama import Fore, Style
import datainput
import graphic
import numpy as np
from solver import euler_method, milnes_method

if __name__ == '__main__':
    print(Fore.GREEN + "Лабораторная работа №6" + Style.RESET_ALL)
    print(Fore.GREEN + "Численное дифферинцирование" + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "Вариант №6" + Style.RESET_ALL)
    data = datainput.input_data()
    answer = None
    if data['method'] == 1:
        answer = euler_method.solve(data['func'], data['a'], data['b'], data['y0'], data['h'])
    elif data["method"] == 2:
        answer = milnes_method.solve(data["func"], 0, data["y0"], data["h"], data["differentiated_func"])
    else:
        print(Fore.RED + "Метод не выбран!" + Style.RESET_ALL)
    if answer is not None:
        print(answer)
        x = np.array([dot[0] for dot in answer])
        y = np.array([dot[1] for dot in answer])
        acc_x = np.linspace(np.min(x), np.max(x), 100)
        acc_y = [data['differentiated_func'](i) for i in acc_x]
        graphic.plot(x, y, acc_x, acc_y)
        print("Ответ:")
        print("%15s %10s %25s" % ("xn", "yn", "точное значение"))
        for i in range(0, len(answer)):
            print("%15f %15f %15f" % (answer[i][0], answer[i][1], data['differentiated_func'](answer[i][0])))
