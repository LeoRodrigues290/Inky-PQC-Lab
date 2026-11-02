"""
Harness de benchmark comparativo de performance para algoritmos criptográficos.
"""
import time
import hashlib

def benchmark_hashing(iterations=50000):
    start = time.perf_counter()
    data = b"benchmark data string"
    for _ in range(iterations):
        data = hashlib.sha3_256(data).digest()
    elapsed = time.perf_counter() - start
    print(f"SHA3-256 Benchmark ({iterations} ops): {elapsed:.4f}s ({iterations/elapsed:.0f} ops/sec)")

if __name__ == "__main__":
    benchmark_hashing()
