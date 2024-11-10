import sympy as sp

def newton_raphson(funcao, ponto_inicial, tolerancia=1e-10, maximo_iteracoes=100, exibir_detalhes=True):
    x = sp.symbols('x')
    derivada_funcao = sp.diff(funcao, x)
    iteracao = 1
    estimativa_atual = ponto_inicial

    if exibir_detalhes:
        print("\n--- Método de Newton-Raphson ---")
        print(f"Iteração {iteracao}: Ponto inicial = {estimativa_atual}")
    
    while iteracao <= maximo_iteracoes:
        valor_funcao = funcao.subs(x, estimativa_atual)
        valor_derivada = derivada_funcao.subs(x, estimativa_atual)
        
        if valor_derivada == 0:
            print("Derivada zero. O método não pode continuar.")
            return None
        
        proxima_estimativa = estimativa_atual - valor_funcao / valor_derivada
        
        if exibir_detalhes:
            print(f"Iteração {iteracao}: x = {estimativa_atual:.6f}, f(x) = {valor_funcao:.6f}, f'(x) = {valor_derivada:.6f}, Próxima estimativa = {proxima_estimativa:.6f}")
        
        if abs(proxima_estimativa - estimativa_atual) < tolerancia:
            if exibir_detalhes:
                print(f"Solução encontrada: x = {proxima_estimativa:.6f} (em {iteracao} iterações)")
            return proxima_estimativa
        
        estimativa_atual = proxima_estimativa
        iteracao += 1
    
    print("Número máximo de iterações alcançado.")
    return estimativa_atual

def bissecao(funcao, limite_inferior, limite_superior, tolerancia=1e-10, maximo_iteracoes=100, exibir_detalhes=True):
    x = sp.symbols('x')
    valor_limite_inferior = funcao.subs(x, limite_inferior)
    valor_limite_superior = funcao.subs(x, limite_superior)
    
    if valor_limite_inferior * valor_limite_superior > 0:
        print("Erro: f(a) e f(b) devem ter sinais opostos.")
        return None
    
    if exibir_detalhes:
        print("\n--- Método da Bisseção ---")
    
    iteracao = 1
    
    while iteracao <= maximo_iteracoes:
        ponto_medio = (limite_inferior + limite_superior) / 2
        valor_ponto_medio = funcao.subs(x, ponto_medio)
        
        if exibir_detalhes:
            print(f"Iteração {iteracao}: Limite inferior = {limite_inferior:.6f}, Limite superior = {limite_superior:.6f}, Ponto médio = {ponto_medio:.6f}, f(Ponto médio) = {valor_ponto_medio:.6f}")
        
        if abs(valor_ponto_medio) < tolerancia or (limite_superior - limite_inferior) / 2 < tolerancia:
            if exibir_detalhes:
                print(f"Solução encontrada: x = {ponto_medio:.6f} (em {iteracao} iterações)")
            return ponto_medio
        
        if valor_limite_inferior * valor_ponto_medio < 0:
            limite_superior = ponto_medio
            valor_limite_superior = valor_ponto_medio
        else:
            limite_inferior = ponto_medio
            valor_limite_inferior = valor_ponto_medio
        
        iteracao += 1
    
    print("Número máximo de iterações alcançado.")
    return (limite_inferior + limite_superior) / 2

def main():
    expressao = input("Digite a expressão da função em termos de x (ex: x**2 - 4): ")
    funcao = sp.sympify(expressao)
    tolerancia = float(input("Digite a tolerância: "))
    maximo_iteracoes = int(input("Digite o número máximo de iterações: "))
    
    print("\nEscolha o método:")
    print("1 - Newton-Raphson")
    print("2 - Bisseção")
    metodo = int(input("Método: "))
    
    if metodo == 1:
        ponto_inicial = float(input("Digite o valor inicial x0 para Newton-Raphson: "))
        newton_raphson(funcao, ponto_inicial, tolerancia, maximo_iteracoes, exibir_detalhes=True)
    elif metodo == 2:
        limite_inferior = float(input("Digite o valor inicial a para Bisseção: "))
        limite_superior = float(input("Digite o valor inicial b para Bisseção: "))
        bissecao(funcao, limite_inferior, limite_superior, tolerancia, maximo_iteracoes, exibir_detalhes=True)
    else:
        print("Método inválido.")

if __name__ == "__main__":
    main()
