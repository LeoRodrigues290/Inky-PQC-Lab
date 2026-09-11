# Algoritmo HHL (Harrow-Hassidim-Lloyd)

Publicado em 2009, o algoritmo HHL resolve sistemas lineares de equações $A x = b$ em tempo logarítmico na dimensão da matriz sob condições ideais.

## Vantagem de Complexidade
- **Clássico (Conjugate Gradient):** $\mathcal{O}(N s \kappa)$, onde $N$ é o tamanho, $s$ é a esparsidade e $\kappa$ é o condition number.
- **Quântico HHL:** $\mathcal{O}(\log(N) s^2 \kappa^2 / \epsilon)$.

## Etapas Principais
1. Preparação do estado quântico $|b\rangle$.
2. Decomposição espectral via QPE com Hamiltoniano $e^{i A t}$.
3. Rotação controlada de um qubit ancilla proporcional aos autovalores invertidos $\lambda_j^{-1}$.
4. Uncomputation da QPE.
5. Post-selection na ancilla obtendo o estado proporcional a $|x\rangle = A^{-1}|b\rangle$.
