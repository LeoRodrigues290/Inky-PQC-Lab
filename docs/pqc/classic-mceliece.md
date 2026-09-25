# Classic McEliece (Criptografia Baseada em Códigos)

Proposto por Robert McEliece em 1978, permanece inquebrável há mais de quatro décadas.

## Fundamentação
- Baseado na dificuldade de decodificar um código linear binário aleatório (problema NP-difícil).
- Utiliza códigos de Goppa binários estruturados ocultos por permutações e matrizes não-singulares.

## Trade-off
- **Criptoanálise:** Confiança extrema e imune a ataques quânticos conhecidos.
- **Chave Pública:** Muito grande (~250 KB a 1 MB), tornando-o ideal para armazenamento permanente e menos prático para protocolos web de baixa latência.
