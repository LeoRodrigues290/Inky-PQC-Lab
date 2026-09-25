# FALCON (Fast-Fourier Lattice-based Compact Signatures)

Algoritmo pós-quântico selecionado pelo NIST para padronização como FN-DSA.

## Destaques
- **Tamanho Ultracompacto:** Menor tamanho combinado de chave pública + assinatura entre os esquemas baseados em reticulados.
- **Trapdoor Gentry-Peikert-Vaikuntanathan (GPV):** Amostragem de Fourier Rápida (Fast Fourier Sampling) sobre reticulados NTRU.
- **Desafio de Implementação:** Requer aritmética de ponto flutuante com precisão estrita em tempo constante para evitar ataques de canal lateral (side-channel).
