# Quantum Approximate Optimization Algorithm (QAOA)

Proposto por Farhi, Goldstone e Gutmann (2014), o QAOA é uma heurística quântica para resolver problemas de otimização combinatória (ex: Max-Cut, TSP, 3-SAT).

## Hamiltoniano de Custo e de Mistura
- **Hamiltoniano do Problema:** $H_C = \sum_{i,j} J_{ij} Z_i Z_j + \sum_i h_i Z_i$
- **Hamiltoniano de Mistura:** $H_M = \sum_i X_i$

## Estado de $p$ Camadas
$$|\gamma, \beta\rangle = \prod_{l=1}^p \left( e^{-i \beta_l H_M} e^{-i \gamma_l H_C} \right) |+\rangle^{\otimes n}$$

Ao aumentar o número de camadas $p \to \infty$, a aproximação se aproxima do recozimento quântico adiabático com solução exata.
