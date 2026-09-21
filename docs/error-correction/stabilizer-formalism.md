# Formalismo dos Estabilizadores (Gottesman-Knill)

Estrutura matemática fundamental desenvolvida por Daniel Gottesman em 1997 para codificar e manipular códigos de correção de erros quânticos.

## Grupo de Pauli e Estabilizador
- Seja $\mathcal{G}_n$ o grupo de Pauli em $n$ qubits gerado por $\{\pm I, \pm i I, X, Y, Z\}^{\otimes n}$.
- Um subgrupo abeliano $S \subset \mathcal{G}_n$ que não contém $-I$ define um código estabilizador.
- O espaço de código $V_S$ é o conjunto de estados fixados por todos os operadores em $S$:
$$V_S = \{|\psi\rangle : M |\psi\rangle = |\psi\rangle, \forall M \in S\}$$
