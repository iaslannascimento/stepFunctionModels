#Autor: Iaslan Nascimento
#Info: Código das fuções de ativação geralmente utilizadas em redes neurais.
#Data 06/06/2019
import numpy as np

#função de ativação
def stepFunction(soma):
    if(soma>=1):
        return 1 
    return 0
print("Função de Ativação:\n " , stepFunction(30))

#função sigimoide 
def sigimoideFunction(soma):
    return 1 /(1+np.exp(-soma))

print("Função Sigmoide:\n", sigimoideFunction(30))

#função de tangente hiperbolica
def tahnFuction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))
print("Função Tangente:\n" ,tahnFuction(30))

#função relu
def reluFunction(soma):
    if soma >=0:
        return soma
    return 0
print("Função Relu:\n" ,reluFunction(30)) 


#função linear 
def lineraFunction(soma):
    return soma
print("Função linear:\n" ,linearFunction(30)) 

#função softmax
def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()
valores = [5.0, 2.0 ,1.3]
print("Função Softmax:\n" ,softmaxFunction(valores)) 
