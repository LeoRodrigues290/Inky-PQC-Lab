"""
Simulação de VQE minimalista para modelo de molécula de dois níveis.
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

H = SparsePauliOp.from_list([("ZZ", -1.05), ("XX", 0.39), ("ZI", 0.52), ("IZ", 0.52)])

def ansatz(theta):
    qc = QuantumCircuit(2)
    qc.ry(theta[0], 0)
    qc.ry(theta[1], 1)
    qc.cx(0, 1)
    qc.ry(theta[2], 0)
    qc.ry(theta[3], 1)
    return qc

if __name__ == "__main__":
    estimator = StatevectorEstimator()
    params = np.array([0.1, 0.2, 0.3, 0.4])
    circ = ansatz(params)
    pub = (circ, H)
    job = estimator.run([pub])
    energy = job.result()[0].data.evs
    print(f"Energia VQE estimada: {energy:.4f} Hartree")
