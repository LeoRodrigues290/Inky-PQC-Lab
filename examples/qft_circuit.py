"""
Implementação manual da Transformada Quântica de Fourier em 4 qubits.
"""
import numpy as np
from qiskit import QuantumCircuit

def build_custom_qft(n=4):
    qc = QuantumCircuit(n)
    for j in range(n):
        qc.h(j)
        for k in range(j + 1, n):
            angle = np.pi / (2 ** (k - j))
            qc.cp(angle, k, j)
            
    # Inversão de ordem
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
        
    return qc

if __name__ == "__main__":
    qft_circ = build_custom_qft(4)
    print("QFT 4-qubits construída com profundidade:", qft_circ.depth())
