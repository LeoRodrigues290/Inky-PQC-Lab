# Algoritmo de Shor (Fatoração em Tempo Polinomial)

O Algoritmo de Shor, formulado por Peter Shor em 1994, é um dos mais impactantes na computação quântica por quebrar a segurança matemática do RSA e Diffie-Hellman.

## Complexidade
- **Clássico (GNFS - General Number Field Sieve):** Subexponencial $\mathcal{O}(\exp((\sqrt[3]{\frac{64}{9}} + o(1)) (\ln N)^{1/3} (\ln \ln N)^{2/3}))$.
- **Quântico (Shor):** Polinomial $\mathcal{O}((\log N)^2 (\log \log N) (\log \log \log N))$.

## Etapas do Algoritmo
1. **Redução Clássica:** Reduz a fatoração de $N$ à determinação do período $r$ da função $f(x) = a^x \pmod N$.
2. **Subrotina Quântica (Order Finding):**
   - Inicialização em superposição uniforme.
   - Aplicação de exponenciação modular unitária $U_a |x\rangle |0\rangle = |x\rangle |a^x \pmod N\rangle$.
   - Transformada Quântica de Fourier Inversa ($QFT^\dagger$).
   - Medição do primeiro registrador para estimar a fase $s/r$.
3. **Pós-processamento Clássico:**
   - Algoritmo de Frações Contínuas para extrair $r$.
   - Se $r$ for par, calcula $\gcd(a^{r/2} \pm 1, N)$ para encontrar os fatores primos.
