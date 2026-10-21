"""
Gerador Quântico de Números Aleatórios (QRNG) baseado em colapso de superposição.
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def generate_quantum_random_bytes(num_bytes=8):
    qc = QuantumCircuit(8, 8)
    qc.h(range(8))
    qc.measure(range(8), range(8))
    
    sim = AerSimulator()
    result = sim.run(qc, shots=num_bytes, memory=True).result()
    random_bytes = bytearray([int(b, 2) for b in result.get_memory()])
    return bytes(random_bytes)

if __name__ == "__main__":
    rand = generate_quantum_random_bytes(16)
    print("Bytes Quânticos Gerados:", rand.hex())
