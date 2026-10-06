"""
Simulação do núcleo quântico de busca de períodos do algoritmo de Shor.
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def c_amod15(a, power):
    """Multiplicação modular controlada a^power mod 15."""
    U = QuantumCircuit(4)
    for _ in range(power):
        if a in [2, 13]:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)
        elif a in [7, 8]:
            U.swap(2, 3)
            U.swap(1, 2)
            U.swap(0, 1)
        elif a in [4, 11]:
            U.swap(1, 3)
            U.swap(0, 2)
        if a in [7, 11, 13]:
            for q in range(4):
                U.x(q)
    U = U.to_gate()
    U.name = f"{a}^{power} mod 15"
    return U.control()

if __name__ == "__main__":
    qc = QuantumCircuit(8, 4)
    for q in range(4):
        qc.h(q)
    qc.x(7)
    
    a = 7
    for q in range(4):
        qc.append(c_amod15(a, 2**q), [q] + list(range(4, 8)))
        
    print("Circuito de Oráculo modular de Shor construído com sucesso.")
