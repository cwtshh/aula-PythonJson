import json
from random import choice
import string

from model import User

def generateId():
    numbers = string.digits
    randomNumber = "".join(choice(numbers) for _ in range(4))
    return randomNumber

def createUser(nome, cpf, endereco, senha, usersList):
    id = generateId()
    newUser = User(nome, id, cpf, endereco, senha)
    convertUser = vars(newUser)
    usersList.append(convertUser)

def updateJson(directory, list):
    with open(directory, "w") as updateFile:
        json.dump(list, updateFile, indent=4)

if __name__ == "__main__":

    # Diretório do arquivo
    jsonDirectory = "D:\\UnB\\Orientação a Objetos - Python - Monitoria\\1 - Orientação a Objetos - Como usar JSON em Pyhton\\aula-PythonJson\\addUser\\database\\users.json"

    usersList = []

    # Converte o arquivo json para uma lista de Dicionários
    with open(jsonDirectory) as fp:
        usersList = json.load(fp)

    # printa os usuarios
    print(usersList)
    print(type(usersList))

    # Criando Um novo usuario
    userName = "Maria"
    cpf = "82273394019"
    endereco = "Taguatinga"
    senha = "123456"

    # função que cria um usuario
    createUser(userName, cpf, endereco, senha, usersList)

    # printa os usuarios no console
    for user in usersList:
        print(f'{user}\n')
    
    # Função que reescreve o json
    updateJson(jsonDirectory, usersList)

    

