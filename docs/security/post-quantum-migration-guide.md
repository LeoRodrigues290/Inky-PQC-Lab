# Guia de Migração para Criptografia Pós-Quântica (Enterprise Blueprint)

Roadmap estratégico para transição criptográfica de organizações para conformidade pós-quântica (NIST / CISA / CNSA 2.0).

## 4 Fases de Migração
1. **Inventário Criptográfico (C-BOM):** Mapear todos os certificados TLS, chaves de assinatura de firmware, algoritmos em banco de dados e APIs legadas.
2. **Avaliação de Risco "Harvest Now, Decrypt Later" (HNDL):** Identificar dados confidenciais com vida útil superior a 10 anos sujeitos a exfiltração imediata.
3. **Adoção Híbrida (Hybrid Transition):** Integrar suítes de cifras híbridas (ex: X25519Kyber768Draft00) em balanceadores de carga e gateways.
4. **Desativação Total de Algoritmos Vulneráveis:** Remover suporte a RSA e ECDSA/ECDH conforme diretrizes regulatórias até 2030.
