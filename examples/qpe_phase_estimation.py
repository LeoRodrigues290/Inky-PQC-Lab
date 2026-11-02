"""
Implementação de Quantum Phase Estimation para a porta T (fase theta = 1/8).
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator

def run_qpe_example():
    qc = QuantumCircuit(4, 3)
    # Inicializa estado |1> no qubit alvo
    qc.x(3)
    
    for q in range(3):
        qc.h(q)
        
    # Porta T controlada com potências de 2
    # T = P(pi/4) -> theta = 1/8 = 0.001 binário
    qc.cp(np.pi / 4 * 1, 0, 3)
    qc.cp(np.pi / 4 * 2, 1, 3)
    qc.cp(np.pi / 4 * 4, 2, 3)
    
    # QFT Inversa
    qc.append(QFT(3, inverse=True), range(3))
    qc.measure(range(3), range(3))
    
    counts = AerSimulator().run(qc, shots=1000).result().get_counts()
    return counts

if __name__ == "__main__":
    print("Resultado QPE:", run_qpe_example())
