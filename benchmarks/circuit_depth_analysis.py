"""
Analisador de profundidade e contagem de portas de circuitos quânticos.
"""
from qiskit import QuantumCircuit

def analyze_circuit(qc: QuantumCircuit):
    print("=== Métricas do Circuito ===")
    print(f"Total de Qubits: {qc.num_qubits}")
    print(f"Profundidade (Depth): {qc.depth()}")
    print(f"Contagem de Operações: {qc.count_ops()}")

if __name__ == "__main__":
    qc = QuantumCircuit(5)
    qc.h(range(5))
    for i in range(4):
        qc.cx(i, i + 1)
    analyze_circuit(qc)
