from sympy import *
from sympy.abc import a, x, y
import random

if __name__ == '__main__':
    x = symbols("x") 
    s = str()
    a = random.randint(1, 100) # �������� �������� ��������� a � b
    b = random.randint(1, 100) 
    integ = integrate(1/x/sqrt(a*x+b), x) # ��������� ������������� ��������
    for i in range(100):
        predel_1 = random.randint(1, 100) # �� ������ �������� ����������� ����� �������
        predel_2 = random.randint(100, 200) 
        result = (integ.subs(x, predel_2) - integ.subs(x, predel_1)).evalf() # ��������� ��������� 
        print(result)
        s += (str(result) + '\n') # ������� ��������� � ������
    with open("results.txt", mode="w") as f:
        f.write(s) # ���������� ������ � ����


