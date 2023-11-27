import numpy as np

def eliminacao_de_gauss(matriz_aumentada):
    # Obtém o número de linhas e colunas da matriz
    linhas, colunas = matriz_aumentada.shape

    # Aplica a eliminação de Gauss
    for i in range(min(linhas, colunas - 1)):
        # Faz o pivoteamento parcial
        pivo = i
        for j in range(i + 1, linhas):
            if abs(matriz_aumentada[j, i]) > abs(matriz_aumentada[pivo, i]):
                pivo = j
        matriz_aumentada[[i, pivo]] = matriz_aumentada[[pivo, i]]

        # Normaliza a linha atual
        pivot_value = matriz_aumentada[i, i]
        matriz_aumentada[i, :] /= pivot_value

        # Eliminação para frente
        for j in range(i + 1, linhas):
            factor = matriz_aumentada[j, i]
            matriz_aumentada[j, :] -= factor * matriz_aumentada[i, :]

    # Substituição para trás
    solucao = np.zeros(linhas)
    for i in range(linhas - 1, -1, -1):
        solucao[i] = matriz_aumentada[i, -1] - np.dot(matriz_aumentada[i, i + 1:-1], solucao[i + 1:])

    return solucao  # Adicionando esta linha para retornar a solução
