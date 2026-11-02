# BB84 Protocol Simulation
import random

def bb84_key_gen(n=100):
    alice_bits = [random.randint(0,1) for _ in range(n)]
    alice_bases = [random.randint(0,1) for _ in range(n)]
    bob_bases = [random.randint(0,1) for _ in range(n)]
    key = [alice_bits[i] for i in range(n) if alice_bases[i] == bob_bases[i]]
    return key

print('Key:', bb84_key_gen(20))
