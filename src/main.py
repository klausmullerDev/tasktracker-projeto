"""
TaskTracker — Ponto de Entrada (Bootstrapping)
Bootcamp II — Fase 2: Entrega Intermediária (UniCEUB)
Estudante: Klaus Müller Marques | RA: 22301876
Curso: Bacharelado em Ciência da Computação (8º Semestre)

Responsável pela injeção de dependências e inicialização da aplicação:
  TaskRepository -> TaskService -> TaskController -> controller.run()
"""

import sys
import os

# Garante a resolução correta dos módulos internos a partir do diretório src
diretorio_src = os.path.dirname(os.path.abspath(__file__))
if diretorio_src not in sys.path:
    sys.path.insert(0, diretorio_src)

from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from controllers.task_controller import TaskController


def main() -> None:
    """
    Função principal de bootstrapping.
    Instancia o repositório, o serviço com as regras de negócio e o controller CLI.
    """
    repository = TaskRepository()
    service = TaskService(repository=repository)
    controller = TaskController(service=service)
    controller.run()


if __name__ == "__main__":
    main()
