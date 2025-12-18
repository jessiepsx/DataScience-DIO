tarefas = []
tarefas_concluidas = []

while True:
    menu = f"""
    {'=' * 30}
    Lista de tarefas 
    {'=' * 30}
    [1] Adicionar tarefa
    [2] Listar tarefas
    [3] Marcar tarefa como concluida
    [4] Remover tarefa 
    [5] Exibir Resumo das tarefas
    [6] Sair
    {'=' * 30}  
    """

    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            print("\n--- Modo Adicionar Tarefas ---")
            print("Digite 'FIM' a qualquer momento para voltar ao Menu Principal.")
            
            adicionar_tarefa = input("Digite a tarefa que deseja adicionar: ")

            if adicionar_tarefa.upper() == "FIM":
                print("\n Voltando ao Menu Principal.\n")
                break 

            elif adicionar_tarefa != "":
                tarefas.append(adicionar_tarefa)
                print(f"Tarefa '{adicionar_tarefa}' adicionada com sucesso!")

            else:
                print("Nenhuma tarefa foi adicionada. Tente novamente.")

        
    elif opcao == "2":
        print("\n--- Modo Listar Tarefas ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa na lista")

        else:
            print("Tarefas: ")
            for i, tarefa in enumerate(tarefas):
                print(f"[{i + 1}] {tarefa}")


    elif opcao == "3":
        print("\n--- Modo Marcar Tarefa como Concluida ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa na lista para marcar como concluida")

        else:
            numero_tarefa = int(input("Digite o número da tarefa que deseja marcar como concluida:"))
            indice_real = numero_tarefa - 1

            if 0 <= indice_real < len(tarefas):
                tarefa_concluida = tarefas.pop(indice_real)
                tarefas_concluidas.append(tarefa_concluida)

                print(f"Tarefa '{tarefa_concluida}' marcada como concluida!")

            else: 
                print("Numero de tarefa invalido")


    elif opcao == "4":
        print("\n--- Modo Remover Tarefas ---")

        numero_tarefa = int(input("Digite o número da tarefa que deseja remover:"))

        indice_real = numero_tarefa - 1

        if 0 <= indice_real < len(tarefas):
                tarefa_removida = tarefas.pop(indice_real)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")

        else: 
            print("Numero de tarefa invalido")

    elif opcao == "5":
        print("\n--- Modo Resumo das Tarefas ---")
        total = len(tarefas) + len(tarefas_concluidas)
        pendentes = len(tarefas)
        concluidas = len(tarefas_concluidas)

        if total <= 5:
            print("Você está indo bem! Continue assim.")

        elif 6 <= total <= 10:
            print("Cuidado! Você tem muitas tarefas pendentes.")

        else:
            print("Alerta! Você tem um número excessivo de tarefas pendentes!")

        print(f"Resumo das tarefas: ")
        print(f"Total de tarefas: {total}")
        print(f"Tarefas concluídas: {concluidas}") 
        print(f"Tarefas pendentes: {pendentes}")

    elif opcao == "6":
        print("Saindo do sistema de tarefas. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")