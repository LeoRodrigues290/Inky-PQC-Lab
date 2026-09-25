# NIST FIPS 205: SLH-DSA (Stateless Hash-Based Signatures)

Padronizado pelo NIST em agosto de 2024 (baseado no algoritmo SPHINCS+).

## Segurança Conservadora
- Não depende de problemas de reticulados (lattices).
- Confia exclusivamente nas propriedades de segurança de funções hash criptográficas (resistência a colisões e segunda pré-imagem).
- Atua como uma salvaguarda caso avanços na álgebra de reticulados comprometam o ML-DSA.

## Árvore de Hashes
Combina árvores de Merkle de múltiplos níveis (hiper-árvores) e assinaturas de uso único FORS (Forest of Random Subsets).
