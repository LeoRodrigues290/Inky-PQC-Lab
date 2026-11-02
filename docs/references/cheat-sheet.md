# Quantum Computing & PQC Cheat Sheet

## Operadores de Pauli
$$I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

## Portas Fundamentais
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}, \quad T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$$

## Padrões FIPS PQC
- **FIPS 203:** ML-KEM (KEM Baseado em Module-Lattice)
- **FIPS 204:** ML-DSA (Assinatura Digital Module-Lattice)
- **FIPS 205:** SLH-DSA (Assinatura Digital Stateless Hash-Based)
