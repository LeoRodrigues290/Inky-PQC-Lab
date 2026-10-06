"""
Demonstração completa do algoritmo de Deutsch-Jozsa em n qubits.
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def build_deutsch_jozsa(n, oracle_type="balanced"):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    
    if oracle_type == "balanced":
        for i in range(n):
            qc.cx(i, n)
            
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc

if __name__ == "__main__":
    circ = build_deutsch_jozsa(3, "balanced")
    counts = AerSimulator().run(circ, shots=100).result().get_counts()
    print("Resultado Deutsch-Jozsa:", counts)
