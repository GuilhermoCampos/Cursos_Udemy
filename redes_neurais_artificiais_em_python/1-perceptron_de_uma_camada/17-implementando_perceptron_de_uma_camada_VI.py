import numpy as np

# entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) # AND
# saidas = np.array([0, 0, 0, 1])
entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) # OR
saidas = np.array([0, 1, 1, 1])
# entradas = np.array([[0,0], [0,1], [1,0], [1,1]]) #XOR
# saidas = np.array([0, 1, 1, 0])
pesos = np.array([0.0 , 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if(soma >= 1):
        return 1
    else:
        return 0

def calculaSaida(registro):
    soma  = registro.dot(pesos)
    return stepFunction(soma)

def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = saidas[i] - saidaCalculada
            erroTotal += erro
            if (erro != 0):
                for j in range(len(pesos)):
                    pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                    print(f"Peso Atualizado: {str(pesos[j])}")
        print(f"Total de erros: {erroTotal}")

treinar()

print("Rede Neural Treinada")

print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))