import math
from collections.abc import Callable
from typing import NamedTuple

PASSO_PADRAO = 1e-6
TOLERANCIA_PADRAO = 1e-6
ITERACOES_MAX_PADRAO = 50 

type FuncaoReal = Callable[[float], float]

class Resultado(NamedTuple):
    raiz: float
    iteracoes: int
    convergido: bool
    historico: list[float]
    mensagem: str

def derivada_simetrica(f: FuncaoReal, h: float = PASSO_PADRAO) -> FuncaoReal:
    """
    Aproxima a derivada f'(x) com precisão de segunda ordem O(h²).
    """
    if h <= 0:
        raise ValueError("O passo h deve ser estritamente positivo.")
    return lambda x: (f(x + h) - f(x - h)) / (2.0 * h)

# ------------------------------- Método da Bisseção --------------------------------

def bissecao(
    f: FuncaoReal, 
    a: float, 
    b: float, 
    tol: float = TOLERANCIA_PADRAO, 
    max_iter: int = ITERACOES_MAX_PADRAO
) -> Resultado:
    """
    Método da Bisseção mostrando a tabela passo a passo.
    """
    if a > b:
        a, b = b, a
        
    try:
        fa = f(a)
        fb = f(b)
    except (ValueError, OverflowError) as e:
        return Resultado(float('nan'), 0, False, [], f"Falha na avaliação inicial: {e}")
        
    if abs(fa) < tol:
        return Resultado(a, 0, True, [a], "Limite 'a' já era a raiz.")
    if abs(fb) < tol:
        return Resultado(b, 0, True, [b], "Limite 'b' já era a raiz.")
        
    if fa * fb > 0:
        return Resultado(
            float('nan'), 0, False, [], 
            f"Intervalo [{a}, {b}] inválido (f(a)={fa:.2e}, f(b)={fb:.2e})."
        )
        
    historico = [a, b]
    
    # Cabeçalho da tabela de iterações
    print(f"\n{'Iter':>4} | {'a':>13} | {'b':>13} | {'m (Raiz)':>13} | {'f(m)':>13} | {'Erro Rel':>12}")
    print("-" * 80)
    
    x_antigo = a
    for k in range(1, max_iter + 1):
        m = a + (b - a) / 2.0
        try:
            fm = f(m)
        except (ValueError, OverflowError) as e:
            return Resultado(m, k, False, historico, f"Erro matemático no ponto médio {m}: {e}")
            
        historico.append(m)
        erro = abs(m - x_antigo) / max(abs(m), 1.0)
        
        # Exibe a linha atual da iteração
        print(f"{k:>4} | {a:>13.8f} | {b:>13.8f} | {m:>13.8f} | {fm:>13.6e} | {erro:>12.6e}")
        
        if abs(fm) < tol or (b - a) / 2.0 < tol:
            return Resultado(m, k, True, historico, "Convergência por tolerância atingida.")
            
        x_antigo = m
        if (fa > 0) == (fm > 0):  
            a = m
            fa = fm
        else:
            b = m
            fb = fm
            
    return Resultado((a + b) / 2.0, max_iter, False, historico, "Atingiu limite de iterações.")


# ------------------------------- Métodos da Falsa Posição ----------------------------------

def falsa_posicao(
    f: FuncaoReal, 
    a: float, 
    b: float, 
    tol: float = TOLERANCIA_PADRAO, 
    max_iter: int = ITERACOES_MAX_PADRAO
) -> Resultado:
    """
    Método da Falsa Posição mostrando a tabela de convergência.
    """
    if a > b:
        a, b = b, a
        
    try:
        fa = f(a)
        fb = f(b)
    except (ValueError, OverflowError) as e:
        return Resultado(float('nan'), 0, False, [], f"Falha na avaliação inicial: {e}")
        
    if abs(fa) < tol:
        return Resultado(a, 0, True, [a], "Limite 'a' já era a raiz.")
    if abs(fb) < tol:
        return Resultado(b, 0, True, [b], "Limite 'b' já era a raiz.")
        
    if fa * fb > 0:
        return Resultado(float('nan'), 0, False, [], "Intervalo inválido pelo Teorema de Bolzano.")
        
    historico = [a, b]
    x_antigo = a
    
    print(f"\n{'Iter':>4} | {'a':>13} | {'b':>13} | {'x (Raiz)':>13} | {'f(x)':>13} | {'Erro Rel':>12}")
    print("-" * 80)
    
    for k in range(1, max_iter + 1):
        denominador = fb - fa
        if abs(denominador) < 1e-15:
            return Resultado(x_antigo, k, False, historico, "Cancelamento numérico (f(b) - f(a) ≈ 0).")
            
        x1 = (a * fb - b * fa) / denominador
        try:
            fx1 = f(x1)
        except (ValueError, OverflowError) as e:
            return Resultado(x1, k, False, historico, f"Erro no ponto {x1}: {e}")
            
        historico.append(x1)
        erro = abs(x1 - x_antigo) / max(abs(x1), 1.0)
        
        print(f"{k:>4} | {a:>13.8f} | {b:>13.8f} | {x1:>13.8f} | {fx1:>13.6e} | {erro:>12.6e}")
        
        if abs(fx1) < tol or erro < tol:
            return Resultado(x1, k, True, historico, "Convergência por tolerância atingida.")
            
        x_antigo = x1
        if (fa > 0) == (fx1 > 0):
            a = x1
            fa = fx1
        else:
            b = x1
            fb = fx1
            
    return Resultado(x1, max_iter, False, historico, "Atingiu limite de iterações.")


# ------------------------------- Métodos de Newton-Raphson --------------------------------

def newton_raphson(
    f: FuncaoReal, 
    x0: float, 
    tol: float = TOLERANCIA_PADRAO, 
    max_iter: int = ITERACOES_MAX_PADRAO,
    h_derivada: float = PASSO_PADRAO
) -> Resultado:
    """
    Método de Newton-Raphson exibindo os passos e derivada numérica.
    """
    try:
        df = derivada_simetrica(f, h=h_derivada)
        fx = f(x0)
    except (ValueError, OverflowError) as e:
        return Resultado(x0, 0, False, [x0], f"Erro inicial: {e}")
        
    if abs(fx) < tol:
        return Resultado(x0, 0, True, [x0], "Chute inicial já era a raiz.")
        
    x = x0
    historico = [x]
    
    print(f"\n{'Iter':>4} | {'x_k':>13} | {'f(x_k)':>13} | {'f_num_dir(x_k)':>14} | {'Erro Rel':>12}")
    print("-" * 75)
    
    for k in range(1, max_iter + 1):
        try:
            dfx = df(x)
            if abs(dfx) < 1e-15:
                return Resultado(x, k, False, historico, f"Derivada nula detectada em x={x}.")
                
            x_novo = x - fx / dfx
            fx_novo = f(x_novo)
        except (ValueError, OverflowError) as e:
            return Resultado(x, k, False, historico, f"Erro durante iteração: {e}")
            
        historico.append(x_novo)
        erro = abs(x_novo - x) / max(abs(x_novo), 1.0)
        
        print(f"{k:>4} | {x_novo:>13.8f} | {fx_novo:>13.6e} | {dfx:>14.6f} | {erro:>12.6e}")
        
        if abs(fx_novo) < tol or erro < tol:
            return Resultado(x_novo, k, True, historico, "Convergência por tolerância atingida.")
            
        x = x_novo
        fx = fx_novo
        
    return Resultado(x, max_iter, False, historico, "Atingiu limite de iterações.")

# ------------------------------- Método da Secante --------------------------------

def secante(
    f: FuncaoReal, 
    x0: float, 
    x1: float, 
    tol: float = TOLERANCIA_PADRAO, 
    max_iter: int = ITERACOES_MAX_PADRAO
) -> Resultado:
    """
    Método da Secante mostrando as iterações e o erro relativo.
    """
    if abs(x0 - x1) < 1e-15:
        raise ValueError("Chutes iniciais devem ser distintos.")
        
    try:
        f0 = f(x0)
        f1 = f(x1)
    except (ValueError, OverflowError) as e:
        return Resultado(float('nan'), 0, False, [], f"Falha na avaliação inicial: {e}")
        
    if abs(f0) < tol:
        return Resultado(x0, 0, True, [x0], "x0 já era a raiz.")
    if abs(f1) < tol:
        return Resultado(x1, 0, True, [x1], "x1 já era a raiz.")
        
    historico = [x0, x1]
    
    print(f"\n{'Iter':>4} | {'x_k':>13} | {'f(x_k)':>13} | {'Erro Rel':>12}")
    print("-" * 55)
    
    for k in range(1, max_iter + 1):
        denominador = f1 - f0
        if abs(denominador) < 1e-15:
            return Resultado(x1, k, False, historico, "Inclinação da secante muito horizontal.")
            
        x2 = x1 - f1 * (x1 - x0) / denominador
        try:
            f2 = f(x2)
        except (ValueError, OverflowError) as e:
            return Resultado(x1, k, False, historico, f"Erro na iteração: {e}")
            
        historico.append(x2)
        erro = abs(x2 - x1) / max(abs(x2), 1.0)
        
        print(f"{k:>4} | {x2:>13.8f} | {f2:>13.6e} | {erro:>12.6e}")
        
        if abs(f2) < tol or erro < tol:
            return Resultado(x2, k, True, historico, "Convergência por tolerância atingida.")
            
        x0, x1 = x1, x2
        f0, f1 = f1, f2
        
    return Resultado(x1, max_iter, False, historico, "Atingiu limite de iterações.")

# ------------------------ Main para teste rápido --------------------------------
