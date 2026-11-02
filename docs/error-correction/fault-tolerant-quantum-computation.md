# Computação Quântica Tolerante a Falhas e Teorema do Limiar

A tolerância a falhas garante que erros induzidos por ruído físico ou portas imperfeitas sejam corrigidos mais rapidamente do que se acumulam.

## Teorema do Limiar Quântico (Quantum Threshold Theorem)
Se a taxa de erro física por porta unitária $p$ estiver estritamente abaixo de um valor crítico $p_{\text{th}}$ ($p < p_{\text{th}}$):
Um circuito quântico de profundidade arbitrária $D$ pode ser simulado com probabilidade de falha $\epsilon$ usando apenas um overhead polilogarítmico em recursos físicos:
$$\mathcal{O}(\text{poly}(\log(D/\epsilon)))$$
