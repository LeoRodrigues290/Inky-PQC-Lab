# Algoritmo de Bernstein-Vazirani

Extensão natural do Deutsch-Jozsa projetada por Ethan Bernstein e Umesh Vazirani em 1993.

## Problema
Dada uma função $f(x) = s \cdot x \pmod 2$, onde $s \in \{0,1\}^n$ é uma string oculta e $\cdot$ representa o produto escalar binário:
$$s \cdot x = \sum_{i=1}^n s_i x_i \pmod 2$$

## Complexidade
- **Clássico:** Requer $n$ consultas (testando vetores unitários $e_i$).
- **Quântico:** Requer **apenas 1 consulta**!

O estado final após a aplicação de Hadamard e medição colapsa deterministicamente para o estado $|s\rangle$.
