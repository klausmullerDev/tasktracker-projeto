"""
TaskTracker — Service Layer
Centraliza as regras de negócio, validações estritas e integridade de dados.
Estudante: Klaus Müller Marques | RA: 22301876
"""

from datetime import datetime
from typing import List, Optional
from models.task_model import Task
from repositories.task_repository import TaskRepository


class TaskService:
    """
    Camada de serviço do TaskTracker.
    Aplica as regras de validação antes de delegar a persistência ao repositório.
    """

    PRIORIDADES_VALIDAS = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
    STATUS_VALIDOS = {"pendente": "Pendente", "em andamento": "Em Andamento", "concluída": "Concluída", "concluida": "Concluída"}

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def validar_titulo(self, title: str) -> str:
        """
        Valida a obrigatoriedade do título.
        Regra: Não pode ser nulo, vazio ou composto unicamente por espaços.
        """
        if not title or not title.strip():
            raise ValueError("O título da tarefa é obrigatório e não pode ser vazio ou conter apenas espaços.")
        return title.strip()

    def validar_prioridade(self, priority: str) -> str:
        """
        Validação estrita do domínio de prioridade.
        Regra: Aceita exclusivamente 'Alta', 'Média' (ou 'Media') e 'Baixa'.
        """
        if not priority:
            raise ValueError("A prioridade é obrigatória. Escolha entre 'Alta', 'Média' ou 'Baixa'.")
        
        p_clean = priority.strip().lower()
        if p_clean not in self.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridade inválida '{priority}'. As opções aceitas são estritamente: 'Alta', 'Média' ou 'Baixa'.")
        
        return self.PRIORIDADES_VALIDAS[p_clean]

    def validar_data_limite(self, due_date: str) -> str:
        """
        Valida o formato da data planejada e verifica se não é retroativa.
        Suporta formatos AAAA-MM-DD e DD/MM/AAAA.
        Se deixado em branco, aceita como sem prazo definido.
        """
        if not due_date or not due_date.strip():
            return ""

        texto = due_date.strip()
        formatos = ["%Y-%m-%d", "%d/%m/%Y"]
        data_parseada = None

        for fmt in formatos:
            try:
                data_parseada = datetime.strptime(texto, fmt).date()
                break
            except ValueError:
                continue

        if data_parseada:
            hoje = datetime.now().date()
            if data_parseada < hoje:
                raise ValueError(f"Data retroativa detectada ({texto}). A data limite deve ser igual ou posterior à data atual ({hoje.strftime('%d/%m/%Y')}).")
            return data_parseada.strftime("%d/%m/%Y")

        # Se for texto livre não retroativo detectado
        return texto

    def validar_status(self, status: str) -> str:
        """Validação estrita dos status permitidos."""
        if not status:
            return "Pendente"
        s_clean = status.strip().lower()
        if s_clean not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido '{status}'. Permitidos: 'Pendente', 'Em Andamento', 'Concluída'.")
        return self.STATUS_VALIDOS[s_clean]

    # --- Operações de Negócio (Módulos 1 a 7) ---

    def create_task(self, title: str, description: str, priority: str, due_date: str) -> Task:
        """Módulo 1: Cadastro de Nova Tarefa."""
        titulo_validado = self.validar_titulo(title)
        prioridade_validada = self.validar_prioridade(priority)
        data_validada = self.validar_data_limite(due_date)

        nova_tarefa = Task(
            id=0,  # Atribuído pelo repositório
            title=titulo_validado,
            description=description.strip() if description else "",
            priority=prioridade_validada,
            due_date=data_validada,
            status="Pendente",
        )
        return self.repository.create(nova_tarefa)

    def list_tasks(self) -> List[Task]:
        """Módulo 2: Listagem Geral de Tarefas."""
        return self.repository.get_all()

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """Módulo 3: Consulta de Tarefa por ID."""
        return self.repository.find_by_id(task_id)

    def update_task_status(self, task_id: int, new_status: str) -> Task:
        """Módulo 4: Alteração de Status da Tarefa."""
        tarefa = self.repository.find_by_id(task_id)
        if not tarefa:
            raise LookupError(f"Tarefa com ID #{task_id} não encontrada no repositório.")
        status_validado = self.validar_status(new_status)
        tarefa.status = status_validado
        self.repository.update(tarefa)
        return tarefa

    def edit_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[str] = None,
        due_date: Optional[str] = None,
    ) -> Task:
        """Módulo 5: Edição Completa de Tarefa."""
        tarefa = self.repository.find_by_id(task_id)
        if not tarefa:
            raise LookupError(f"Tarefa com ID #{task_id} não encontrada no repositório.")

        if title is not None and title.strip():
            tarefa.title = self.validar_titulo(title)
        if description is not None and description.strip():
            tarefa.description = description.strip()
        if priority is not None and priority.strip():
            tarefa.priority = self.validar_prioridade(priority)
        if due_date is not None and due_date.strip():
            tarefa.due_date = self.validar_data_limite(due_date)

        self.repository.update(tarefa)
        return tarefa

    def delete_task(self, task_id: int) -> bool:
        """Módulo 6: Exclusão / Remoção de Tarefa."""
        tarefa = self.repository.find_by_id(task_id)
        if not tarefa:
            raise LookupError(f"Tarefa com ID #{task_id} não encontrada no repositório.")
        return self.repository.delete(task_id)

    def filter_tasks_by_priority(self, priority: str) -> List[Task]:
        """Módulo 7: Filtragem por Prioridade."""
        prioridade_validada = self.validar_prioridade(priority)
        return self.repository.filter_by_priority(prioridade_validada)
