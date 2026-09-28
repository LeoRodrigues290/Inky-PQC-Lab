# Protocolo Ekert91 (E91 QKD)

Formulado por Artur Ekert em 1991, baseia-se na violação da Desigualdade de Bell (CHSH) para detecção de interceptação de canal (eavesdropping).

## Verificação de Segurança
Se um espião (Eve) tentar interceptar as partículas emaranhadas, o colapso da função de onda destrói o emaranhamento quântico:
$$S = |E(a,b) - E(a,b') + E(a',b) + E(a',b')| \le 2 \quad \text{(Clássico/Local)}$$
Estados quânticos emaranhados atingem até o limite de Tsirelson $S = 2\sqrt{2} \approx 2.828$. Qualquer valor $S < 2\sqrt{2}$ sinaliza ruído ou interceptação.
