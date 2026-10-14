"""
TaskTracker — Model Layer
Define a estrutura de dados e propriedades da classe Task.
Estudante: Klaus Müller Marques | RA: 22301876
"""

from typing import Dict, Any


class Task:
    """
    Representa a entidade de uma Tarefa no sistema TaskTracker.
    
    Atributos:
        id (int): Identificador único gerado automaticamente pelo sistema.
        title (str): Título descritivo obrigatório da tarefa.
        description (str): Detalhamento textual opcional.
        priority (str): Prioridade estrita ('Alta', 'Média' ou 'Baixa').
        due_date (str): Data planejada para conclusão (ex: AAAA-MM-DD ou DD/MM/AAAA).
        status (str): Estado de execução ('Pendente', 'Em Andamento' ou 'Concluída').
    """

    def __init__(
        self,
        id: int,
        title: str,
        description: str = "",
        priority: str = "Média",
        due_date: str = "",
        status: str = "Pendente"
    ) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
        """Converte o objeto Task em um dicionário para serialização e exibição."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description or "(Sem descrição informada)",
            "priority": self.priority,
            "due_date": self.due_date or "(Sem data limite definida)",
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Instancia um objeto Task a partir de um dicionário de dados."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", "Média"),
            due_date=data.get("due_date", ""),
            status=data.get("status", "Pendente"),
        )

    def __repr__(self) -> str:
        return f"<Task id={self.id} title='{self.title}' priority='{self.priority}' status='{self.status}'>"
