'''
Função:
T(f,c_i,d_i) - S(f,c_i,d_i)) | > \frac{\epsilon}{2^{i+1}}

Relação exercício 8(b):
Função Exercício 10:
S(f,c,d) = \frac{4T_1(f,c,d) - T_0(f,c,d)}{3}
Nas fórmulas: T_0(f,c,d) = T(f,c,d)$ e $T_1(f,c,d), (ou seja, Ti(f,c,d,1)).
Função: T_1(f,c,d) = T(f, c, \frac{c+d}{2}) + T(f, \frac{c+d}{2}, d).

A Função `integracao_dinamica` implementa essa abordagem

A condição de subdivisão é:
T(f,c_i,d_i) - S(f,c_i,d_i)) | > \frac{\epsilon}{2^{i+1}}$
No código fornecido, a função `integracao_dinamica` usa `S(f,c,m)` e `T_val = T(f,c,d)`.
'''

import math

def abs(x):
    if x > 0:
        return (x)
    else:
        return (-x)

a = 3
b = 12

f1 = lambda x: math.log(1 + x) * math.sin(0.1 * x) / (x * (1 + x)) * math.exp(x)
f2 = lambda x: math.sin(x) * math.exp(x / 10) * math.cos(1 / x)
f3 = lambda x: x ** 2 + 2
f4 = lambda x: math.log(1 + x) * math.sin(0.1 * x) / (x * (1 + x)) * math.exp(x)
f5 = lambda x: math.exp(2 ** x) - x ** 10


contador_f_x = 0
cache_f_x = {}

def f_monitorizada(f_original, x):
    global contador_f_x
    global cache_f_x

    if x not in cache_f_x:
        contador_f_x += 1
        valor = f_original(x)
        cache_f_x[x] = valor
    return cache_f_x[x]

def T_adapt(f, c, d):
    if c > d or c < a or d > b:
        return (None)
    return ((d - c) * (f(c) + f(d)) / 2)

def T_m(f, c, d):
    m = (c + d) / 2
    return T_m(f, c, m) + T_m(f, m, d)

def S_adapt(f, c, d):
    return ((d - c) / 6 * (f(c) + 4 * f((c + d) / 2) + f(d)))


def integracao_adaptativa(f_original, c, d, epsilon, nivel_atual=0):
    f = lambda x: f_monitorizada(f_original, x)

    if c > d or c < a or d > b:
        print("Limites são ilegais!")
        return None

    T_val = T_adapt(f, c, d)
    S_val = S_adapt(f, c, d) # Usa f(c), f(d), f((c+d)/2)

    if abs(T_val - S_val) > epsilon / (2**nivel_atual):
        m = (c + d) / 2
        return (integracao_adaptativa(f_original, c, m, epsilon, nivel_atual + 1) +
                integracao_adaptativa(f_original, m, d, epsilon, nivel_atual + 1))
    else:
        return S_val

#'''
# TEST 10:
f= input("A função: ")
f_callable = eval(f)
c= float(input("Limite esquerda (c): "))
d= float(input("Limite direita (d): "))
epsilon = float(input("Precição (epsilon): "))

contador_f_x = 0
cache_f_x = {}

resultado_adaptativo = integracao_adaptativa(f_callable, c, d, epsilon)

if resultado_adaptativo is not None:
    print(f"Integral Adaptativa para {f} no [{c},{d}] com epsilon {epsilon}:")
    print(f"Resultado = {resultado_adaptativo:}")
    print(f"Número total de chamadas únicas a f: {contador_f_x}")
else:
    print("O cálculo da integral falhou devido a limites ilegais.")
#'''
