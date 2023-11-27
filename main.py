import numpy as np
from pade import pade_approximation
import sympy as smp

def main():
    while True:
        m = int(input("m: "))
        if m > 0:
            break

    while True:
        n = int(input("n: "))
        if n > 0:
            break
    x= smp.symbols('x', real=True)
    func= smp.exp(-x)       
    rat = pade_approximation(m, n, func)
    print(rat)
    

if __name__ == "__main__":
    main()
