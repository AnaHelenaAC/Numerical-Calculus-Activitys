import math

def bissecao(f, a, b, epsilon=1e-6, max_iter=100, verbose=True, n_scan=200):
    """
    Resolve f(x) = 0 pelo método da bisseção no intervalo [a, b].
    Informa se há raiz garantida no intervalo e em qual iteração o processo parou.
    Se f(a)*f(b) > 0, faz uma varredura para checar se ainda há raízes
    (caso de número par de raízes no intervalo).
    """
    if a > b:
            a, b = b, a
    
    fa, fb = f(a), f(b)

    # Verifica se os limites já são raízes exatas

    if abs(f(a)) < epsilon:
        if verbose:
            print(f"x = {a} já é raiz aproximada (|f(a)| = {abs(fa):.2e} < ε = {epsilon}). Parou na iteração 0.")
        return a, 0
    if abs(f(b)) < epsilon:
        if verbose:
            print(f"x = {b} já é raiz aproximada (|f(b)| = {abs(fb):.2e} < ε = {epsilon}). Parou na iteração 0.")
        return b, 0
    
    # Verifica se o Teorema do Valor Intermediário garante raiz no intervalo
    if fa * fb > 0:
        if verbose:
            print(f"f(a)={fa:.4f} e f(b)={fb:.4f} têm o mesmo sinal em [{a}, {b}].")
            print("Isso não garante ausência de raiz -- pode haver um número par de raízes.")
            print(f"Fazendo uma varredura com {n_scan} subintervalos para verificar...\n")

        passo = (b - a) / n_scan
        x_atual = a
        f_atual = f(x_atual)
        subintervalos_com_raiz = []

        for i in range(n_scan):
            x_prox = x_atual + passo
            f_prox = f(x_prox)

            if f_atual == 0:
                subintervalos_com_raiz.append((x_atual, x_atual))
            elif f_atual * f_prox < 0:
                subintervalos_com_raiz.append((x_atual, x_prox))

            x_atual, f_atual = x_prox, f_prox

        if f_atual == 0:
            subintervalos_com_raiz.append((x_atual, x_atual))

        if not subintervalos_com_raiz:
            if verbose:
                print(f"Nenhuma troca de sinal encontrada na varredura de [{a}, {b}].")
                print("Não há raiz nesse intervalo (ou é uma raiz de multiplicidade par, indetectável por sinal).")
            return None, 0

        if verbose:
            print(f"Encontradas {len(subintervalos_com_raiz)} raiz(es) em subintervalos com troca de sinal:")
        resultados = []
        for (ai, bi) in subintervalos_com_raiz:
            if ai == bi:
                if verbose:
                    print(f"  Raiz exata em x = {ai:.6f}")
                resultados.append((ai, 0))
            else:
                raiz, n_iter = bissecao(f, ai, bi, epsilon, max_iter, verbose=False)
                if verbose:
                    print(f"  Raiz em x ≈ {raiz:.8f} (subintervalo [{ai:.4f}, {bi:.4f}], {n_iter} iterações)")
                resultados.append((raiz, n_iter))

        return resultados[0]

    if fa == 0:
        if verbose:
            print(f"x = {a} já é raiz exata (f(a) = 0). Parou na iteração 0.")
        return a, 0
    if fb == 0:
        if verbose:
            print(f"x = {b} já é raiz exata (f(b) = 0). Parou na iteração 0.")
        return b, 0

    if verbose:
        print(f"Há raiz garantida no intervalo [{a}, {b}], pois f(a) e f(b) têm sinais opostos.")


    # ESTIMATIVA DO NUNERO DE ITERAÇÕES NECESSARIAS
    n_estimado = math.ceil(math.log2((b - a) / epsilon))


    if verbose:
        print(f"Iterações estimadas: n > log2((b0-a0)/eps) => n ~ {n_estimado}\n")

    a_n, b_n = a, b
    fa_n, fb_n = fa, fb
    
    # --- TABELA DE ITERAÇÕES CORRIGIDA ---
    if verbose:
        print(f"{'k':>4} {'a_k':>14} {'b_k':>14} {'x_k':>14} {'f(x_k)':>18} {'b_k - a_k':>14}")
        print("-" * 92)
    
    for n in range(1, max_iter + 1):
        c = (a_n + b_n) / 2
        fc = f(c)
        
        # Exibe a linha da tabela
        if verbose:
            print(f"{n:>4} {a_n:>14.8f} {b_n:>14.8f} {c:>14.8f} {fc:>18.8e} {b_n - a_n:>14.6e}")
        
        # Critérios de parada
        if abs(fc) < 1e-14:
            if verbose:
                print("\n" + "-" * 92)
                print(f"Raiz exata encontrada: x = {c:.10f}")
                print(f"Processo parou na iteração {n} (f(c) ≈ 0).")
            return c, n
        
        if (b_n - a_n) / 2 < epsilon:
            if verbose:
                print("\n" + "-" * 92)
                print(f"Raiz aproximada encontrada: x = {c:.10f}")
                print(f"Processo parou na iteração {n} (erro < epsilon = {epsilon}).")
            return c, n
        
        # Atualiza o intervalo
        if fa_n * fc < 0:
            b_n = c
            fb_n = fc
        else:
            a_n = c
            fa_n = fc

    if verbose:
        print(f"\n Número máximo de iterações ({max_iter}) atingido sem convergência.")
    return None, max_iter


# Exemplo de uso
if __name__ == "__main__":
    f = lambda x: math.exp(-x) - x  # Função para encontrar a raiz   
   
    raiz, iteracoes = bissecao(f, a=0, b=1, epsilon=1e-6, verbose=True)
    
    if raiz is not None:
        print(f"\n{'='*50}")
        print(f"RESULTADO FINAL:")
        print(f"  Raiz ≈ {raiz:.10f}")
        print(f"  Iterações: {iteracoes}")
        print(f"  f(raiz) = {f(raiz):.2e}")
        print(f"{'='*50}")