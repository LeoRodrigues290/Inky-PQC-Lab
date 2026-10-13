"""
QAOA de 1 camada para o problema Max-Cut em grafo de 4 vértices.
"""
import numpy as np
from qiskit import QuantumCircuit

def qaoa_maxcut_circuit(gamma=0.5, beta=0.5):
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    qc = QuantumCircuit(4)
    qc.h(range(4))
    
    # Camada de Custo
    for u, v in edges:
        qc.cx(u, v)
        qc.rz(2 * gamma, v)
        qc.cx(u, v)
        
    # Camada de Mistura
    for i in range(4):
        qc.rx(2 * beta, i)
        
    return qc

if __name__ == "__main__":
    qc = qaoa_maxcut_circuit()
    print("Circuito QAOA Max-Cut gerado com", qc.num_qubits, "qubits")
