# TaskTracker — Sistema de Gestão Modular de Tarefas (CLI)

> **Bootcamp II — Fase 2: Entrega Intermediária (Desafio de Desenvolvimento e Versionamento)**  
> **Instituição:** Centro Universitário de Brasília (UniCEUB)  
> **Estudante:** Klaus Müller Marques  
> **Matrícula / RA:** 22301876  
> **Curso:** Bacharelado em Ciência da Computação (8º Semestre)  
> **E-mail Institucional:** klaus.muller.@sempreceub.com  

---

## 📌 1. Visão Geral do Projeto

O **TaskTracker** é uma aplicação em linha de comando (CLI — *Command Line Interface*) desenvolvida em **Python 3**, projetada sob os princípios da **Arquitetura em Camadas (Layered Architecture)** e boas práticas da Engenharia de Software. O sistema resolve a perda de prazos e a sobrecarga cognitiva através da centralização, priorização objetiva e acompanhamento do ciclo de vida de atividades cotidianas.

O projeto faz parte do **Bootcamp II (75 horas)**, dividido em três fases cumulativas:
1. **Fase 1 — Entrega Inicial (Concluída):** Planejamento Lógico, Arquitetura de Dados, Decomposição do Problema, Algoritmo em Português Estruturado e Mapeamento para Git/GitHub.
2. **Fase 2 — Entrega Intermediária (Etapa Atual):** Estruturação do repositório, versionamento profissional com Git/GitHub, implementação da arquitetura em camadas em Python 3 e validação estrita das regras de negócio.
3. **Fase 3 — Entrega Final (Próxima Etapa):** Empacotamento da aplicação, conteinerização com Docker, testes automatizados e deploy.

---

## 🗂️ 2. Arquitetura de Software e Estrutura do Repositório

O repositório reflete integralmente a **Arquitetura em Camadas** planejada no Documento de Planejamento Lógico e Arquitetural da Fase 1:

```plaintext
tasktracker-projeto/
├── README.md                   # Documentação explicativa do projeto e guia de execução
├── .gitignore                  # Arquivo de exclusão de artefatos temporários, caches e ambientes virtuais
├── docs/                       
│   └── planejamento_logico.pdf # Documento oficial de planejamento da Fase 1 mantido para rastreabilidade
└── src/                        
    ├── main.py                 # Ponto de entrada (Bootstrapping) e injeção de dependências
    ├── controllers/            
    │   ├── __init__.py
    │   └── task_controller.py  # Camada de Interface do Usuário (CLI) e controle de menus
    ├── services/               
    │   ├── __init__.py
    │   └── task_service.py     # Camada de Regras de Negócio e Validações estritas
    ├── repositories/           
    │   ├── __init__.py
    │   └── task_repository.py  # Camada de Persistência e Acesso a Dados em memória
    └── models/                 
        ├── __init__.py
        └── task_model.py       # Modelo da Entidade Task (dados e propriedades)
```

### Separação de Responsabilidades:
- **`models/task_model.py`:** Define a entidade `Task` contendo `id`, `title`, `description`, `priority`, `due_date` e `status`.
- **`repositories/task_repository.py`:** Encapsula o acesso aos dados em memória, gerenciando identificadores sequenciais automáticos e operações CRUD.
- **`services/task_service.py`:** Centraliza a inteligência do negócio, validação defensiva de inputs, captura de erros e integridade referencial.
- **`controllers/task_controller.py`:** Gerencia a interface de linha de comando, leitura interativa do terminal e renderização dos cards das tarefas.
- **`main.py`:** Ponto de entrada (*Bootstrapping*) que realiza a injeção de dependências (`TaskRepository` -> `TaskService` -> `TaskController`) e inicia o loop da aplicação.

---

## ⚙️ 3. Regras de Negócio e Validações Implementadas

O sistema aplica rigorosamente todas as validações desenhadas no algoritmo da Fase 1:

| Regra / Campo | Tipo | Obrigatoriedade | Descrição e Validação Estrita |
| :--- | :--- | :--- | :--- |
| **`id`** | Inteiro | Automático | Identificador único sequencial gerado automaticamente pelo repositório (1, 2, 3...). |
| **`title`** | String | Obrigatório | Não pode ser nulo, vazio ou composto unicamente por espaços em branco. O sistema repete o prompt defensivamente até um valor válido ser fornecido. |
| **`description`** | String | Opcional | Texto descritivo opcional com o detalhamento das ações. Teclar Enter preserva em branco. |
| **`priority`** | String | Obrigatório | **Validação Estrita:** aceita exclusivamente as opções `"Alta"`, `"Média"` (ou `"Media"`) e `"Baixa"` (sem distinção de maiúsculas/minúsculas). Entradas fora do padrão geram mensagem de erro e repetição do prompt. |
| **`due_date`** | String | Opcional | Data no formato `DD/MM/AAAA` ou `AAAA-MM-DD`. O serviço valida e rejeita datas retroativas em relação ao dia atual. |
| **`status`** | String | Automático | Definido automaticamente como `"Pendente"` no momento do cadastro. Transições aceitas: `"Pendente"`, `"Em Andamento"` e `"Concluída"`. |
| **Integridade** | Sistema | Obrigatório | Ações de busca, edição, exclusão e alteração de status exigem ID válido existente no repositório. |

---

## 📱 4. Módulos e Funcionalidades (Menu CLI)

O menu da aplicação organiza os fluxos principais e avançados:

```plaintext
==========================================================
               TASKTRACKER - MENU PRINCIPAL
==========================================================
  --- Requisitos Centrais da Fase 2 ---
  [1] Cadastrar nova tarefa
  [2] Visualizar tarefas cadastradas
  [3] Sair da aplicação
  --- Módulos Estendidos do Planejamento Lógico (Fase 1) ---
  [4] Buscar tarefa por ID
  [5] Atualizar status da tarefa
  [6] Editar tarefa
  [7] Remover tarefa
  [8] Filtrar tarefas por prioridade
----------------------------------------------------------
```

1. **Módulo 1 — Cadastrar Tarefa (`create_task`):** Solicita título, descrição, prioridade e data limite com validação em tempo real.
2. **Módulo 2 — Listar Tarefas (`list_tasks`):** Exibe a mensagem informativa `[INFO] Nenhuma tarefa cadastrada no momento.` quando vazia, ou cards formatados de todas as tarefas cadastradas.
3. **Módulo 3 — Sair da Aplicação:** Encerra a execução de forma elegante e amigável.
4. **Módulo 4 — Buscar por ID (`find_task_by_id`):** Localiza e detalha um registro específico pelo seu código numérico.
5. **Módulo 5 — Atualizar Status (`update_task_status`):** Permite alterar o progresso da tarefa (`1 - Pendente`, `2 - Em Andamento`, `3 - Concluída`).
6. **Módulo 6 — Editar Tarefa (`edit_task`):** Permite modificar campos específicos preservando os demais caso pressionado Enter.
7. **Módulo 7 — Remover Tarefa (`delete_task`):** Solicita confirmação de segurança (`S/N`) antes de deletar o registro.
8. **Módulo 8 — Filtrar por Prioridade (`filter_tasks_by_priority`):** Retorna o subconjunto de tarefas categorizadas por `"Alta"`, `"Média"` ou `"Baixa"`.

---

## 🚀 5. Guia de Instalação e Execução

### Pré-requisitos
- **Python 3.8+** instalado.
- **Git** configurado.

### Execução Local:
1. Abra o terminal na raiz do projeto:
   ```bash
   cd /Users/klaus/Projects/faculdade/taskmanager
   ```
2. Execute a aplicação diretamente via Python 3:
   ```bash
   python3 src/main.py
   ```

---

## 🌿 6. Estratégia de Versionamento Git

O versionamento segue a evolução solicitada no desafio e as boas práticas de Engenharia de Software com Commits Semânticos:

1. **Inicialização do Projeto (`git init`):** Criação do repositório local na branch `main`.
2. **Commit 1 (`docs`):** Registro do `README.md`, `.gitignore` e documento da Fase 1 (`docs/planejamento_logico.pdf`).
3. **Commit 2 (`feat`):** Implementação da estrutura principal em `src/main.py` (menu e loop principal).
4. **Commit 3 (`feat`):** Adição das funções de validação de dados (título não vazio e prioridades).
5. **Commit 4 (`refactor`):** Arquitetura em camadas modular (`Model`, `Repository`, `Service`, `Controller`) e cobertura dos 7 módulos do planejamento lógico.
6. **Publicação Remota (`git push`):** Vinculação do repositório remoto no GitHub (`origin main`).

---

## 📹 7. Roteiro Sugerido para Apresentação em Vídeo (YouTube)

O vídeo da Fase 2 deve ter 5 minutos de duração, formato horizontal (16:9), webcam ligada e voz própria:

- **00:00 - 00:30 (30s) — Introdução:** Apresentação pessoal (Klaus Müller Marques, RA 22301876, Ciência da Computação UniCEUB) e contexto da Fase 2 do Bootcamp II.
- **00:30 - 02:00 (1m30s) — Apresentação do GitHub:** Repositório publicado, árvore de pastas com a arquitetura em camadas, arquivo `docs/planejamento_logico.pdf` da Fase 1 e histórico de commits semânticos.
- **02:00 - 04:00 (2m) — Demonstração Prática:**
  - Execução de `python3 src/main.py`.
  - Exibir listagem vazia (opção 2).
  - Forçar erro de título vazio (opção 1) e erro de prioridade inválida (`Urgente`).
  - Cadastrar tarefa com sucesso e mostrar o status atribuído como `Pendente`.
  - Exibir a lista atualizada com a tarefa cadastrada.
  - (Opcional) Demonstrar atualização de status ou busca por ID.
  - Encerrar na opção 3.
- **04:00 - 04:30 (30s) — Encerramento:** Considerações finais e preparação para a Fase 3 (Docker, testes e deploy).
