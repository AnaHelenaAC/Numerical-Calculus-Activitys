import math

def g(lam):
    return lam**3 - lam - 2

def dg(lam):
    return 3*lam**2 - 1

def newton(f, df, x0, tol=1e-8, max_iter=50):
    print("\n--- MÉTODO DE NEWTON-RAPHSON ---")
    print(f"{'k':>4} {'x_k':>18} {'h(x_k)':>22} {'Erro_rel (%)':>18}")
    print("-" * 70)
    
    xk = x0
    for k in range(max_iter + 1):
        fk = f(xk)
        dfk = df(xk)
        
        if k == 0:
            erro_rel = float('inf')
        else:
            erro_rel = abs((xk - x_ant) / xk) * 100 if abs(xk) > 1e-15 else float('inf')
        
        print(f"{k:>4} {xk:>18.10f} {fk:>22.10e} {erro_rel:>18.6e}")
        
        if abs(fk) < tol:
            print(f"\nConvergência em {k} iterações.")
            return xk, k
        
        if k == max_iter:
            print(f"Máximo de iterações atingido.")
            return xk, k
        
        if abs(dfk) < 1e-15:
            print("Derivada nula! Encerrando.")
            return xk, k
        
        x_ant = xk
        xk = xk - fk / dfk
    
    return xk, max_iter

def secante(f, x0, x1, tol=1e-6, max_iter=50):
    print("\n--- MÉTODO DE SECANTE ---")
    print(f"{'k':>4} {'x_k':>18} {'h(x_k)':>22} {'Erro_rel (%)':>18}")
    print("-" * 70)
    
    x_ant = x0
    xk = x1
    g_ant = f(x_ant)
    gk = f(xk)
    
    print(f"{0:>4} {x_ant:>18.10f} {g_ant:>22.10e} {'':>18}")
    print(f"{1:>4} {xk:>18.10f} {gk:>22.10e} {'':>18}")
    
    for k in range(2, max_iter + 1):
        if abs(gk - g_ant) < 1e-15:
            print("Divisão por zero! Encerrando.")
            break
        
        x_prox = xk - gk * (xk - x_ant) / (gk - g_ant)
        g_prox = f(x_prox)
        
        erro_rel = abs((x_prox - xk) / x_prox) * 100 if abs(x_prox) > 1e-15 else float('inf')
        
        print(f"{k:>4} {x_prox:>18.10f} {g_prox:>22.10e} {erro_rel:>18.6e}")
        
        if abs(g_prox) < tol:
            print(f"\nConvergência alcançada em {k} iterações.")
            return x_prox, k
        
        x_ant, xk = xk, x_prox
        g_ant, gk = gk, g_prox
    
    print(f"\nNúmero máximo de iterações ({max_iter}) atingido.")
    return xk, max_iter

# Execução
print("=" * 70)
print("COMPARAÇÃO NEWTON-RAPHSON × SECANTE")
print("=" * 70)

# Newton: x0 = 1.5
raiz_newton, iter_newton = newton(g, dg, 1.5, tol=1e-8)

# Secante: x0 = 1.0, x1 = 2.0
raiz_secante, iter_secante = secante(g, 1.0, 2.0, tol=1e-8)

# Tabela comparativa
print("\n" + "=" * 70)
print("RESUMO COMPARATIVO")
print("=" * 70)
print(f"{'Método':<20} {'Iterações':<15} {'Raiz encontrada':<20} {'g(raiz)':<20}")
print("-" * 75)
print(f"{'Newton-Raphson':<20} {iter_newton:<15} {raiz_newton:<20.10f} {g(raiz_newton):<20.10e}")
print(f"{'Secante':<20} {iter_secante:<15} {raiz_secante:<20.10f} {g(raiz_secante):<20.10e}")