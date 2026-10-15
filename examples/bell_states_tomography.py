"""
Gerador dos 4 estados de Bell maximamente emaranhados.
"""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def create_bell(state_name="phi_plus"):
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    if state_name == "phi_minus":
        qc.z(0)
    elif state_name == "psi_plus":
        qc.x(1)
    elif state_name == "psi_minus":
        qc.z(0)
        qc.x(1)
    return Statevector.from_instruction(qc)

if __name__ == "__main__":
    for name in ["phi_plus", "phi_minus", "psi_plus", "psi_minus"]:
        vec = create_bell(name)
        print(f"Estado {name}:\n{vec}\n")
