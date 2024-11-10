from __future__ import division
import sympy as sp

def bissecao(f, a, b):
    iteration = 0
    max_iteration = 100
    aNew = a
    bNew = b

    error_x = 1
    error_f = 1
    precision = 10**(-10)

    while ((error_x > precision) or (error_f > precision)) and (iteration < max_iteration):
        p = (aNew + bNew) / 2
        if f(aNew) * f(p) > 0:
            aNew = p
        else:
            bNew = p

        error_x = abs(aNew - bNew)
        error_f = abs(f(aNew) - f(bNew))

        print(f'Iteração {iteration}: p = {p}')
        iteration += 1

    print(f'Total de iterações: {iteration}')
    return p

def newton_method(f_expr, p0):
    x = sp.symbols("x")
    f_sympy = sp.sympify(f_expr)
    d = sp.diff(f_sympy, x)

    iteration = 0
    max_iteration = 100

    error_x = 1
    error_f = 1
    precision = 10**(-10)
    p0_aux = float(p0)

    while ((error_x > precision) or (error_f > precision)) and (iteration < max_iteration):
        aux1 = f_sympy.subs(x, p0_aux)
        aux2 = d.subs(x, p0_aux)

        if aux2 == 0:
            print("Derivada zero. O método não pode continuar.")
            return None

        p = p0_aux - aux1 / aux2

        error_x = abs(p - p0_aux)
        error_f = abs(f_sympy.subs(x, p) - f_sympy.subs(x, p0_aux))

        print(f'Iteração {iteration}: p = {p}')
        iteration += 1
        p0_aux = p

    return p


def main():
    print("Escolha o método para encontrar a raiz:")
    print("1 - Método da Bisseção")
    print("2 - Método de Newton-Raphson")
    method_choice = int(input("Digite o número do método desejado: "))

    if method_choice == 1:
        f_input = input("Digite a função f(x) para o método da Bisseção (exemplo: x**3 - 2*x - 5): ")
        a = float(input("Digite o extremo esquerdo do intervalo (a): "))
        b = float(input("Digite o extremo direito do intervalo (b): "))
        
        f = eval("lambda x: " + f_input)
        
        print("\nMétodo da Bisseção:")
        raiz_bissecao = bissecao(f, a, b)
        print(f"Aproximação da raiz pelo método da Bisseção: {raiz_bissecao}")
    
    elif method_choice == 2:
        f_input = input("Digite a função f(x) para o método de Newton-Raphson (exemplo: x**3 - 2*x - 5): ")
        p0 = float(input("Digite a aproximação inicial (p0): "))
        
        print("\nMétodo de Newton-Raphson:")
        raiz_newton = newton_method(f_input, p0)
        print(f"Aproximação da raiz pelo método de Newton-Raphson: {raiz_newton}")
    
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")


if __name__ == "__main__":
    main()
