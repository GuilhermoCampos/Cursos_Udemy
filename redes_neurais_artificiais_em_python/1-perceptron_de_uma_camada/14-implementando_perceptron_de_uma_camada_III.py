import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0 , 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if(soma >= 1):
        return True
    else:
        return False

def calculaSaida(registro):
    soma  = registro.dot(pesos)
    return stepFunction(soma)

def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print(f"Peso Atualizado: {str(pesos[j])}")
        print(f"Total de erros: {erroTotal}")

treinar()

