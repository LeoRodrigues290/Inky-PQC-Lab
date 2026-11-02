"""
Implementação do algoritmo de Grover para 3 qubits com Qiskit.
Busca o estado marcado |111>.
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def create_grover_circuit():
    qc = QuantumCircuit(3, 3)
    # Inicialização uniforme
    qc.h(range(3))
    
    # Oráculo de fase para |111>
    qc.h(2)
    qc.ccx(0, 1, 2)
    qc.h(2)
    
    # Difusor de Grover
    qc.h(range(3))
    qc.x(range(3))
    qc.h(2)
    qc.ccx(0, 1, 2)
    qc.h(2)
    qc.x(range(3))
    qc.h(range(3))
    
    qc.measure(range(3), range(3))
    return qc

if __name__ == "__main__":
    circuit = create_grover_circuit()
    backend = AerSimulator()
    result = backend.run(circuit, shots=1024).result()
    print("Distribuição de Medição Grover:", result.get_counts())
