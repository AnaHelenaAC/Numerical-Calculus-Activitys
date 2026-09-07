import math

def f(x):
    return math.exp(-x) - x  # Função para encontrar a raiz

def falsa_posicao(f, a, b, tol=1e-6, max_iter=3, verbose=True):
    """
    Método da Falsa Posição (Regula Falsi) para encontrar raiz de f(x) = 0.
    
    Parâmetros:
        f: função contínua
        a, b: intervalo [a, b] com f(a) e f(b) de sinais opostos
        tol: tolerância (critério de parada)
        max_iter: número máximo de iterações
        verbose: se True, exibe tabela de iterações
    
    Retorna:
        (raiz, iteracoes)
    """
    # Garante que a < b
    if a > b:
        a, b = b, a
    
    fa = f(a)
    fb = f(b)
    
    # ============================================================
    # VERIFICAÇÃO DE RAIZ NOS EXTREMOS
    # ============================================================
    if abs(fa) < tol:
        if verbose:
            print(f"x = {a} já é raiz aproximada (|f(a)| = {abs(fa):.2e} < ε = {tol}).")
        return a, 0
    
    if abs(fb) < tol:
        if verbose:
            print(f"x = {b} já é raiz aproximada (|f(b)| = {abs(fb):.2e} < ε = {tol}).")
        return b, 0
    
    # ============================================================
    # VERIFICAÇÃO DO TEOREMA DO VALOR INTERMEDIÁRIO
    # ============================================================
    if fa * fb >= 0:
        raise ValueError(f"O intervalo [{a}, {b}] não contém uma raiz garantida.")
    
    
    # ============================================================
    # TABELA DE ITERAÇÕES
    # ============================================================
    if verbose:
        print(f"{'k':>4} {'a':>14} {'b':>14} {'c':>14} {'f(c)':>18} {'b - a':>14}")
        print("-" * 92)
    
    for k in range(max_iter):
        # ============================================================
        # CÁLCULO DO PONTO DE INTERSEÇÃO (FÓRMULA DA FALSA POSIÇÃO)
        # ============================================================
        # Verifica divisão por zero
        if abs(fb - fa) < 1e-15:
            if verbose:
                print("  f(b) - f(a) ≈ 0. Método não pode prosseguir.")
            return (a + b) / 2, k
        
        # Fórmula correta: c = a - f(a) * (b - a) / (f(b) - f(a))
        c = a - fa * (b - a) / (fb - fa)
        fc = f(c)
        
        # Exibe a iteração
        if verbose:
            print(f"{k+1:>4} {a:>14.8f} {b:>14.8f} {c:>14.8f} {fc:>18.8e} {b - a:>14.6e}")
        
        # ============================================================
        # CRITÉRIOS DE PARADA
        # ============================================================
        if abs(fc) < tol:
            if verbose:
                print("\n" + "-" * 92)
                print(f" Convergência alcançada: |f(c)| = {abs(fc):.2e} < ε = {tol}")
            return c, k + 1
        
        if abs(b - a) < tol:
            if verbose:
                print("\n" + "-" * 92)
                print(f" Convergência alcançada: |b - a| = {abs(b - a):.2e} < ε = {tol}")
            return c, k + 1
        
        # ============================================================
        # ATUALIZAÇÃO DO INTERVALO
        # ============================================================
        if fc * fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    # ============================================================
    # MÁXIMO DE ITERAÇÕES ATINGIDO
    # ============================================================
    if verbose:
        print(f"\n Número máximo de iterações ({max_iter}) atingido.")
    return c, max_iter


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================
if __name__ == "__main__":
    # f(x) = e^(-x) - x  → raiz ≈ 0.5671432904
    a = 0.0
    b = 1.0
    
    print("=" * 60)
    print("MÉTODO DA FALSA POSIÇÃO (REGULA FALSI)")
    print("=" * 60)
    
    raiz, iteracoes = falsa_posicao(f, a, b, tol=1e-6, max_iter=3, verbose=True)
    
    print(f"\n{'='*60}")
    print(f"RESULTADO FINAL:")
    print(f"  Raiz ≈ {raiz:.10f}")
    print(f"  Iterações: {iteracoes}")
    print(f"  f(raiz) = {f(raiz):.2e}")
    print(f"{'='*60}")