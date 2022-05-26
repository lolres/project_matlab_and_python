from sympy import *
from sympy.abc import a, x, y
import random

if __name__ == '__main__':
    x = symbols("x") 
    s = str()
    a = random.randint(1, 100) # выбираем рандомно константы a и b
    b = random.randint(1, 100) 
    integ = integrate(1/x/sqrt(a*x+b), x) # вычисл€ем неопределЄнный интеграл
    for i in range(100):
        predel_1 = random.randint(1, 100) # на каждой итерации подставл€ем новые пределы
        predel_2 = random.randint(100, 200) 
        result = (integ.subs(x, predel_2) - integ.subs(x, predel_1)).evalf() # результат вычисл€ем 
        print(result)
        s += (str(result) + '\n') # заносим результат в строку
    with open("results.txt", mode="w") as f:
        f.write(s) # записываем строку в файл


