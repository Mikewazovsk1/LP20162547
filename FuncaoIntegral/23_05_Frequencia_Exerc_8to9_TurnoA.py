# 8º Exercício

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

def T_monitorizado(f_original, c, d):
    if c > d or c < a or d > b:
        return (None)
    return ((d - c) * (f_monitorizada(f_original, c) + f_monitorizada(f_original, d)) / 2)

def Tn_monitorizado(f_original, c, d, n):
    soma = 0
    unidade = (d - c) / n
    for i in range(0, n):
        soma = soma + T_monitorizado(f_original, c + i * unidade, c + (i + 1) * unidade)
    return (soma)

def S_monitorizado(f_original, c, d):
    return ((d - c) / 6 * (f_monitorizada(f_original, c) + 4 * f_monitorizada(f_original, (c + d) / 2) + f_monitorizada(f_original, d)))

'''
# TEST 8:
f = input("A função: ")
f_callable = eval(f)
c = float(input("Limite esquerda: "))
d = float(input("Limite direita: "))
n = int(input("Nº de intervalos inicial (N): "))

# Intervalos n
contador_f_x = 0
cache_f_x = {}
res_N = Tn_monitorizado(f_callable, c, d, n)
chamadas_N = contador_f_x

# Intervalos 2n
chamadas_antes_2N = contador_f_x
res_2N = Tn_monitorizado(f_callable, c, d, 2 * n)
novas_chamadas_2N = contador_f_x - chamadas_antes_2N

print(f"Tn para N intervalos = {res_N}, (Chamadas de f: {chamadas_N})")
print(f"Tn para 2N intervalos = {res_2N} (Novas chamadas de f: {novas_chamadas_2N})")
'''

'''
Reutilização de Tn para T2n
Quando calculamos a integral usando a regra dos trapézios com n subintervalos (Tn), avaliamos a função f nas fronteiras desses n subintervalos. Isso significa que obtemos os valores de f no ponto inicial do intervalo principal, no ponto final, e em todos os pontos intermédios.
Ao calcular T2n, estamos a dobrar o número de subintervalos, o que significa que cada um dos subintervalos originais de Tn é agora dividido em dois. Os pontos onde f foi avaliada para Tn ainda são necessários e usados em T2n. A única coisa que T2n adiciona são os pontos médios de cada um dos n subintervalos originais.
Assim, para ir de Tn para T2n, em vez de reavaliar f em todos os 2n+1 pontos necessários para T2n (o que seria o dobro das avaliações de Tn mais um), nós só precisamos avaliar f nos n novos pontos médios. Os valores de f nas fronteiras dos subintervalos originais (que já estavam calculados em Tn) são simplesmente reutilizados. Isso reduz significativamente o número total de vezes que a função f precisa ser chamada.
Otimização de Sn para S2n
A mesma otimização é perfeitamente possível na transição de Sn para S2n.
A regra de Simpson para n subintervalos (Sn) avalia a função f nas fronteiras de cada subintervalo e no seu ponto médio. Ao passar para S2n, cada um desses subintervalos é dividido em dois. Os pontos que foram usados em Sn (fronteiras e pontos médios dos intervalos originais) são reutilizados. Os únicos pontos novos onde f precisa ser avaliada são os novos pontos médios que surgem da subdivisão.
Tal como na regra dos trapézios, você aproveita os cálculos de f já feitos, evitando redundância e economizando tempo computacional.
'''

# 9º Exercício

contador_f_x = 0
cache_f_x = {}

def integracao_dinamica(f, c, d, epsilon, nivel_atual=0, nivel_maximo=30):
    if nivel_atual >= nivel_maximo:
        return S(f, c, d)

    mid = (c + d) / 2
    T_val = T(f, c, d)
    S_val_left_half = S(f, c, mid)

    if abs(T_val - S_val_left_half) > epsilon / (2 ** (nivel_atual + 1)):
        return (integracao_dinamica(f, c, mid, epsilon / 2, nivel_atual + 1, nivel_maximo) +
                integracao_dinamica(f, mid, d, epsilon / 2, nivel_atual + 1, nivel_maximo))
    else:
        return S(f, c, d)

'''
# TEST 9:

f = input("A função: ")
f_9 = eval(f)
c = float(input("Limite esquerda: "))
d = float(input("Limite direita: "))
epsilon_9 = float(input("Precisão (epsilon): "))

if c > d or c < a or d > b:
    print("Limites são ilegais!")
else:
    contador_f_x = 0
    cache_f_x = {}

    resultado_dinamico = integracao_dinamica(lambda x: f_monitorizada(f_9, x), c, d, epsilon_9)

    print(f"Integracao Dinamica({f_9},{c},{d},{epsilon_9})={resultado_dinamico:}")
    print(f"Chamadas Únicas a f: {contador_f_x})")
    print(f"T({f_9},{c},{d})={T(f_9, c, d):}")
    print(f"S({f_9},{c},{d})={S(f_9, c, d):}")
'''