# Dilithium Signature Example
import oqs

sig = oqs.Signature('Dilithium2')
public_key = sig.generate_keypair()
message = b'Hello PQC'
signature = sig.sign(message)
print('Sig OK:', sig.verify(message, signature, public_key))
