"""
TaskTracker — Fase 2 (Entrega Intermediária)
Estudante: Klaus Müller Marques | RA: 22301876
Curso: Bacharelado em Ciência da Computação — UniCEUB

Estrutura principal da aplicação CLI e loop de navegação do menu.
"""

import sys

# Lista em memória para armazenamento das tarefas
tarefas = []


def exibir_menu():
    """Exibe as opções do menu principal da aplicação."""
    print("\n" + "=" * 50)
    print("           TASKTRACKER - MENU PRINCIPAL")
    print("=" * 50)
    print("  [1] Cadastrar nova tarefa")
    print("  [2] Visualizar tarefas cadastradas")
    print("  [3] Sair da aplicação")
    print("-" * 50)


def cadastrar_tarefa():
    """Rotina inicial para cadastro de tarefas."""
    print("\n--- CADASTRO DE NOVA TAREFA ---")
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
    data_limite = input("Digite a data limite (DD/MM/AAAA): ")

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(nova_tarefa)
    print("[OK] Tarefa cadastrada com sucesso!")


def visualizar_tarefas():
    """Rotina inicial para exibição das tarefas."""
    print("\n--- TAREFAS CADASTRADAS ---")
    if not tarefas:
        print("[INFO] Nenhuma tarefa cadastrada no momento.")
        return

    for t in tarefas:
        print(f"ID: {t['id']} | Título: {t['titulo']} | Prioridade: {t['prioridade']} | Status: {t['status']}")


def main():
    """Loop principal da aplicação."""
    print("Inicializando TaskTracker...")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nEncerrando a aplicação TaskTracker. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Digite um número de 1 a 3.")


if __name__ == "__main__":
    main()
