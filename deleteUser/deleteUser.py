import json


def deleteUser(userName, userlist):
    for i in range(len(userlist)):
        if usersList[i]['nome'] == userName:
            usersList.pop(i)
            print("Usuario deletado com sucesso!")

def updateJson(directory, list):
    with open(directory, "w") as updateFile:
        json.dump(list, updateFile, indent=4)

if __name__ == "__main__":

    # Diretório do arquivo json
    jsonDirectory = "D:\\UnB\\Orientação a Objetos - Python - Monitoria\\1 - Orientação a Objetos - Como usar JSON em Pyhton\\aula-PythonJson\\deleteUser\\database\\users.json"

    # Converte o arquivo json para uma lista de Dicionários
    with open(jsonDirectory) as fp:
        usersList = json.load(fp)

    # Printa os Usuarios cadastrados
    print("Usuarios Cadastrados:")
    for user in usersList:  
        print(f"{user}\n")

    nameForDeletion = "Maria"

    # função que deleta o usuario
    deleteUser(nameForDeletion, usersList)

    # função que reescreve o json
    updateJson(jsonDirectory, usersList)
