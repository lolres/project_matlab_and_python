﻿from sympy import *
from sympy.abc import a, x, y
import random
from time import *

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time() # время на начало выполнения функции
        result = func(*args, **kwargs)
        t2 = time() # время на конец выполнения функции
        with open("time.txt", mode='a') as f:
            f.write(f"{(t2-t1):.4f}s\n")
        print(f"{(t2-t1):.4f}s")
        return result
    return wrap_func

@timer_func
def rand_integral(x, predel_1, predel_2):
    result = (integ.subs(x, predel_2) - integ.subs(x, predel_1)).evalf() # результат вычисляем 
    print(result)
    return (str(result) + '\n') # возвращаем результат в виде строки

if __name__ == '__main__':
    x = symbols("x") 
    s = str()
    a = 54
    b = 77
    integ = integrate(1/x/sqrt(a*x+b), x) # вычисляем неопределённый интеграл

    predel_1 = 2 # 1ый определённый интеграл у нас совпадает 
    predel_2 = 10
    s += rand_integral(x, predel_1, predel_2)

    for i in range(1, 100):
        predel_1 = random.randint(1, 100) # на каждой итерации подставляем новые пределы
        predel_2 = random.randint(100, 200) 
        s += rand_integral(x, predel_1, predel_2)
    with open("results.txt", mode="w") as f:
        f.write(s) # записываем строку в файл


