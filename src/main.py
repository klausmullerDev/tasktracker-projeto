"""
TaskTracker — Sistema de Gestão Modular de Tarefas (CLI)
Bootcamp II — Fase 2: Entrega Intermediária
Instituição: UniCEUB
Estudante: Klaus Müller Marques | RA: 22301876
Curso: Bacharelado em Ciência da Computação (8º Semestre)

Arquivo: src/main.py
Descrição: Código-fonte principal da aplicação TaskTracker contendo o menu interativo,
           as regras de negócio e validações estritas de entrada, e a persistência em memória.
"""

from typing import List, Dict, Any, Optional

# Base de dados em memória para as tarefas
tarefas: List[Dict[str, Any]] = []
_contador_id: int = 1


# ==============================================================================
# FUNÇÕES DE VALIDAÇÃO DE ENTRADAS (REGRAS DE NEGÓCIO)
# ==============================================================================

def validar_titulo(texto: str) -> bool:
    """
    Verifica se o título é válido.
    Regra: O título não pode ser nulo, vazio ou conter apenas espaços em branco.
    """
    return bool(texto and texto.strip())


def validar_prioridade(texto: str) -> Optional[str]:
    """
    Validação estrita de prioridade.
    Aceita exclusivamente: 'Alta', 'Média' (ou 'Media') e 'Baixa'.
    Retorna o valor normalizado ('Alta', 'Média', 'Baixa') ou None se inválido.
    """
    if not texto:
        return None
    
    padrao = texto.strip().lower()
    mapa_prioridades = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa",
    }
    return mapa_prioridades.get(padrao)


def solicitar_titulo() -> str:
    """
    Solicita o título da tarefa em loop contínuo até que uma entrada válida seja fornecida.
    Rejeita valores vazios ou apenas espaços em branco.
    """
    while True:
        entrada = input("Digite o título da tarefa: ")
        if validar_titulo(entrada):
            return entrada.strip()
        print("\n  [ERRO] O título da tarefa é obrigatório e não pode ser vazio ou composto apenas por espaços!")
        print("  Por favor, digite um título válido.\n")


def solicitar_prioridade() -> str:
    """
    Solicita a prioridade da tarefa em loop contínuo até que um valor aceito seja informado.
    Validação estrita: exclusivamente 'Alta', 'Média' (ou 'Media') e 'Baixa'.
    """
    while True:
        entrada = input("Digite a prioridade (Alta / Média / Baixa): ")
        prioridade_valida = validar_prioridade(entrada)
        if prioridade_valida:
            return prioridade_valida
        print("\n  [ERRO] Prioridade inválida! As opções aceitas são estritamente: 'Alta', 'Média' ou 'Baixa'.")
        print("  Por favor, tente novamente.\n")


def solicitar_descricao() -> str:
    """Solicita a descrição opcional da tarefa."""
    entrada = input("Digite a descrição da tarefa (opcional - pressione Enter para pular): ").strip()
    return entrada if entrada else "(Sem descrição informada)"


def solicitar_data_limite() -> str:
    """Solicita a data limite planejada para a conclusão da tarefa."""
    entrada = input("Digite a data limite (ex: DD/MM/AAAA ou livre - pressione Enter para pular): ").strip()
    return entrada if entrada else "(Sem data limite definida)"


# ==============================================================================
# OPERAÇÕES PRINCIPAIS DA APLICAÇÃO (CADASTRO E LISTAGEM)
# ==============================================================================

def cadastrar_nova_tarefa() -> None:
    """
    Fluxo de cadastro de uma nova tarefa com aplicação das regras de negócio:
    - ID automático e incremental
    - Título validado (não vazio)
    - Descrição livre
    - Prioridade com validação estrita (Alta, Média, Baixa)
    - Data limite
    - Status definido automaticamente como 'Pendente'
    """
    global _contador_id

    print("\n" + "=" * 55)
    print("             CADASTRO DE NOVA TAREFA")
    print("=" * 55)

    titulo = solicitar_titulo()
    descricao = solicitar_descricao()
    prioridade = solicitar_prioridade()
    data_limite = solicitar_data_limite()

    nova_tarefa: Dict[str, Any] = {
        "id": _contador_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }

    tarefas.append(nova_tarefa)
    _contador_id += 1

    print("\n-------------------------------------------------------")
    print(f" [SUCESSO] Tarefa cadastrada com sucesso! (ID #{nova_tarefa['id']})")
    print(f" Status inicial: '{nova_tarefa['status']}'")
    print("-------------------------------------------------------")


def visualizar_tarefas_cadastradas() -> None:
    """
    Exibe a listagem de todas as tarefas cadastradas.
    - Se a lista estiver vazia: exibe mensagem clara informando ausência de registros.
    - Se houver tarefas: itera e exibe todas as propriedades de forma legível e organizada.
    """
    print("\n" + "=" * 55)
    print("             TAREFAS CADASTRADAS")
    print("=" * 55)

    if not tarefas:
        print("\n [INFO] Nenhuma tarefa cadastrada no momento.\n")
        print(" Utilize a opção [1] do menu para cadastrar sua primeira atividade.")
        print("-" * 55)
        return

    print(f" Total de tarefas registradas: {len(tarefas)}\n")

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"  ┌─ Tarefa #{tarefa['id']} ─────────────────────────────────")
        print(f"  │ Título:      {tarefa['titulo']}")
        print(f"  │ Descrição:   {tarefa['descricao']}")
        print(f"  │ Prioridade:  {tarefa['prioridade']}")
        print(f"  │ Data Limite: {tarefa['data_limite']}")
        print(f"  │ Status:      {tarefa['status']}")
        print(f"  └────────────────────────────────────────────────────\n")

    print("-" * 55)


def exibir_menu_principal() -> None:
    """Renderiza visualmente o menu de opções do terminal."""
    print("\n" + "=" * 55)
    print("           TASKTRACKER - MENU PRINCIPAL")
    print("=" * 55)
    print("  [1] Cadastrar nova tarefa")
    print("  [2] Visualizar tarefas cadastradas")
    print("  [3] Sair da aplicação")
    print("-" * 55)


# ==============================================================================
# PONTO DE ENTRADA E LOOP DE NAVEGAÇÃO
# ==============================================================================

def main() -> None:
    """Loop contínuo de controle da aplicação por linha de comando."""
    print("\n" + "#" * 55)
    print("#  TaskTracker CLI - Inicialização do Sistema        #")
    print("#  Desenvolvido por: Klaus Müller Marques (UniCEUB)   #")
    print("#" * 55)

    while True:
        try:
            exibir_menu_principal()
            opcao = input("Escolha uma opção (1-3): ").strip()

            if opcao == "1":
                cadastrar_nova_tarefa()
            elif opcao == "2":
                visualizar_tarefas_cadastradas()
            elif opcao == "3":
                print("\n=======================================================")
                print("  Encerrando o TaskTracker. Obrigado por utilizar!")
                print("=======================================================\n")
                break
            else:
                print("\n  [ERRO] Opção inválida! Por favor, escolha '1', '2' ou '3'.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n[INFO] Operação interrompida pelo usuário. Encerrando TaskTracker.")
            break


if __name__ == "__main__":
    main()
