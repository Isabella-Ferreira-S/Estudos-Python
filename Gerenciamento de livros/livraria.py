# Inicio - Boas-vindas com o nome de identificação
print('*'*50)
print(' '*8 + "Bem-vindo a livraria da Isabella!")
print('*'*50)

# Lista de livros e variável global
lista_livro = []
id_global = 1

# Função para cadastrar livro
def cadastrar_livro(id):
    global id_global
    print('-'*50)
    print(' '*15 + 'Menu castrar livro')
    print('-'*50)
    id_livro = id_global
    id_global += 1
    nome = input("Qual o nome do livro que deseja cadastrar: ")
    autor = input("Qual o nome do autor do livro: ")
    editora = input("Qual a editora do livro: ")
    livro = {'id': id_livro, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    print("\nLivro cadastrado com sucesso!")

# Função para consultar livro (todos, por id, por autor e exibir uma mensagem de "erro" caso não localize)
def consultar_livro():
    global lista_livro
    print('-'*50)
    print(' '*15 + 'Menu consulta livro')
    print('-'*50)
    print("1. Consultar Todos")
    print("2. Consultar por Id")
    print("3. Consultar por Autor")
    print("4. Retornar ao menu")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\nListagem de todos os livros:\n")
        for livro in lista_livro:
            print("ID:", livro['id'])
            print("Nome:", livro['nome'])
            print("Autor:", livro['autor'])
            print("Editora:", livro['editora'])
            print()
    elif opcao == '2':
        id_consulta = int(input("Digite o ID do livro que deseja consultar: "))
        encontrado = False
        for livro in lista_livro:
            if livro['id'] == id_consulta:
                print("\nLivro encontrado: ")
                print("ID:", livro['id'])
                print("Nome:", livro['nome'])
                print("Autor:", livro['autor'])
                print("Editora:", livro['editora'])
                encontrado = True
                break
        if not encontrado:
            print("\nLivro não encontrado.")
    elif opcao == '3':
        autor_consulta = input("Digite o autor do livro: ")
        livros_encontrados = [
            livro for livro in lista_livro if livro['autor'] == autor_consulta]
        if livros_encontrados:
            print("\nLivro(s) encontrado(s) do autor", autor_consulta)
            for livro in livros_encontrados:
                print("ID:", livro['id'])
                print("Nome:", livro['nome'])
                print("Autor:", livro['autor'])
                print("Editora:", livro['editora'])
                print()
        else:
            print("\nNenhum livro encontrado deste autor.")
    elif opcao == '4':
        return
    else:
        print("Opção inválida")

# Função para remover livro
def remover_livro():
    id_remover = int(input("Digite o ID do livro a ser removido: "))
    global lista_livro
    livro_encontrado = False
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            livro_encontrado = True
            print("\nLivro removido com sucesso!")
            break
    if not livro_encontrado:
        print("Livro não encontrado.")


while True:
    print('-'*50)
    print(' '*15 + 'Menu Principal')
    print('-'*50)
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")
    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == '1':
        cadastrar_livro(id_global)
    elif opcao_menu == '2':
        consultar_livro()
    elif opcao_menu == '3':
        remover_livro()
    elif opcao_menu == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida")
