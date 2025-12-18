filmes_a_ver = ["descendentes", "titanic", "a bela e a fera", "frozen", "moana"]
filmes_assistidos = []

while True:
    menu = f"""
    {'=' * 30}
    Lista de filmes pendentes
    {'=' * 30}
    [1] Adicionar Filme à Lista Para Ver
    [2] Marcar Filme como Visto
    [3] Listar Filmes Pendentes/Assistidos
    [4] Consultar um Título Específico
    [5] Sair
    {'=' * 30}  
    """

    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_filme = input("Digite o filme que deseja ver: ").strip().title()
        
        if novo_filme: 
            filmes_a_ver.append(novo_filme)
            print(f"Filme '{novo_filme}' adicionado à lista de filmes para ver.")
        else:
            print("Nenhum filme adicionado. A descrição não pode ser vazia.")


    elif opcao == "2":
        for i, filme in enumerate(filmes_a_ver):
            print(f"[{i}] {filme}")

        indice_str = input("\nDigite o ÍNDICE do filme que você acabou de assistir: ").strip()
        
        if indice_str.isdigit():
            indice_a_remover = int(indice_str)
            
            if 0 <= indice_a_remover < len(filmes_a_ver):
                filme_movido = filmes_a_ver.pop(indice_a_remover) 
                
                filmes_assistidos.append(filme_movido)
                
                print(f"\n Filme '{filme_movido}' movido para sua lista de VISTOS!")
            else:
                print("\n ERRO: Índice inválido.")
        else:
            print("\n ERRO: Por favor, digite um número inteiro.")


    elif opcao == "3":

        print("Qual lista deseja ver?")
        print("[1] Filmes Pendentes (A VER)")
        print("[2] Filmes Assistidos (VISTOS)")

        escolha_lista = input("Digite 1 ou 2: ")

        lista_escolhida = []
        nome_lista = ""

        if escolha_lista == "1" :
            lista_escolhida = filmes_a_ver
            nome_lista = "PENDENTES"

        elif escolha_lista == "2":
            lista_escolhida = filmes_assistidos
            nome_lista = "VISTO"

        else:
            print("\nOpção inválida! Voltando ao menu principal.")
            continue

        if not lista_escolhida:
            print(f"A lista está vazia.")
        else:
            for i, filme in enumerate(lista_escolhida):
                print(f"[{i + 1}] {filme}") 
        print("-" * 35)


    elif opcao == "4":
        titulo_consulta = input("Qual titulo de filme deseja buscar? ").strip().title()

        total_a_ver = filmes_a_ver.count(titulo_consulta)
        total_vistos = filmes_assistidos.count(titulo_consulta)
        total_geral = total_a_ver + total_vistos

        if total_geral == 0:
            print(f"O filme '{titulo_consulta}' não foi encontrado em nenhuma das listas")

        else:
            if total_a_ver > 0:
                print(f"PENDENTE: Você ainda não assistiu o filme {titulo_consulta}.")
            
            if total_vistos > 0:
                print(f"ASSISTIDO: O filme {titulo_consulta} já foi assistido.")
        print("-" * 35)

    elif opcao == "5":
            print("Saindo do sistema de filmes!")
            break

    else: 
        print("Digite um número válido.")