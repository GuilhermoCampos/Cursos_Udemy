import numpy

entradas = numpy.array([1, 7, 5])
pesos = numpy.array([0.8, 0.1, 0])

def soma(ent, pes):
    return ent.dot(pes)

sum = soma(entradas, pesos)

def stepFunction(soma):
    if soma >= 1:
        return 1
    else:
        return 0

res = stepFunction(sum)

print(f'Entrada {entradas}')
print(res)

entradas[0] = -1

sum = soma(entradas, pesos)

res = stepFunction(sum)

print(f'Entrada {entradas}')
print(res)