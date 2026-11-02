# Ataques de Canal Lateral e Injeção de Falhas em PQC

Mesmo com segurança matemática comprovada, implementações físicas de algoritmos pós-quânticos podem vazar segredos via canais laterais.

## Vetores Críticos
- **Consumo de Energia (DPA/CPA):** Análise diferencial de potência durante a computação da transformada NTT (Number Theoretic Transform).
- **Vazamento por Tempo (Timing Attacks):** Operações que não executam em tempo constante (ex: rejeição de amostragem gaussiana no Falcon).
- **Ataques de Falha Induzida:** Corrupção de estados intermediários para forçar o decapsulamento incorreto e inferir coeficientes de polinômios secretos.
