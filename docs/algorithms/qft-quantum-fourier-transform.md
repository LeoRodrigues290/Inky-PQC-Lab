# Transformada Quântica de Fourier (QFT)

A Transformada Quântica de Fourier mapeia a base computacional na base de Fourier quântica.

## Definição Matemática
$$|j\rangle \mapsto \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} \omega^{jk} |k\rangle, \quad \omega = e^{2\pi i / N}$$

## Decomposição em Portas Elementares
A QFT em $n$ qubits requer:
- Portas Hadamard ($H$)
- Portas de rotação controlada de fase $R_k$:
$$R_k = \begin{pmatrix} 1 & 0 \\ 0 & e^{2\pi i / 2^k} \end{pmatrix}$$
- Portas SWAP para reverter a ordem dos qubits.

**Complexidade de portas:** $\mathcal{O}(n^2)$ comparado a $\mathcal{O}(n 2^n)$ da FFT clássica.
