import sympy as sp

def newton_raphson(f, x0, tol=1e-10, max_iter=100, verbose=True):
    x = sp.symbols('x')
    f_prime = sp.diff(f, x)
    k = 1
    xk = x0

    if verbose:
        print("\n--- Método de Newton-Raphson ---")
        print(f"Iteração {k}: x0 = {xk}")
    
    while k <= max_iter:
        fxk = f.subs(x, xk)
        fpxk = f_prime.subs(x, xk)
        
        if fpxk == 0:
            print("Derivada zero. O método não pode continuar.")
            return None
        
        x_next = xk - fxk / fpxk
        
        if verbose:
            print(f"Iteração {k}: x = {xk:.6f}, f(x) = {fxk:.6f}, f'(x) = {fpxk:.6f}, x_next = {x_next:.6f}")
        
        if abs(x_next - xk) < tol:
            if verbose:
                print(f"Solução encontrada: x = {x_next:.6f} (em {k} iterações)")
            return x_next
        
        xk = x_next
        k += 1
    
    print("Número máximo de iterações alcançado.")
    return xk

def bissecao(f, a, b, tol=1e-10, max_iter=100, verbose=True):
    x = sp.symbols('x')
    fa = f.subs(x, a)
    fb = f.subs(x, b)
    
    # Verificação se os valores nos extremos do intervalo possuem sinais opostos
    if fa * fb > 0:
        print("Erro: f(a) e f(b) devem ter sinais opostos.")
        return None
    
    if verbose:
        print("\n--- Método da Bisseção ---")
    k = 1
    
    while k <= max_iter:
        c = (a + b) / 2
        fc = f.subs(x, c)
        
        if verbose:
            print(f"Iteração {k}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6f}")
        
        if abs(fc) < tol or (b - a) / 2 < tol:
            if verbose:
                print(f"Solução encontrada: x = {c:.6f} (em {k} iterações)")
            return c
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        k += 1
    
    print("Número máximo de iterações alcançado.")
    return (a + b) / 2

def main():
    expr = input("Digite a expressão da função em termos de x (ex: x**2 - 4): ")
    f = sp.sympify(expr)
    tol = float(input("Digite a tolerância: "))
    max_iter = int(input("Digite o número máximo de iterações: "))
    
    print("\nEscolha o método:")
    print("1 - Newton-Raphson")
    print("2 - Bisseção")
    metodo = int(input("Método: "))
    
    if metodo == 1:
        x0 = float(input("Digite o valor inicial x0 para Newton-Raphson: "))
        newton_raphson(f, x0, tol, max_iter, verbose=True)
    elif metodo == 2:
        a = float(input("Digite o valor inicial a para Bisseção: "))
        b = float(input("Digite o valor inicial b para Bisseção: "))
        bissecao(f, a, b, tol, max_iter, verbose=True)
    else:
        print("Método inválido.")

if __name__ == "__main__":
    main()
