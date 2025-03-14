def dividir_em_linhas(texto, chave):

    texto = texto.replace('\n', '')
# Remove todas as quebras de linha (\n) do texto.
    texto_completo = texto.ljust((len(texto) + chave - 1) // chave * chave)
# Completa o texto com espaços à direita para que seu comprimento seja um múltiplo da chave.
# Exemplo: Se o texto tem 33 caracteres e a chave é 5, o comprimento necessário será 35 (o menor múltiplo de 5 maior ou igual a 33).
    linhas = [texto_completo[i:i + chave] for i in range(0, len(texto_completo), chave)]
#Divide o texto em linhas com o valor de "chave" em caracteres, por linha.
    return linhas

def encriptar(texto, chave, coluna_inicial):

    linhas = dividir_em_linhas(texto, chave)
# Usa a função dividir_em_linhas
    texto_encriptado = ''
    for coluna in range(coluna_inicial - 1, coluna_inicial - 1 + chave): # É o Ciclo que vai correr inicialmente do valor da chave, até, ao valor da chave(coluna inicial) mais o valor da chave novamente, sendo que a coluna inicial é o valor da chave.
        coluna = coluna % chave # Garante que o valor da coluna esteja sempre dentro do intervalo [0, chave - 1], ou seja o valor da chave.
        for linha in linhas: # Faz um ciclo no texto dividido
            if coluna < len(linha): # Garante que a coluna existe na linha
                texto_encriptado += linha[coluna] # Adiciona o caractere da coluna atual ao texto encriptado.

    return texto_encriptado

def desencriptar(texto_encriptado, chave, coluna_inicial):
# Calcula o número de linhas necessárias para reconstruir a matriz de caracteres.
    num_linhas = (len(texto_encriptado) + chave - 1) // chave
# Cria uma lista_matriz (lista de listas) com num_linhas linhas e chave colunas.
    lista_matriz = [[''] * chave for _ in range(num_linhas)]
# Ciclo sobre as colunas da matriz
    lista_indexante = 0
    for coluna in range(chave):
        coluna_ajustada = (coluna_inicial - 1 + coluna) % chave  # Ajusta a posição correta
        for linha in range(num_linhas): # Ciclo das Linhas no Total de Linhas
            if lista_indexante < len(texto_encriptado): # Garante que ainda há caracteres para processar.
                lista_matriz[linha][coluna_ajustada] = texto_encriptado[lista_indexante] # Preenche a matriz com os caracteres do texto encriptado.
                lista_indexante += 1 # Converte a matriz de volta para uma string, lendo as linhas em ordem.

    texto_original = ''.join(''.join(linha) for linha in lista_matriz)

    return texto_original.rstrip()