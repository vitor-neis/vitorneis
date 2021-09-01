
from sys import maxsize
from itertools import permutations
numPosicao = 11 #numero de US, contando com o centro de distibuição possui 11
 
def vacinacaoCuritiba(grafo, s):
 
    posicao = []
    for i in range(numPosicao):
        if i != s:
            posicao.append(i)
 
    menorCaminho = maxsize
    proxPermut=permutations(posicao)
    for i in proxPermut:
 
        custoAtual = 0
 
        k = s
        for j in i:
            custoAtual += grafo[k][j]
            k = j
        custoAtual += grafo[k][s]
 
        menorCaminho = min(menorCaminho, custoAtual)
         
    return menorCaminho
 
if __name__ == "__main__":
 
    # Exemplo de matriz para buscar a melhor rota acessando todas US
    grafo = [[0, 65, 74, 78, 32, 151, 45, 30, 73, 62, 32], [34, 0, 60, 45, 79, 67, 34, 87, 31, 20, 25], [32, 60, 0, 73, 89, 67, 77, 45, 33, 30, 29], [56, 68, 42, 0, 42, 56, 43, 44, 22, 78, 91], [39, 26, 25, 70, 0, 58, 35, 53, 75, 41, 89], [65, 23, 44, 72, 45, 0, 66, 47, 73, 64, 44], [54, 51, 32, 71, 16, 33, 0, 14, 22, 41, 66], [31, 39, 22, 67, 51, 59, 31, 0, 74, 43, 27], [39, 21, 44, 47, 51, 57, 33, 46, 0, 67, 45], [44, 23, 34, 75, 26, 59, 33, 31, 72, 0, 49], [45, 62, 23, 45, 23, 47, 54, 78, 34, 21, 0]]
    s = 0
    print(vacinacaoCuritiba(grafo, s))