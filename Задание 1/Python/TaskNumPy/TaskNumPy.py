import numpy as np
import os
from time import *

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time() # время на начало выполнения функции
        result = func(*args, **kwargs)
        t2 = time() # время на конец выполнения функции
        with open("time.txt", mode='a') as f:
            f.write(f"{(t2-t1):.4f}s\n")
        print(f"{(t2-t1):.4f}s\n")
        return result
    return wrap_func

@timer_func
def matrix_solve(m):
    A = m[:, :-1] # матрица
    b = m[:, -1] # вектор свободных членов
    x = np.linalg.solve(A, b)
    return x

if __name__ == '__main__':
    os.makedirs("data", exist_ok=True)
    for i in range(50):
        # создаём матрицу со 100 строками и 101 столбцом, где последний столбец будем в будущем использовать как вектор свободных членов
        m = np.random.randint(-100, 101, size=(100, 101))

        # сохраняем в файл матрицу
        np.savetxt(f"data/np_matrix_{i}.txt", m, fmt="%i")

        # получаем из файла матрицу (на самом деле это лишний шаг, можно его убрать и заменить m1 на m)
        m1 = np.loadtxt(f"data/np_matrix_{i}.txt", usecols=range(101), dtype=int)

        # решаем матрицу и сохраняем в файл результат
        x = matrix_solve(m1)
        np.savetxt(f"data/np_matrix_solved_{i}.txt", x, fmt="%f")

