"""
Algoritmo de Bernstein-Vazirani para descobrir string binária s em 1 consulta.
"""
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def solve_bv(secret_s="1011"):
    n = len(secret_s)
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    
    # Oráculo
    for idx, bit in enumerate(reversed(secret_s)):
        if bit == '1':
            qc.cx(idx, n)
            
    qc.h(range(n))
    qc.measure(range(n), range(n))
    
    result = AerSimulator().run(qc, shots=1).result()
    return list(result.get_counts().keys())[0]

if __name__ == "__main__":
    s = "1101"
    discovered = solve_bv(s)
    print(f"Segredo original: {s} | Descoberto: {discovered}")
