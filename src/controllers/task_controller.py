"""
TaskTracker — Controller Layer
Gerencia a interface por linha de comando (CLI), recebe inputs e exibe os menus.
Estudante: Klaus Müller Marques | RA: 22301876
"""

from typing import List
from models.task_model import Task
from services.task_service import TaskService


class TaskController:
    """
    Controlador CLI do TaskTracker.
    Interage com o usuário, trata erros de entrada e aciona o TaskService.
    """

    def __init__(self, service: TaskService) -> None:
        self.service = service

    def exibir_banner(self) -> None:
        """Exibe o cabeçalho inicial do sistema."""
        print("\n" + "#" * 58)
        print("#  TaskTracker CLI — Gestão Modular de Tarefas           #")
        print("#  Arquitetura em Camadas (Fase 1 / Fase 2 - UniCEUB)    #")
        print("#  Estudante: Klaus Müller Marques | RA: 22301876        #")
        print("#" * 58)

    def exibir_menu(self) -> None:
        """Exibe o menu com as opções principais e módulos avançados."""
        print("\n" + "=" * 58)
        print("               TASKTRACKER - MENU PRINCIPAL")
        print("=" * 58)
        print("  --- Requisitos Centrais da Fase 2 ---")
        print("  [1] Cadastrar nova tarefa")
        print("  [2] Visualizar tarefas cadastradas")
        print("  [3] Sair da aplicação")
        print("  --- Módulos Estendidos do Planejamento Lógico (Fase 1) ---")
        print("  [4] Buscar tarefa por ID")
        print("  [5] Atualizar status da tarefa")
        print("  [6] Editar tarefa")
        print("  [7] Remover tarefa")
        print("  [8] Filtrar tarefas por prioridade")
        print("-" * 58)

    def _renderizar_tarefa(self, tarefa: Task) -> None:
        """Exibe os dados de uma única tarefa formatada como card."""
        d = tarefa.to_dict()
        print(f"  ┌─ Tarefa #{d['id']} ─────────────────────────────────")
        print(f"  │ Título:      {d['title']}")
        print(f"  │ Descrição:   {d['description']}")
        print(f"  │ Prioridade:  {d['priority']}")
        print(f"  │ Data Limite: {d['due_date']}")
        print(f"  │ Status:      {d['status']}")
        print(f"  └────────────────────────────────────────────────────\n")

    def _renderizar_lista(self, tarefas: List[Task], titulo_secao: str = "TAREFAS CADASTRADAS") -> None:
        """Exibe a lista de tarefas ou mensagem informativa caso esteja vazia."""
        print("\n" + "=" * 58)
        print(f"             {titulo_secao}")
        print("=" * 58)

        if not tarefas:
            print("\n  [INFO] Nenhuma tarefa cadastrada no momento.\n")
            print("  Utilize a opção [1] do menu para cadastrar sua primeira atividade.")
            print("-" * 58)
            return

        print(f"  Total de registros: {len(tarefas)}\n")
        for t in tarefas:
            self._renderizar_tarefa(t)
        print("-" * 58)

    # --- Handlers dos Módulos ---

    def handle_create_task(self) -> None:
        """Módulo 1: Cadastrar Nova Tarefa com validações defensivas."""
        print("\n" + "=" * 58)
        print("             CADASTRO DE NOVA TAREFA")
        print("=" * 58)

        # Validação do Título (obrigatório e não vazio)
        while True:
            titulo = input("Digite o título da tarefa: ")
            try:
                titulo_valido = self.service.validar_titulo(titulo)
                break
            except ValueError as e:
                print(f"\n  [ERRO] {e}")
                print("  Por favor, digite um título válido.\n")

        # Descrição opcional
        descricao = input("Digite a descrição da tarefa (opcional - pressione Enter para pular): ")

        # Validação estrita de Prioridade
        while True:
            prioridade = input("Digite a prioridade (Alta / Média / Baixa): ")
            try:
                prioridade_valida = self.service.validar_prioridade(prioridade)
                break
            except ValueError as e:
                print(f"\n  [ERRO] {e}")
                print("  Por favor, tente novamente.\n")

        # Validação de Data Limite
        while True:
            data_limite = input("Digite a data limite (ex: DD/MM/AAAA ou AAAA-MM-DD - opcional): ")
            try:
                data_valida = self.service.validar_data_limite(data_limite)
                break
            except ValueError as e:
                print(f"\n  [ERRO] {e}")
                print("  Por favor, informe uma data válida.\n")

        nova_tarefa = self.service.create_task(titulo_valido, descricao, prioridade_valida, data_valida)
        print("\n----------------------------------------------------------")
        print(f"  [SUCESSO] Tarefa cadastrada com sucesso! (ID #{nova_tarefa.id})")
        print(f"  Status inicial atribuído: '{nova_tarefa.status}'")
        print("----------------------------------------------------------")

    def handle_list_tasks(self) -> None:
        """Módulo 2: Listagem Geral de Tarefas."""
        tarefas = self.service.list_tasks()
        self._renderizar_lista(tarefas)

    def handle_find_task_by_id(self) -> None:
        """Módulo 3: Consulta de Tarefa por ID."""
        print("\n" + "=" * 58)
        print("             CONSULTAR TAREFA POR ID")
        print("=" * 58)
        entrada = input("Digite o ID da tarefa desejada: ").strip()
        try:
            task_id = int(entrada)
        except ValueError:
            print("\n  [ERRO] O ID deve ser um número inteiro válido.")
            return

        tarefa = self.service.find_task_by_id(task_id)
        if not tarefa:
            print(f"\n  [AVISO] Nenhuma tarefa encontrada com o ID #{task_id}.")
        else:
            print(f"\n  Tarefa localizada com sucesso:")
            self._renderizar_tarefa(tarefa)

    def handle_update_status(self) -> None:
        """Módulo 4: Alteração de Status da Tarefa."""
        print("\n" + "=" * 58)
        print("             ATUALIZAR STATUS DA TAREFA")
        print("=" * 58)
        entrada = input("Digite o ID da tarefa: ").strip()
        try:
            task_id = int(entrada)
        except ValueError:
            print("\n  [ERRO] O ID deve ser um número inteiro válido.")
            return

        tarefa = self.service.find_task_by_id(task_id)
        if not tarefa:
            print(f"\n  [ERRO] Tarefa #{task_id} não existe no sistema.")
            return

        print(f"  Status atual: '{tarefa.status}'")
        print("  Opções disponíveis:")
        print("    [1] Pendente")
        print("    [2] Em Andamento")
        print("    [3] Concluída")
        opcao = input("Escolha o novo status (1-3): ").strip()
        mapa = {"1": "Pendente", "2": "Em Andamento", "3": "Concluída"}
        novo_status = mapa.get(opcao)
        if not novo_status:
            print("\n  [ERRO] Opção de status inválida.")
            return

        atualizada = self.service.update_task_status(task_id, novo_status)
        print(f"\n  [SUCESSO] Status da Tarefa #{atualizada.id} atualizado para '{atualizada.status}'.")

    def handle_edit_task(self) -> None:
        """Módulo 5: Edição Completa de Tarefa."""
        print("\n" + "=" * 58)
        print("             EDIÇÃO DE TAREFA")
        print("=" * 58)
        entrada = input("Digite o ID da tarefa a ser modificada: ").strip()
        try:
            task_id = int(entrada)
        except ValueError:
            print("\n  [ERRO] O ID deve ser um número inteiro válido.")
            return

        tarefa = self.service.find_task_by_id(task_id)
        if not tarefa:
            print(f"\n  [ERRO] Tarefa #{task_id} não encontrada.")
            return

        print(f"\nEditando Tarefa #{tarefa.id}. Pressione [Enter] para manter o valor atual.")
        novo_titulo = input(f"Novo título [{tarefa.title}]: ")
        nova_desc = input(f"Nova descrição [{tarefa.description}]: ")
        nova_prioridade = input(f"Nova prioridade [{tarefa.priority}]: ")
        nova_data = input(f"Nova data limite [{tarefa.due_date}]: ")

        try:
            self.service.edit_task(
                task_id=task_id,
                title=novo_titulo if novo_titulo.strip() else None,
                description=nova_desc if nova_desc.strip() else None,
                priority=nova_prioridade if nova_prioridade.strip() else None,
                due_date=nova_data if nova_data.strip() else None,
            )
            print(f"\n  [SUCESSO] Tarefa #{task_id} atualizada com êxito!")
        except ValueError as e:
            print(f"\n  [ERRO] Falha ao atualizar: {e}")

    def handle_delete_task(self) -> None:
        """Módulo 6: Exclusão / Remoção de Tarefa."""
        print("\n" + "=" * 58)
        print("             REMOÇÃO DE TAREFA")
        print("=" * 58)
        entrada = input("Digite o ID da tarefa que deseja excluir: ").strip()
        try:
            task_id = int(entrada)
        except ValueError:
            print("\n  [ERRO] O ID deve ser um número inteiro válido.")
            return

        tarefa = self.service.find_task_by_id(task_id)
        if not tarefa:
            print(f"\n  [ERRO] Tarefa #{task_id} não encontrada.")
            return

        confirma = input(f"Tem certeza que deseja remover a tarefa '{tarefa.title}'? (S/N): ").strip().upper()
        if confirma == "S":
            self.service.delete_task(task_id)
            print(f"\n  [SUCESSO] Tarefa #{task_id} excluída permanentemente.")
        else:
            print("\n  [INFO] Operação de remoção cancelada. Dados preservados.")

    def handle_filter_by_priority(self) -> None:
        """Módulo 7: Filtragem por Prioridade."""
        print("\n" + "=" * 58)
        print("             FILTRAR TAREFAS POR PRIORIDADE")
        print("=" * 58)
        p = input("Informe a categoria de prioridade ('Alta', 'Média' ou 'Baixa'): ")
        try:
            tarefas_filtradas = self.service.filter_tasks_by_priority(p)
            self._renderizar_lista(tarefas_filtradas, titulo_secao=f"TAREFAS COM PRIORIDADE '{p.upper()}'")
        except ValueError as e:
            print(f"\n  [ERRO] {e}")

    # --- Loop Principal da Aplicação ---

    def run(self) -> None:
        """Loop contínuo de controle da aplicação CLI."""
        self.exibir_banner()
        while True:
            try:
                self.exibir_menu()
                opcao = input("Escolha uma opção (1-8): ").strip()

                if opcao == "1":
                    self.handle_create_task()
                elif opcao == "2":
                    self.handle_list_tasks()
                elif opcao == "3":
                    print("\n==========================================================")
                    print("  Encerrando o TaskTracker. Obrigado por utilizar!")
                    print("==========================================================\n")
                    break
                elif opcao == "4":
                    self.handle_find_task_by_id()
                elif opcao == "5":
                    self.handle_update_status()
                elif opcao == "6":
                    self.handle_edit_task()
                elif opcao == "7":
                    self.handle_delete_task()
                elif opcao == "8":
                    self.handle_filter_by_priority()
                elif opcao in ("0", "sair", "exit"):
                    print("\n==========================================================")
                    print("  Encerrando o TaskTracker. Até breve!")
                    print("==========================================================\n")
                    break
                else:
                    print("\n  [ERRO] Opção inválida! Escolha um número do menu (1 a 8).")
            except (KeyboardInterrupt, EOFError):
                print("\n\n[INFO] Operação interrompida pelo usuário. Encerrando TaskTracker.")
                break
