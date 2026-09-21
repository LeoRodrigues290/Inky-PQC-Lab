# Código de 9 Qubits de Shor

Primeiro código de correção de erros quânticos da história, formulado por Peter Shor em 1995.

## Princípio
Combina a repetição de inversão de bit (bit-flip) e inversão de fase (phase-flip):
$$|0_L\rangle = \frac{1}{2\sqrt{2}} (|000\rangle + |111\rangle)(|000\rangle + |111\rangle)(|000\rangle + |111\rangle)$$
$$|1_L\rangle = \frac{1}{2\sqrt{2}} (|000\rangle - |111\rangle)(|000\rangle - |111\rangle)(|000\rangle - |111\rangle)$$

Pode corrigir simultaneamente qualquer erro arbitrário de um único qubit ($X$, $Z$, ou $Y = i X Z$).
