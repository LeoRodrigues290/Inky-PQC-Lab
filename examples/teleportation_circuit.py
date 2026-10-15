"""
Circuito completo de Teletransporte Quântico com Qiskit.
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def build_teleportation():
    qc = QuantumCircuit(3, 1)
    # Estado arbitrário a teletransportar no qubit 0
    qc.ry(np.pi / 3, 0)
    
    # Par de Bell entre 1 e 2
    qc.h(1)
    qc.cx(1, 2)
    
    # Medição de Bell por Alice
    qc.cx(0, 1)
    qc.h(0)
    
    # Correções de Bob (portas dinâmicas)
    qc.cx(1, 2)
    qc.cz(0, 2)
    
    # Medição do estado teletransportado
    qc.measure(2, 0)
    return qc

if __name__ == "__main__":
    qc = build_teleportation()
    counts = AerSimulator().run(qc, shots=1000).result().get_counts()
    print("Contagens do teletransporte:", counts)
