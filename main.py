# Importando OS só para poder usar o cls
import os

# Input para o tamanho da matriz
m = int(input("Insira o numero de linhas: "))
n = int(input("Insira o numero de colunas: "))

# Variáveis de posição na matriz
i = 1
j = 1

# Variável de controle
x = 0

# Array/List para recebimento das características da matriz e seus valores
A = []

# Estrutura de repetição para aplicação das características de linhas
while len(A) < m and x < n:
    # Cria linhas
    A.append([])
    # Insere coluna em cada linha e o posição na matriz
    j = 1
    while len(A[x]) != n:
        A[x].append(f"a{i}{j}")
        j += 1
    x += 1
    i += 1

os.system('cls') # Limpa o console para não deixar que as informações preenchidas continuem na tela
print(f"\nNúmero de linhas: " + str(len(A))) # Mostra no console o número de linhas solicitadas
print("Número de colunas: " + str(len(A[0]))) # Mostra no console o número de colunas solicitadas

print(f"\nA matriz solicitada é igual:\n--------------------------") # Linha dL

# Usando o for só para dar um estílo à matriz, deixando linha abaixo de linha
for ax in A:
    print(f"     {ax}")

print(f"--------------------------\n")# Linha dL

texto = "Sua matriz é uma matriz "

print(f"{texto}quadrada\n") if n == m else ""
print(f"{texto}linha\n") if 1 == m else ""
print(f"{texto}coluna\n") if 1 == n else ""

# Pergunta se quer manipular valores da matriz
aij = input("Deseja manipular os valores da matriz? y/N: ")

# Variáveis de segurança
condicao1 = 0
condicao2 = 0
condicao3 = 0

if aij == "y":
    # Relação i < j
    os.system('cls')
    condicao1 = int(input('Se i < j então: '))

    # Relação i = j
    os.system('cls')
    condicao2 = int(input('Se i = j então: '))
    
    # Relação i > j
    os.system('cls')
    condicao3 = int(input('Se i > j então: '))

# Reinicia Variáveis, crio uma nova variável para a matriz modificada.
i = 1
j = 1
x = 0
B = []

# Só executa se a resposta para desejo de modificação for yes
if aij == "y":
    # Reaproveito o código
    while len(B) < m and x < n:
        # Cria linhas
        B.append([])
        # Insere coluna em cada linha e o posição na matriz
        j = 1
        while len(B[x]) != n:
        
            if condicao1:
                if i < j:
                    B[x].append(f"{condicao1}")

            if condicao2:
                if i == j:
                    B[x].append(f"{condicao2}")

            if condicao3:
                if i > j:
                    B[x].append(f"{condicao3}")

            j += 1
        x += 1
        i += 1

    # Reaproveitando o código novamente - só para dar um estílo à matriz, deixando linha abaixo de linha
    os.system('cls')
    print(f"\nA matriz modificada é igual:\n--------------------------") # Linha dL
    if aij == "y":
        for bx in B:
            print(f"     {bx}")

        print(f"--------------------------\n")# Linha dL
