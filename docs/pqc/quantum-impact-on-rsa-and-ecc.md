# Impacto Quântico na Criptografia Clássica

Matriz detalhada do impacto de computadores quânticos tolerantes a falhas (CRQC - Cryptanalytically Relevant Quantum Computer):

| Algoritmo Clássico | Uso Primário | Ameaça Quântica | Status Pós-Quântico | Substitutos Recomendados |
|---|---|---|---|---|
| **RSA-2048 / RSA-4096** | Assinatura / Troca de Chaves | Algoritmo de Shor | ❌ **Totalmente Quebrado** | ML-KEM, ML-DSA |
| **ECDSA / Ed25519** | Assinaturas Digitais | Algoritmo de Shor | ❌ **Totalmente Quebrado** | ML-DSA, SLH-DSA, Falcon |
| **ECDH / X25519** | Estabelecimento de Sessão TLS | Algoritmo de Shor | ❌ **Totalmente Quebrado** | ML-KEM-768 |
| **AES-128** | Cifração Simétrica | Algoritmo de Grover | ⚠️ Reduzido para 64 bits | Migrar para AES-256 |
| **AES-256** | Cifração Simétrica | Algoritmo de Grover | ✅ Seguro (128 bits residuais) | Manter |
| **SHA-256 / SHA-3** | Hashing | Ataque BHT / Grover | ✅ Seguro ($2^{128}$ colisões) | SHA-384 / SHA-512 |
