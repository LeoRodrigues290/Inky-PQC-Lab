# Redes Neurais Quânticas (QNNs)

As QNNs utilizam circuitos quânticos parametrizados (PQC) como camadas de aprendizado de máquina supervisionado e não-supervisionado.

## Arquitetura
1. **Feature Map:** Codificação dos dados clássicos $x$ em um estado quântico $|\Phi(x)\rangle$ (ZZFeatureMap, PauliFeatureMap).
2. **Ansatz Variacional:** Portas unitárias parametrizadas $U(\theta)$.
3. **Medição:** Valor esperado $\langle M \rangle = \langle \Phi(x) | U^\dagger(\theta) M U(\theta) | \Phi(x) \rangle$.
4. **Gradiente Quântico:** Calculado analiticamente via a **Parameter Shift Rule**:
$$\frac{\partial f}{\partial \theta_i} = \frac{f(\theta_i + \pi/2) - f(\theta_i - \pi/2)}{2}$$
