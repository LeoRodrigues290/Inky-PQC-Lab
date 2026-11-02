# Algoritmo de Simon

Formulado por Daniel Simon em 1994, serviu de inspiração direta para Peter Shor criar o algoritmo de fatoração.

## O Problema do Período Oculto
Dada uma função $f: \{0,1\}^n \to \{0,1\}^n$ tal que $f(x) = f(y) \iff x \oplus y \in \{0^n, s\}$, onde $s$ é o período secreto.

## Complexidade
- **Clássico:** $\Omega(2^{n/2})$ consultas pelo paradoxo do aniversário.
- **Quântico:** $\mathcal{O}(n)$ consultas com resolução clássica por eliminação Gaussiana em $\mathbb{F}_2$.
