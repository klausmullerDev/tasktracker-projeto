"""
TaskTracker — Repository Layer
Encapsula o acesso aos dados e abstrai o armazenamento em memória.
Estudante: Klaus Müller Marques | RA: 22301876
"""

from typing import List, Optional
from models.task_model import Task


class TaskRepository:
    """
    Repositório em memória para persistência de tarefas.
    Garante integridade e controle de identificadores sequenciais.
    """

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def create(self, task: Task) -> Task:
        """Adiciona uma nova tarefa gerando um ID sequencial automático."""
        task.id = self._next_id
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all(self) -> List[Task]:
        """Retorna todas as tarefas registradas."""
        return list(self._tasks)

    def find_by_id(self, task_id: int) -> Optional[Task]:
        """Busca uma tarefa pelo identificador numérico (ID)."""
        for t in self._tasks:
            if t.id == task_id:
                return t
        return None

    def update(self, updated_task: Task) -> Optional[Task]:
        """Atualiza os dados de uma tarefa existente."""
        for i, t in enumerate(self._tasks):
            if t.id == updated_task.id:
                self._tasks[i] = updated_task
                return updated_task
        return None

    def delete(self, task_id: int) -> bool:
        """Remove a tarefa com o ID fornecido. Retorna True se removida com sucesso."""
        for i, t in enumerate(self._tasks):
            if t.id == task_id:
                del self._tasks[i]
                return True
        return False

    def filter_by_priority(self, priority: str) -> List[Task]:
        """Retorna a lista de tarefas filtrada por prioridade."""
        p_clean = priority.strip().lower()
        return [t for t in self._tasks if t.priority.strip().lower() == p_clean]
