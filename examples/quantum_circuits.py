# Quantum Circuit Examples
from qiskit import QuantumCircuit

def ghz_state(n):
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(1, n):
        qc.cx(0, i)
    return qc

print(ghz_state(4))
