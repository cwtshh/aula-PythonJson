import json



if __name__ == "__main__":

    file_directory = "D:\\UnB\\Orientação a Objetos - Python - Monitoria\\1 - Orientação a Objetos - Como usar JSON em Pyhton\\aula-PythonJson\\openJson\\database\\users.json"

    # Abre o arquivo JSON
    with open(file_directory) as users_file:
        file_contents = users_file.read()

    #Converte o JSON para um dicionario
    convert_json = json.loads(file_contents)

    for user in convert_json:
        print(f"{user}\n")

    