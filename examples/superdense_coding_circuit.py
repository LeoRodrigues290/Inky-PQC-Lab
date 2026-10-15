"""
Transmissão de dois bits clássicos em um único qubit via Superdense Coding.
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def send_dense(b1=1, b2=0):
    qc = QuantumCircuit(2, 2)
    # Entrelaçamento
    qc.h(0)
    qc.cx(0, 1)
    
    # Codificação de Alice
    if b2 == 1:
        qc.x(0)
    if b1 == 1:
        qc.z(0)
        
    # Decodificação de Bob
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    
    counts = AerSimulator().run(qc, shots=10).result().get_counts()
    return list(counts.keys())[0]

if __name__ == "__main__":
    bits = (1, 1)
    received = send_dense(*bits)
    print(f"Bits enviados: {bits} -> Recebidos: {received}")
