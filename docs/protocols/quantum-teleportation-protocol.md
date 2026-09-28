# Protocolo de Teletransporte Quântico

O teletransporte quântico transmite o estado quântico de um qubit desconhecido utilizando entrelaçamento prévio e 2 bits clássicos de comunicação.

## Protocolo Bennett et al. (1993)
1. Alice e Bob compartilham um par de Bell $|\Phi^+angle = rac{1}{\sqrt{2}}(|00angle + |11angle)$.
2. Alice possui um qubit desconhecido $|\psiangle = lpha |0angle + eta |1angle$.
3. Alice aplica uma porta CNOT entre $|\psiangle$ e sua metade do par de Bell, seguida de uma porta Hadamard em $|\psiangle$.
4. Alice mede ambos os seus qubits, obtendo 2 bits clássicos ($m_1, m_2$).
5. Bob recebe os 2 bits e aplica correções unitárias: $X^{m_2} Z^{m_1}$.
6. O estado do qubit de Bob é agora exatamente $|\psiangle$!
