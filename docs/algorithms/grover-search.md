# Algoritmo de Busca de Grover

O Algoritmo de Grover (1996) fornece uma aceleração quadrática para busca em bancos de dados desestruturados ou inversão de funções unidirecionais.

## Speedup Quadrático
- **Clássico:** $\mathcal{O}(N)$ avaliações.
- **Grover:** $\mathcal{O}(\sqrt{N})$ iterações do operador de Grover.

## Operador de Grover $\mathcal{G}$
$$\mathcal{G} = -(I - 2|s\rangle\langle s|) O_f = (2|s\rangle\langle s| - I) O_f$$

Onde:
- $O_f |x\rangle = (-1)^{f(x)} |x\rangle$ é o Oráculo de Fase.
- $D = 2|s\rangle\langle s| - I$ é o Difusor (Inversão em torno da média).
- $|s\rangle = \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle$ é o estado uniforme inicial.

## Impacto na Criptografia Simétrica
Grover reduz a segurança efetiva de chaves AES:
- AES-128 $\to$ 64 bits de segurança quântica.
- AES-256 $\to$ 128 bits de segurança quântica (recomendado pós-quântico).
