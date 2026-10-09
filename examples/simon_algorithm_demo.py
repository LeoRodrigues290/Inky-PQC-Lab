"""
Estrutura do algoritmo de Simon com Qiskit.
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def simon_circuit_demo():
    qc = QuantumCircuit(4, 2)
    qc.h(0)
    qc.h(1)
    
    # Oráculo 1-a-1 ou 2-a-1 com segredo s=11
    qc.cx(0, 2)
    qc.cx(1, 3)
    qc.cx(0, 3)
    qc.cx(1, 2)
    
    qc.h(0)
    qc.h(1)
    qc.measure([0, 1], [0, 1])
    return qc

if __name__ == "__main__":
    qc = simon_circuit_demo()
    counts = AerSimulator().run(qc, shots=500).result().get_counts()
    print("Amostras ortogonais a s no algoritmo de Simon:", counts)
