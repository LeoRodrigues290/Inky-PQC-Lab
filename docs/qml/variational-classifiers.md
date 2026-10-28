# Classificadores Quânticos Variacionais (VQC)

Modelos quânticos de classificação em espaços de Hilbert de alta dimensão.

## Barren Plateaus (Platôs Estéreis)
Um dos principais desafios em QML: à medida que o número de qubits $n$ cresce, a variância do gradiente decresce exponencialmente:
$$\text{Var}[\partial_{\theta} \langle H \rangle] \in \mathcal{O}(2^{-n})$$
Soluções incluem inicialização de identidade, circuitos locais e designs conscientes da simetria.
