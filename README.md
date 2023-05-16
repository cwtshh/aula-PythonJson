# Como usar Python e JSON para armazenar dados localmente
Uma aula sobre python e JSON

# O que é JSON?

   O formato JSON (JavaScript Object Notation) é, como o nome sugere, uma forma de notação de objetos JavaScript de modo que eles possam ser representados de uma forma comum a diversas linguagens.
   Além disso, uma ideia que está fortemente enraizada neste formato é que ele seja facilmente trafegado entre aplicações em quaisquer protocolos, inclusive o HTTP. Portanto, a principal diferença entre um objeto JavaScript padrão e um JSON é o fato do JSON ser na realidade: um texto.

# Estrutura de um JSON

![Screenshot_1](https://github.com/cwtshh/aula-PythonJson/assets/101185927/18299b5c-1442-4543-99fb-b3d6511aad85)

# E como podemos usar isso em python?

# Coisas importantes

Funções importantes:

   ``` Open("file.json") ```
   > Abrir o arquivo

   ```json.load(nome_arquivo)``` 
   > Converter um arquivo para Json

   ```Json.dump()```
   > Converter uma lista de dicionários para Json

   ```vars(object)``` 
   > Converte um objeto para dicionário

Noções importantes:

* If, for
* Dicionários python
    
# Por onde começamos?

Começamos fazemos o import da biblioteca json:

``` import json ```

Após isso precisamos criar nosso arquivo para leitura:

***IMPORTANTE!***

Coloque [ ] no arquivo json, caso contrário o programa irá dar erro

# Como podemos ler o arquivo?

* Usamos a função open(), juntamente com a função json.load(). Desta forma, iremos abrir um arquivo e converte-lo para um dicionário.

![Screenshot_2](https://github.com/cwtshh/aula-PythonJson/assets/101185927/f00c610c-616b-45b5-b4ce-b55a750ee10d)

* Assim podemos manipular o nosso json de maneira dinâmica e simples.

# E agora?

Com o arquivo carregado e convertido em um dicionário, podemos realizar todas as operações que desejamos!
A seguir vamos aprender a:

* Colocar objetos dentro de um json

* Atualizar atributos de um objeto vindo de um json

* Deletar objeto vindo de um json

# Adicionando objetos ao json

É simples!

1º - Precisamos converter o nosso objeto para um dicionário. (vars())

![Screenshot_3](https://github.com/cwtshh/aula-PythonJson/assets/101185927/70780099-7402-4363-b6a6-475ac175f022)

2º - Adicionamos o dicionário convertido a nossa lista de dicionários. (append())

Por ultimo nos vamos sobrescrever todo o conteúdo do nosso arquivo json.

![Screenshot_4](https://github.com/cwtshh/aula-PythonJson/assets/101185927/132ae647-9762-4eae-9591-a8e326e3430d)

O comando json.dump() é usado para, ao mesmo tempo, converter nossa lista de dicionários para objetos json e os passar para um arquivo .json.

# Atualizando objetos json

Apartir daqui é mais fácil ainda!

Como estamos trabalhando com uma lista de dicionários podemos acessar elementos especifícos e alterar seus atributos.

Usando uma combinação de for e if podemos fazer isso.

![Screenshot_5](https://github.com/cwtshh/aula-PythonJson/assets/101185927/bd037b48-be28-4e57-91f9-36278741e765)

Após isso, podemos reescrever o nosso arquivo json para aplicar as modificações.

![Screenshot_4](https://github.com/cwtshh/aula-PythonJson/assets/101185927/132ae647-9762-4eae-9591-a8e326e3430d)

# Deletando um objeto json

Podemos aproveitar a mesma ideia que usamos para atualizar o objeto, apenas mudamos um pouco da lógica.

```def deleteUser(userName, userList):
    for user in userList:
        if user['nome'] == userName:
            userList.remove(user) 
```

E por fim... É só sobrescrever nosso arquivo!

![Screenshot_4](https://github.com/cwtshh/aula-PythonJson/assets/101185927/132ae647-9762-4eae-9591-a8e326e3430d)
    
