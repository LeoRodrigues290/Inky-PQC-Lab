# ⚛️ Inky-PQC-Lab

> **Laboratório Avançado de Pesquisa & Desenvolvimento em Computação Quântica, Algoritmos Quânticos e Criptografia Pós-Quântica (PQC)** desenvolvido pela [Inky Digital](https://github.com/Inky-Digital).

---

## 🌟 Visão Geral

O **Inky-PQC-Lab** é um repositório central dedicado ao estudo rigoroso, experimentação e implementação prática de:
1. **Algoritmos Quânticos Universais** (Shor, Grover, QPE, QFT, VQE, QAOA)
2. **Criptografia Pós-Quântica (PQC)** em conformidade com as normas oficiais do **NIST (FIPS 203, 204, 205)**
3. **Arquiteturas de Hardware Quântico** (Supercondutores, Íons Presos, Fotônica, Átomos Neutros)
4. **Correção de Erros Quânticos e Tolerância a Falhas (FTQC)**
5. **Protocolos de Comunicação Quântica** (QKD, Teletransporte, Superdense Coding)

---

## 📚 Estrutura do Laboratório

```
Inky-PQC-Lab/
├── docs/
│   ├── algorithms/        # Shor, Grover, Deutsch-Jozsa, Bernstein-Vazirani, Simon, QPE, QFT, HHL, VQE, QAOA
│   ├── hardware/          # Supercondutores, Íons Presos, Fotônica, Átomos Neutros, Silício
│   ├── error-correction/  # Estabilizadores, Surface Codes, Shor 9-qubit, Steane, Estados Mágicos
│   ├── pqc/               # FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA), Falcon, McEliece
│   ├── protocols/         # Teletransporte, Superdense Coding, E91, B92, QRNG, Computação Cega
│   ├── qml/               # Redes Neurais Quânticas (QNNs), Classificadores Variacionais
│   └── security/          # Guia de Migração Enterprise, Ataques de Canal Lateral
├── examples/              # Scripts executáveis com Qiskit, Qiskit Aer e implementações conceituais
├── benchmarks/            # Harness de benchmarks de circuitos e performance criptográfica
└── requirements.txt       # Dependências de ambiente
```

---

## 🚀 Instalação e Execução

Clone o repositório e instale o ambiente virtual com Qiskit e ferramentas de PQC:

```bash
git clone https://github.com/LeoRodrigues290/Inky-PQC-Lab.git
cd Inky-PQC-Lab
pip install -r requirements.txt
```

### Executando Exemplos

```bash
# Busca de Grover em 3 qubits
python examples/grover_search_simulation.py

# Teletransporte Quântico
python examples/teleportation_circuit.py

# Gerador Quântico de Números Aleatórios (QRNG)
python examples/qrng_entropy_generator.py
```

---

## 🔬 Referências e Padrões Internacionais

- [NIST Post-Quantum Cryptography Standardization](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [IBM Quantum & Qiskit Documentation](https://docs.quantum.ibm.com/)
- [Open Quantum Safe (OQS)](https://openquantumsafe.org/)

---
*Mantido por Léo Rodrigues & Inky Digital.*
