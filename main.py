import numpy as np
from pade import pade_approximation
from sympy import symbols, exp, sin, cos
from generatepoints import generatepoints
import matplotlib.pyplot as plt

def main(func):
    print("Padé para a seguinte função:", func)
    while True:
        try:
            m = int(input("m: "))
            if m > 0:
                break
        except:
            print("Deve ser um valor positivo maior que zero")
            continue

    while True:
        try:
            n = int(input("n: "))
            if n > 0:
                break
        except:
            print("Deve ser um valor positivo maior que zero")
            continue

    ratio = pade_approximation(m, n, func)
    points = generatepoints(69)
    points.sort()
    resultspade = []
    resultfunc = []

    for _ in points:
        value = ratio.subs([(x, _)]).evalf()
        resultspade.append(value)
        valuefunc = func.subs([(x, _)]).evalf()
        resultfunc.append(valuefunc)

    resultfunc = np.array(resultfunc)
    resultspade = np.array(resultspade)
    error = resultfunc - resultspade
    norma_maxima = np.max(np.abs(error))
    norma_erro_l2 = (np.sum(np.array(error, dtype=float) ** 2)) ** (1/2)
    error = np.abs(error)

    print("Erro médio (soma dos erros em módulo pela quantidade de pontos):", np.mean(np.abs(error)), "\n", "Erro Max:", norma_maxima, "\n", "Norma L2:", norma_erro_l2)

    plt.plot(points, resultspade, label='Padé', color='red')
    plt.plot(points, resultfunc, label='Func', color='blue')
    plt.xlabel('Pontos')
    plt.ylabel('Valores')
    plt.legend()
    plt.show()

    plt.plot(points, error, label='Erro', color='blue')
    plt.xlabel('Pontos')
    plt.ylabel('Erro')
    plt.legend()
    plt.show()

x = symbols('x', real=True)

while True:
    main(exp(x) * sin(x) * cos(x))
    y = input("Deseja continuar (s/n)?")
    if y.lower() == "n":
        break

while True:
    main(exp(x) * sin(x) / cos(x) ** 2)
    y = input("Deseja continuar (s/n)?")
    if y.lower() == "n":
        break
