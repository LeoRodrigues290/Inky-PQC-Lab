# Algoritmo de Deutsch-Jozsa

O Algoritmo de Deutsch-Jozsa foi um dos primeiros exemplos a demonstrar vantagem quântica determinística exponencial sobre algoritmos clássicos exatos.

## Problema
Dada uma função booleana $f: \{0,1\}^n \to \{0,1\}$, determine se $f$ é:
- **Constante:** retorna o mesmo valor para todas as entradas ($0$ ou $1$).
- **Balanceada:** retorna $0$ para metade das entradas e $1$ para a outra metade.

## Complexidade
- **Clássico Determinístico:** $2^{n-1} + 1$ consultas no pior caso.
- **Quântico:** Exatamente **1 consulta** ao oráculo.

## Circuito
1. Prepara $|0\rangle^{\otimes n} |1\rangle$.
2. Aplica portas Hadamard $H^{\otimes (n+1)}$ gerando kickback de fase.
3. Consulta o oráculo $U_f$.
4. Aplica Hadamard $H^{\otimes n}$ nos primeiros $n$ qubits.
5. Mede: se todos forem $|0\rangle$, $f$ é constante; caso contrário, é balanceada.
