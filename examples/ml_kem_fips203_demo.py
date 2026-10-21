"""
Simulação didática dos princípios matemáticos do ML-KEM (Module-LWE).
"""
import numpy as np

def toy_lwe_keygen(n=256, q=3329):
    # Polinômios simulados com coeficientes em Z_q
    a = np.random.randint(0, q, size=n)
    s = np.random.choice([-1, 0, 1], size=n)
    e = np.random.choice([-1, 0, 1], size=n)
    t = (np.convolve(a, s, mode='same') + e) % q
    return (a, t), s

if __name__ == "__main__":
    pk, sk = toy_lwe_keygen()
    print("Chave Pública LWE gerada com dimensão", len(pk[0]))
