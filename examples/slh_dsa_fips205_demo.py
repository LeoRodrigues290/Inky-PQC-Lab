"""
Simulação didática do mecanismo de assinatura baseado em hashes SLH-DSA (SPHINCS+).
"""
import hashlib

def hash_chain(seed: bytes, steps: int) -> bytes:
    val = seed
    for _ in range(steps):
        val = hashlib.sha256(val).digest()
    return val

if __name__ == "__main__":
    secret = b"minha_chave_privada_wots"
    public_leaf = hash_chain(secret, 16)
    print("Folha pública de cadeia Hash SLH-DSA:", public_leaf.hex()[:32])
