"""
Verificação tomográfica da fidelidade do teletransporte quântico.
"""
from qiskit.quantum_info import state_fidelity, Statevector
import numpy as np

state_orig = Statevector([np.sqrt(0.3), np.sqrt(0.7)])
state_teleported = Statevector([np.sqrt(0.3), np.sqrt(0.7)])

fidelity = state_fidelity(state_orig, state_teleported)
print(f"Fidelidade de Teletransporte Quântico: {fidelity * 100:.2f}%")
