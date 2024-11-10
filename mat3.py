from __future__ import division
import sympy as sp
import math

def bissecao(f, a, b, TOL, N):
    i = 1
    fa = f(a)
    
    while i <= N:
        p = a + (b - a) / 2
        fp = f(p)
        
        if (fp == 0) or ((b - a) / 2 < TOL):
            return p
        
        i += 1
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p

    print("O método da Bisseção não convergiu após o número máximo de iterações.")
    return None


def newton_method(f_expr, p0, TOL, N):
    x = sp.symbols("x")
    f_sympy = sp.sympify(f_expr)
    f_prime = sp.diff(f_sympy, x)
    
    iteration = 0
    p0_aux = float(p0)
    
    while iteration < N:
        aux1 = f_sympy.subs(x, p0_aux)
        aux2 = f_prime.subs(x, p0_aux)
        
        if aux2 == 0:
            print("Derivada zero. O método não pode continuar.")
            return None
        
        p = p0_aux - aux1 / aux2
        
        if abs(p - p0_aux) < TOL:
            return p
        
        iteration += 1
        p0_aux = p
    
    print("O método de Newton-Raphson não convergiu após o número máximo de iterações.")
    return None


def main():
    print("Escolha o método para encontrar a raiz:")
    print("1 - Método da Bisseção")
    print("2 - Método de Newton-Raphson")
    method_choice = int(input("Digite o número do método desejado: "))

    if method_choice == 1:
        f_input = input("Digite a função f(x) para o método da Bisseção (exemplo: x**3 - 2*x - 5): ")
        a = float(input("Digite o extremo esquerdo do intervalo (a): "))
        b = float(input("Digite o extremo direito do intervalo (b): "))
        TOL = float(input("Digite a tolerância desejada: "))
        N = int(input("Digite o número máximo de iterações: "))
        
        f = eval("lambda x: " + f_input)
        
        print("\nMétodo da Bisseção:")
        raiz_bissecao = bissecao(f, a, b, TOL, N)
        if raiz_bissecao is not None:
            print(f"Aproximação da raiz pelo método da Bisseção: {raiz_bissecao}")
    
    elif method_choice == 2:
        f_input = input("Digite a função f(x) para o método de Newton-Raphson (exemplo: x**3 - 2*x - 5): ")
        p0 = float(input("Digite a aproximação inicial (p0): "))
        TOL = float(input("Digite a tolerância desejada: "))
        N = int(input("Digite o número máximo de iterações: "))
        
        print("\nMétodo de Newton-Raphson:")
        raiz_newton = newton_method(f_input, p0, TOL, N)
        if raiz_newton is not None:
            print(f"Aproximação da raiz pelo método de Newton-Raphson: {raiz_newton}")
    
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")


if __name__ == "__main__":
    main()
