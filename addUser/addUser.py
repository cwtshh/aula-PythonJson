import json

from model import User

if __name__ == "__main__":

    jsonDirectory = "D:\\UnB\\Orientação a Objetos - Python - Monitoria\\1 - Orientação a Objetos - Como usar JSON em Pyhton\\aula-PythonJson\\addUser\\database\\users.json"

    usersList = []

    with open(jsonDirectory) as fp:
        usersList = json.load(fp)


    print(usersList)
    print(type(usersList))

    newUser = User("Pedro", 5, "88755348590", "Asa Sul", "1234")
    convertUser = vars(newUser)
    usersList.append(convertUser)

    for user in usersList:
        print(f'{user}\n')

    with open(jsonDirectory, "w") as updateFile:
        json.dump(usersList, updateFile, indent=4)

    

