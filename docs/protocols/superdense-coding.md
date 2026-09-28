# Superdense Coding (Codificação Superdensa)

Permite enviar **dois bits clássicos** de informação física através da transmissão de **um único qubit**.

## Mecanismo
1. Alice e Bob compartilham o estado emaranhado $|\Phi^+angle = rac{1}{\sqrt{2}}(|00angle + |11angle)$.
2. Para enviar $00$, Alice aplica $I$.
3. Para enviar $01$, Alice aplica $X$ ($|\Psi^+angle$).
4. Para enviar $10$, Alice aplica $Z$ ($|\Phi^-angle$).
5. Para enviar $11$, Alice aplica $i Y = Z X$ ($|\Psi^-angle$).
6. Alice envia seu qubit para Bob, que realiza a medição na base de Bell e decodifica ambos os bits com 100% de precisão.
