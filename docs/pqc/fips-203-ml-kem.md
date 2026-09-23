# NIST FIPS 203: ML-KEM (Module-Lattice KEM)

Padronizado oficialmente pelo NIST em agosto de 2024, baseado no algoritmo CRYSTALS-Kyber.

## Níveis de Segurança
- **ML-KEM-512:** Categoria de segurança NIST 1 (equivalente ao AES-128).
- **ML-KEM-768:** Categoria de segurança NIST 3 (equivalente ao AES-192, recomendado para implantação geral).
- **ML-KEM-1024:** Categoria de segurança NIST 5 (equivalente ao AES-256).

## Fundamento Matemático
Baseado na dureza computacional do problema MLWE (Module Learning With Errors) sobre o anel polinomial $R_q = \mathbb{Z}_q[X]/(X^{256} + 1)$ com $q = 3329$.
