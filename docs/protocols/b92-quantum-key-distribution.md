# Protocolo B92 de QKD

Formulado por Charles Bennett em 1992 como uma simplificação minimalista do protocolo BB84.

## Estados Não-Ortogonais
Enquanto o BB84 utiliza 4 estados em 2 bases ortogonais, o B92 utiliza apenas 2 estados não-ortogonais:
- Alice envia $|0angle$ (para representar 0) ou $|+angle$ (para representar 1).
- Bob mede aleatoriamente nas bases $\{|0angle, |1angle\}$ ou $\{|+angle, |-angle\}$.
- O teorema da não-clonagem garante que Eve não pode distinguir estados não-ortogonais sem perturbá-los.
