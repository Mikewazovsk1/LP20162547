from Functions import encriptar
from Functions import desencriptar

def main():
    with open('texto.txt', 'r') as file:
        texto = file.read()
# 'r' = read

    chave = 5
    coluna_inicial = 3

    texto_encriptado = encriptar(texto, chave, coluna_inicial)
    with open('texto_encriptado.txt', 'w') as file:
        file.write(texto_encriptado)
# 'w' = write
    texto_desencriptado = desencriptar(texto_encriptado, chave, coluna_inicial)
    with open('texto_desencriptado.txt', 'w') as file:
        file.write(texto_desencriptado)

    print("Encriptação e desencriptação concluídas com sucesso!")

if __name__ == "__main__":
    main()
