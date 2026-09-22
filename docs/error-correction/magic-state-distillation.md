# Destilação de Estados Mágicos (Magic State Distillation)

O Teorema de Eastin-Knill proíbe que qualquer código quântico implemente um conjunto universal de portas lógicas usando unicamente portas transversais.

## Superando Eastin-Knill com Estados Mágicos
- Portas de Clifford (H, S, CNOT) são transversais em muitos códigos, mas não são universais.
- A adição da porta $T = \text{diag}(1, e^{i\pi/4})$ fornece universalidade.
- A porta $T$ lógica é injetada através de teletransporte quântico consumindo um **estado mágico**:
$$|T\rangle = \cos(\pi/8)|0\rangle + \sin(\pi/8)|1\rangle$$
- A destilação purifica estados mágicos ruidosos usando rotinas de correção de erros.
