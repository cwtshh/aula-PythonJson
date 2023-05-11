import json

def updateUserName(oldName , newName, userList):
    for i in range(len(userList)):
        if usersList[i]['nome'] == oldName:
            usersList[i]['nome'] = newName

def updateUserCpf(name, newCpf, userList):
    for i in range(len(userList)):
        if usersList[i]['nome'] == name:
            usersList[i]['cpf'] = newCpf

def updateUserEndereco(name, newEnd, userList):
    for i in range(len(userList)):
        if usersList[i]['nome'] == name:
            usersList[i]['endereco'] = newEnd

def updateUserSenha(name, newSenha, userList):
    for i in range(len(usersList)):
        if userList[i]['nome'] == name:
            userList[i]['contaSenha'] = newSenha

    



def updateJson(directory, list):
    with open(directory, "w") as updateFile:
        json.dump(list, updateFile, indent=4)

if __name__ == "__main__":


    # DIRETORIO DO ARQUIVO
    jsonDirectory = "D:\\UnB\\Orientação a Objetos - Python - Monitoria\\1 - Orientação a Objetos - Como usar JSON em Pyhton\\aula-PythonJson\\updateUser\\database\\users.json"

    # ABRINDO O ARQUIVO
    with open(jsonDirectory) as fp:
        usersList = json.load(fp)



    # Printa os usuarios cadastrados no console
    print("Usuarios Cadastrados:")
    for user in usersList:  
        print(f"{user}\n")

    # ATUALIZANDO O NOME
    nameForUpdate = 'Peter'
    newName = "Cleiton"

    # função para atualizar o nome do usuario
    updateUserName(nameForUpdate, newName, usersList)

    # Printa os usuarios no console
    for user in usersList:
        print(f"{user}\n")

    # função que reescreve o Json
    updateJson(jsonDirectory, usersList)




    # ATUALIZANDO O CPF - PASS
    userForUpdate1 = "Gustavo"
    newCpf = "77281193403"

    # função para atualizar o cpf do usuario
    updateUserCpf(userForUpdate1, newCpf, usersList)

    # função que reescreve o json
    updateJson(jsonDirectory, usersList)



    # ATUALIZANDO O ENDEREÇO - PASS
    userForUpdate2 = "Clara"
    newEnd = "Guara"

    # função que atualiza o endereço do usuario
    updateUserEndereco(userForUpdate2, newEnd, usersList)

    # função que reescreve o json
    updateJson(jsonDirectory, usersList)

    # ATUALIZANDO A SENHA - PASS
    userForUpdate3 = "Mike"
    newSenha = "8845"

    # função que atualiza a senha do usuario
    updateUserSenha(userForUpdate3, newSenha, usersList)

    # função que atualiza o json
    updateJson(jsonDirectory, usersList)


