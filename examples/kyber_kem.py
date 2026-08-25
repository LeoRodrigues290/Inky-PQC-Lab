# Kyber KEM Example
import oqs

kem = oqs.KeyEncapsulation('Kyber512')
public_key = kem.generate_keypair()
ciphertext, shared_secret = kem.encap_secret(public_key)
print('KEM OK')
