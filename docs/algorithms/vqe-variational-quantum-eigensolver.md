# Variational Quantum Eigensolver (VQE)

O VQE é um algoritmo híbrido quântico-clássico projetado especificamente para a era NISQ (Noisy Intermediate-Scale Quantum).

## Teorema Variacional
Para qualquer Hamiltoniano $H$ e estado de teste parametrizado $|\psi(\vec{\theta})\rangle$:
$$\langle \psi(\vec{\theta}) | H | \psi(\vec{\theta}) \rangle \ge E_0$$
onde $E_0$ é a energia do estado fundamental.

## Loop Híbrido
1. **QPU:** Prepara o ansatz $|\psi(\vec{\theta})\rangle$ e mede os valores esperados dos termos de Pauli em $H$.
2. **CPU Clássica:** Executa um otimizador (COBYLA, SPSA, Adam) para sugerir novos parâmetros $\vec{\theta}_{k+1}$.
3. Repete até convergência do valor de energia.
