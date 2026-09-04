# Estimativa de Fase Quântica (QPE)

A Estimativa de Fase Quântica é a espinha dorsal de algoritmos fundamentais como Shor, HHL e algoritmos quânticos de química computacional.

## Objetivo
Dado um operador unitário $U$ e um autoestado $|\psi\rangle$ tal que:
$$U |\psi\rangle = e^{2\pi i \theta} |\psi\rangle$$
com $\theta \in [0, 1)$, o QPE estima $\theta$ com $m$ bits de precisão.

## Estrutura
1. Registrador de contagem com $m$ qubits inicializados com Hadamard.
2. Portas controladas $U^{2^k}$ para codificar a fase na base de Fourier.
3. Transformada Quântica de Fourier Inversa ($QFT^\dagger$).
4. Medição dos qubits de contagem obtendo a melhor aproximação binária de $\theta$.
