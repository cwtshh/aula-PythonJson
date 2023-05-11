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

    jsonDirectory = "D:\\UnB\\Orientação a Objetos - Python - Monitoria\\1 - Orientação a Objetos - Como usar JSON em Pyhton\\aula-PythonJson\\deleteUser\\database\\users.json"

    with open(jsonDirectory) as fp:
        usersList = json.load(fp)

    print("Usuarios Cadastrados:")
    for user in usersList:  
        print(f"{user}\n")

    nameForDeletion = "Maria"

    deleteUser(nameForDeletion, usersList)

    updateJson(jsonDirectory, usersList)
